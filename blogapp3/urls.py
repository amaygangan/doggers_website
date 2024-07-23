from django.urls import path
from blogapp3 import views

urlpatterns=[
    path("contact",views.contact),
    path("about",views.about),
    path("job",views.job)
]