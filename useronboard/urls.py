from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.Userreg, name="userreg"),
    path('', views.Login_User, name="userlogin"),
    path('testpage/', views.TestPage, name='testpage'),
    path('profilepic/<str:id>/', views.ProfilePic, name="profilepic"),

]
