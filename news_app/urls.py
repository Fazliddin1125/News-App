from django.urls import path
from .views import news_detail, ContactPageView, CategoryNewsView, NewsDeleteView, NewsUpdateView, NewsCreateView, SearchResultsList

urlpatterns = [
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),
    path('create/', NewsCreateView.as_view(), name='news_create_page'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path('<slug:news>/', news_detail, name='news_detail_page'),
    path('<slug>/edit/', NewsUpdateView.as_view(), name='news_edit_page'),
    path('<slug>/delete/', NewsDeleteView.as_view(), name='news_delete_page'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path('category/<slug:cat_name>/', CategoryNewsView.as_view(), name='category_data'),

]