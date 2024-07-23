from django.urls import path
from blogapp1 import views

urlpatterns = [
    path('',views.user_login),
    path("info",views.info),
    path("stud/<sid>",views.stud),
    path("add/<x>/<y>",views.add),
    path("Hello",views.hello),
    path("hyedad",views.hyedad),
    path("code",views.code),
    path("test",views.test),
    path("learnstatic",views.lstat),
    path("dognation",views.dogn),
    path("dashboard",views.dashboard),
    path("edit/<rid>",views.edit),
    path("delete/<rid>",views.delete),
    path("gender/<gid>",views.gender),
    path("vaccine/<vid>",views.vaccine),
    path("price/<a>",views.price),
    path("filp/<fid>",views.filp),
    path("multifilter",views.multifilter),
    path("djforms",views.django_form),
    path("dognationmof",views.modelform),
    path("registeruser",views.userregform),
    path("userlogin",views.user_login),
    path("setcookie",views.setcookie),
    path("getcookie",views.getcookie),
    path("setsession",views.setsession),
    path("getsession",views.getsession)
]