from django.urls import path
from .views import news_list, news_detail, ContactPageView, CategoryNewsView, NewsDeleteView, NewsUpdateView

urlpatterns = [
    path('all/', news_list, name='news_list'),
    path('<slug:news>/', news_detail, name='news_detail_page'),
    path('<slug>/edit/', NewsUpdateView.as_view(), name='news_edit_page'),
    path('<slug>/delete/', NewsDeleteView.as_view(), name='news_delete_page'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path('category/<slug:cat_name>/', CategoryNewsView.as_view(), name='category_data')
]