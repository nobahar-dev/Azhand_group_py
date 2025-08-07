from django.urls import path
from . import views


app_name = 'avicenna'
urlpatterns = [
    path('', views.avicenna_page, name='avicenna_page'),
    path('article_detail/<int:article_id>', views.article_detail, name='article_detail'),
    path('category/<int:category_id>/<slug>/', views.avicenna_page, name='category'),
    path('comment/<int:article_id>/', views.article_comments, name='article_comments')
]