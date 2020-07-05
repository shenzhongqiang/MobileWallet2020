from django.contrib import admin
from django.urls import path, include
from mainapp import views


urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('users/', views.list_users),
    path('usages/', views.list_usages),
    path('deposit/', views.deposit),
    path('balance/', views.get_balance),
    path('transactions/', views.get_user_transactions),
    path('all_transactions/', views.get_all_transactions),
    path('transfer/', views.transfer),
]

