from django.urls import path
from blogapp2 import views

urlpatterns = [
   path("idle",views.idle)
]