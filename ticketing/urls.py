from django.urls import path
from . import views


app_name = 'ticketing'
urlpatterns = [
    path('', views.request_ticket, name='request_ticket'),
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('ticket_detail/<int:ticket_id>/', views.ticket_detail, name='ticket_detail')
]
