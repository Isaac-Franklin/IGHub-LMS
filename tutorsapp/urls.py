from django.urls import path
from . import views


urlpatterns = [
    path("", views.Dashboard, name="Dashboard"),
    path("scores/", views.Fellow_scores, name="Fellowscores"),
    path("nav/", views.Nav, name="Nav"),
    path("fellowtrack/", views.FellowTrack, name="FellowTrack"),
    path("tutorquestion/", views.TutorQuestion, name="TutorQuestion"),
    path("tutortutorialpage/", views.TutorTutorials, name="TutorTutorials"),
    path("createassignment/", views.Createassignment, name="Createassignment"),
    path("videoupload/", views.VideoUpload, name="VideoUpload"),
    path("tutorquiz/", views.Tutorquiz, name="Tutorquiz"),
    path("createroom/", views.Createroom, name="Createroom"),
    path("createquiz/", views.Createquiz, name="Createquiz"),
    path("tutorquizdetails/<str:pk>/",
         views.TutorQuizdetails, name="TutorQuizdetails"),
    path("tutorquestiondetails/<str:pk>/",
         views.TutorQuestiondetails, name="TutorQuestiondetails"),
    path("tutorassignment/<str:pk>/",
         views.Tutor_Assignment_page, name="Tutor_Assignment_page"),
    path("deleteresponse/<str:pk>/",
         views.DeleteResponse, name="DeleteResponse"),
    path("tutorprofile/<str:username>/",
         views.Tutorprofile, name="Tutorprofile")
]
