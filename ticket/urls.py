from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('tickets', views.show_ticket, name ='show_ticket'),
    path('tickets/<int:pk>', views.show_tickets, name ='show_tickets'),
    path('response', views.response, name='response'),
    path('register', views.register, name='register'),
    path('login',views.login_view,name='login_view'),
    path('add_ticket',views.index,name='index'),
    path('logout', views.logout, name='logout'),
    path('remaining-tickets', views.remaining_ticket, name ='remaining_ticket'),
    path('remaining-tickets/<int:pk>', views.remaining_tickets, name ='remaining_tickets'),
    path('update_ticket/<int:pk>', views.update_ticket, name ='update_ticket'),
    path('response_update/<int:pk>', views.response_update, name ='response_update'),
]