from django.urls import path, include 
from . import views

urlpatterns = [
    path('firstapi/', views.firstApi, name='firstapi'),
    path('signup/', views.signup, name='signup'),
    path('signup/<int:id>', views.signup, name='signup')
]
