from django.urls import  re_path, path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show, name='home'),
    path('add/', views.add, name='add'),
    path('detail/<int:detail_id>/', views.read, name='detail'),
    path('edit/<int:detail_id>/', views.edit, name="edit"),
    path('delete/<int:detail_id>/', views.delete, name="delete"),
]