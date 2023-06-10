from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import dashboard, UserCreateView, user_register, edit_user, EditUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', dashboard, name='profile'),
    path('signup/', user_register, name='signup'),
    # path('profile/edit/', edit_user, name='edit'),
    path('profile/edit/', EditUserView.as_view(), name='edit'),
    # path('signup/', UserCreateView.as_view(), name='signup'),
    path('profile/', dashboard, name='profile'),
]