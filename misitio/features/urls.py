from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('list/', views.view_list, name='view_list'),
    path('list/add', views.add, name='add'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('grid_list/', views.grid_view, name='grid_view'),
    path('add/', views.add_grid, name='add_grid'),
    path('grid_list/delete/<int:grid_id>/', views.delete_grid, name='delete_grid'),
    path('grid_list/edit/<int:grid_id>/<int:element>/', views.edit_grid, name='edit_grid'),
    path('grid_list/predit/<int:grid_id>/<int:element>/', views.predit_grid, name='predit_grid'),
    path('grid_list/search/', views.search, name='search'),
    path('grid_list/sort/<str:element>/<str:sorting>/', views.sort, name='sort'),
]