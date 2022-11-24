from django.urls import path
from . import views

urlpatterns = [
    path("videoupload/", views.VideoUpload, name="videoupload"),
    path("", views.Dashboard, name="dashboard"),
    path("tracks/", views.TrackList, name="Track"),
    path("tutorial/", views.Tutorial, name="Tutorial"),
    path("room/", views.Room, name="Room"),
    path("roomdetails/<str:pk>/", views.RoomDetails, name="RoomDetails"),
    path("assignment/<str:pk>/", views.Assignment_page, name="Assignment"),
    path("allassignments/", views.AllAssignments, name="AllAssignments"),
    path("report/", views.ReportSubmit, name="Report"),
    path("assignmentsumlist/<str:pk>/",
         views.AssignmentSumList, name="AssignmentSumList"),
    path('logout/', views.logoutUser, name="logout"),
    path("navbar/", views.NavBar, name="navbar"),
    path("createroom/", views.CreateRoom, name="CreateRoom"),
    path("allscores/", views.AllScores, name="AllScores"),
    path("quiz/", views.Quizsection, name="Quizsection"),
    path("delete/<str:pk>/", views.DeleteRoom, name="DeleteRoom"),
    path("quizdetails/<str:pk>/", views.Quizdetails, name="Quizdetails"),
    path("deleteresponse/<str:pk>/", views.DeleteResponse, name="DeleteResponse"),
    path("profile/<str:username>/", views.Profile, name="Profile"),
]
