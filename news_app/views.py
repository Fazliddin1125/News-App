from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .custom_permission import OnlyLoggedSuperUser
from .models import News, Category
from .forms import ContactForm, CommentForm
from django.views import View
from django.shortcuts import redirect
from django.db.models import Q, Count
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

# Create your views here.

def news_detail(request, news):
    new = get_object_or_404(News, slug=news, status=News.Status.Published)


    comments = new.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None



    if request.method == "POST":
        print("Helloooooo")
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.news = new
                new_comment.user = request.user
                new_comment.save()
                comment_form = CommentForm()
            else:
                comment_form = CommentForm()
        else:
            return redirect('login')
    else:
        comment_form = CommentForm()
        comment_count = comments.count()

    context = {
        'news': new,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count
    }
    return render(request, 'news/news_detail.html', context)

def indexView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:10]
    local_one = News.published.all().filter(category__name='Mahalliy').order_by("-publish_time")[0]
    local_news = News.published.all().filter(category__name='Mahalliy')[1:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
        'local_one': local_one
    }

    return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:10]
        context['local_one'] = News.published.all().filter(category__name='Mahalliy').order_by("-publish_time")[0]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name='Mahalliy')[:5]
        context['texnologiya'] = News.published.all().filter(category__name='Texnogiya')[:5]
        context['xorijiy'] = News.published.all().filter(category__name='Xorijiy')[:5]
        context['sport'] = News.published.all().filter(category__name='Sport')[:5]

        return context


class ContactPageView(View):
    template_name = 'news/contact.html'

    def get(self, request):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)


    def post(self, request):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur</h2>")
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)

class CategoryNewsView(View):
    def get(self, request, cat_name):

        CategoryNews = get_list_or_404(News, category__name=cat_name)
        context = {
            'category_data': CategoryNews,
            'name': cat_name
        }
        return render(request, 'news/category_page.html', context)

class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'

class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')

class NewsCreateView(OnlyLoggedSuperUser , CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category')
    prepopulated_fields = {"slug": ('title',)}


class SearchResultsList(ListView):
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'barcha_yangiliklar'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
