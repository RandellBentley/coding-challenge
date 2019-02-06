from django.urls import path

from . import views

app_name = 'linkApp'
urlpatterns = [
    path('', views.linkList, name='linkList'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
]
