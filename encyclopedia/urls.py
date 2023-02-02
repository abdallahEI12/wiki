from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>", views.viewentry, name = "entry"),
    path("",views.gotowiki, name = "gotowiki"),
    path("new/",views.newpage, name="newpage"),
    path("editpage/<str:entry>",views.editpage, name="editpage"),
    path("randompage/", views.randompage, name = "randpage")

]
