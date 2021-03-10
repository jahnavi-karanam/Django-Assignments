from django.urls import path

from . import views

urlpatterns = [
    path('w/', views.welcome, name='welcome'),
    path('h/',views.hi, name="hi"),
]