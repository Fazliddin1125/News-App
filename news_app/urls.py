from django.urls import path
from .views import news_list, news_detail, ContactPageView, CategoryNewsView

urlpatterns = [
    path('all/', news_list, name='news_list'),
    path('<slug:news>/', news_detail, name='news_detail_page'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path('category/<slug:cat_name>/', CategoryNewsView.as_view(), name='category_data')
]