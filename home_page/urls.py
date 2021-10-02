from django.urls import path
from . import views


urlpatterns = [
    path('', views.myfunction, name="index"),

    path('intro/<str:name>/<int:age>', views.intro, name="intro"),

    path("home", views.home, name="natures home page"),
    path('packages', views.packages, name="packages page"),
    path('trek', views.trek, name="trek page"),
    path('sea diving', views.seadiving, name="diving page"),
    path('contactus', views.contact_us, name="contact_us"),
    path('addition', views.addition,name="addition"),
    path('destinations',views.destination,name="destinations"),
   
   

]
