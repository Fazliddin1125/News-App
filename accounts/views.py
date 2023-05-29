from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


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