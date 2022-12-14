from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('stock', views.stockMarket, name='stockMarket'),
    path('blog', views.blog, name='blog'),
    path('post/<str:pk>', views.post, name='post'),
    path('chat', views.chat, name='chat'),
    path('checkview', views.checkview, name='checkview'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),    
    path('getMessages/<str:room>/', views.getMessages, name='getmessages'),  
]
