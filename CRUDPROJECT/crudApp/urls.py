from django.urls import path
from .views import home,contact,about,form,search,delete_data,update


urlpatterns = [
    path("",home,name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path("form/",form,name="form"),
    path("search/",search,name='search'),
    path("delete/<int:id>",delete_data,name='delete'),
    path("update/<int:id>",update,name='update'),
]



