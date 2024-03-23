from django.urls import  re_path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.show),
    re_path(r'^add/', views.add),
]