from django.urls import path, re_path

from . import views

app_name = 'linkApp'
urlpatterns = [
    path('', views.linkList, name='linkList'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('landing/<site_name>', views.landingLink, name="landingLink"),
]
