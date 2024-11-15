from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('fdi/', HomePage, name="home"),
    path('fdi/about/', AboutUs, name="about"),
    path('fdi/service/', Service, name="service"),
    path('fdi/supervisors/', Guard, name="supervisors"),
    path('fdi/contact/', ContactUS, name="contact"),
    path('fdi/register/', register, name="register"),
    path('fdi/login/', LoginView.as_view(template_name='main/login.html'), name="login"),
    path('fdi/logout/confirm/', Logout_Confirm, name='logout-confirm'),
    path('fdi/logout/', LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('fdi/personal/profile/', profile, name="profile"),
    path('fdi/personal/profile/history', history, name="history"),
    path('fdi/personal/profile/transfer/', transfer_money, name="transfer_money")
]