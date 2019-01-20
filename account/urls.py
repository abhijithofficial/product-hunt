from django.urls import path
from . import views as view

urlpatterns = [
path('login/',view.login,name="login"),
path('signup/',view.signup,name="signup"),
path('logout/',view.logout,name="logout"),

 ]
