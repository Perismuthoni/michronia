from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
     path("home/", views.home, name="home"),
      path("services/", views.services, name="services"),
      path("keeping/", views.keeping, name="keeping"),
      path("consultancy/", views.consultancy, name="consultancy"),
      path("Accountancy/", views.Accountancy, name="Accountancy"),
      path("Advisory/", views.Advisory, name="Advisory"),
    path("about/", views.about, name="about"), 
     path("contact/", views.contact, name="contact"), 
     
     
    path("search/", views.search, name="search"),  
    path("loggedin_contact/", views.loggedin_contact, name="loggedin_contact"),
    path("register/", views.register, name="register"),
    path("registerbsn/", views.registerbsn, name="registerbsn"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
   
    
]