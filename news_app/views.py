from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView


from .models import News, Category
from .forms import ContactForm
from django.views import View

# Create your views here.
def news_list(request):
    news = get_list_or_404(News, status=News.Status.Published)

    context = {
        "news": news
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, news):
    new = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {
        'new': new
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

class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')
