from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Muzafaqiyatli login amalga oshirildi")
                else:
                    return HttpResponse("Sizning profilingiz activ holatda emas")
            else:
                return HttpResponse("Parol yoki Username xato")

        else:
            return HttpResponse("Formani to'ldiring")

    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"login_form": form})



def dashboard(request):
    user = request.user

    context = {
        'user': user
    }

    return render(request, 'pages/dashboard.html', context)


# def user_register(request):
#     if request.method == "POST":
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password']
#             )
#             new_user.save()
#             context = {
#                 "new_user": new_user
#             }
#             return render(request, 'registration/register_done.html', context)
#     else:
#         user_form = UserRegistrationForm()
#         context = {
#             "user_form": user_form
#         }
#         return render(request, 'registration/register.html', context)



class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"