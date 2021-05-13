from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('<str:language>/<int:number>/<int:hide>/', views.study, name='study'),
    path('<str:language>/<int:number>/', views.evaluate, name='evaluate'),
]