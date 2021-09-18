from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clf/<str:sentence>/', views.clf, name='clf'),
]
