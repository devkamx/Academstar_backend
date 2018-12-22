from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='courses'),
    path('<int:courses_id>', views.courses, name='courses'),
    path('search', views.search, name='search'),
]
