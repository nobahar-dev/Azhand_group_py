from django.urls import path
from . import views


app_name = 'office'
urlpatterns = [
    path('', views.office_page, name='office_page'),
    path('article_detail/<int:article_id>', views.article_detail, name='article_detail'),
    path('category/<int:category_id>/<slug>/', views.office_page, name='category'),
    path('comment/<int:article_id>/', views.article_comments, name='article_comments')
]
