from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('add_advertisement', views.add_advertisement, name='add_advertisement'),
]