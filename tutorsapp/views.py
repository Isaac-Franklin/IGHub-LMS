from django.shortcuts import render, redirect
from .models import *
from useronboard.models import user_reg
from lmsapp.models import *
from django.contrib import messages
from django.db.models import Q



# Create your views here.


def Dashboard(request):
    grades = GradeStudent.objects.all()
    students = user_reg.objects.all()
    quizanswer = Answer.objects.all()
    videos = Video_upload.objects.all()
    numberofstudents = students.count()
    quiz = Quiz.objects.all()
    rooms = Rooms.objects.all()
    assign = Assignment.objects.all()
    # responses = rooms.response_set.get().order_by('-created')
    responses = Response.objects.all()
    context = {'grades':grades, "students": students, 'quiz':quiz, 'quizanswer' :quizanswer, "responses": responses,
               "numberofstudents": numberofstudents, "videos": videos, "rooms": rooms, "assign": assign}
    return render(request, 'tutorsapp/dashboard.html', context)


def Fellow_scores(request):
    if request.method == 'POST':
        form = Scores(request.POST)
        # if form.is_valid():
        firstname = request.POST['firstname']
        track = request.POST['track']
        score = request.POST['fellowscore']
        scoresform = Scores(name=firstname, track=track, score=score)
        scoresform.save()
        form.save()
        return redirect('Fellowscores')
        messages.success(request, 'Update Successful')
    # fellows = user_reg.objects.all()
    # context = {"fellows": fellows}
    return render(request, 'tutorsapp/scores.html')


def UpdateScores(request):
    scores = Fellow_scores.objects.all()
    context = {"scores": scores}
    return render(request, 'scoresform.html', context)


def Nav(request):
    return render(request, 'generalnav.html')


# @login_required
def Tutor_Assignment_page(request, pk):
    assin = Assignment.objects.get(id=pk)
    context = {'assin': assin}
    return render(request, 'tutorsapp/tutorassignment.html', context)


def FellowTrack(request):
    query = request.GET.get('query') if request.GET.get(
        'query') != None else ''

    trackresult = user_reg.objects.filter(
        Q(firstname__icontains=query) |
        Q(lastname__icontains=query) |
        Q(username__icontains=query) |
        Q(email__icontains=query) |
        Q(track__icontains=query)
    )
    fellows = user_reg.objects.all()
    data = user_reg.objects.all()
    context = {'data': data, 'fellows': fellows, "trackresult": trackresult}
    return render(request, 'tutorsapp/fellowtrack.html', context)


def TutorQuestion(request):
    data = Rooms.objects.all()
    # responses = data.response_set.all()
    context = {'data': data}
    return render(request, 'tutorsapp/tutorquestion.html', context)


def TutorQuestiondetails(request, pk):
    quiz = Rooms.objects.get(id = pk)
    responses = quiz.response_set.all().order_by('-created')
    count_responses = responses.count()

    if request.method == 'POST':
        response = Response.objects.create(
            user=request.user,
            room = quiz,
            body=request.POST.get('body')
        )
        # else:
        #     messages.error(request, 'Fill The Form Properly')
        return redirect('TutorQuestiondetails', pk=quiz.id)

    context = {'quiz': quiz, "responses": responses,
               "count_responses": count_responses}
    return render(request, 'tutorsapp/tutorquestiondetails.html', context)


def TutorTutorials(request):
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    video = Video_upload.objects.all()
    context = {'video': video}
    return render(request, 'tutorsapp/tutortutorialvideos.html', context)


def Createassignment(request):
    if request.method == 'POST':
        form = Assignment(request.POST)
        user = request.user
        title = request.POST.get('title')
        track = request.POST.get('track')
        short_description = request.POST.get('shortdescription')
        detailed_description = request.POST.get('detaileddescription')
        resources = request.POST.get('resources')
        mode_of_submission = request.POST.get('modeofsubmission')
        task_point = request.POST.get('task_point')
        data_of_submission = request.POST.get('dataofsubmission')
        # if form.is_valid():
        createassign = Assignment(user=user, title=title, track=track, short_description=short_description, detailed_description=detailed_description,
                                  resources=resources, mode_of_submission=mode_of_submission, task_point=task_point, data_of_submission=data_of_submission)
        createassign.save()
        # form.save()
        messages.success(request, 'Assignment Successfully Created')
    return render(request, 'tutorsapp/createassignment.html')


def VideoUpload(request):
    if request.method == "POST":
        user = request.user
        track = request.POST['track']
        title = request.POST['title']
        description = request.POST['description']
        videofile = request.POST['videofile']
        uploadvideofile = Video_upload(
            user=user, Select_Track=track, Select_Title=title, Video_Description=description, Video=videofile)
        uploadvideofile.save()
        messages.success(request, 'Video Tutorial Successfully Uploaded')
    return render(request, 'tutorsapp/uploadvideo.html')


def Tutorquiz(request):
    quizproper = Quiz.objects.all()
    context = {'quizproper':quizproper}
    return render(request, 'tutorsapp/tutorquiz.html', context)


def TutorQuizdetails(request, pk):
    quizproper = Quiz.objects.get(id = pk)
    quizes = Rooms.objects.all()
    Allquizanswer = quizproper.answer_set.all().order_by('-created_at')
    quizanswerscount = Allquizanswer.count()
    quizanswer = quizproper.answer_set.all().order_by('-created_at')
    if request.method == 'POST':
        response = Answer.objects.create(
            user=request.user,
            quiz=quizproper,
            response=request.POST.get('body')
        )
        # else:
        #     messages.error(request, 'Fill The Form Properly')
        return redirect('TutorQuizdetails', pk=quizproper.id)
    context = {'quizproper' : quizproper, 'quizanswerscount': quizanswerscount, 'quizes':quizes,  'quizanswer':quizanswer, 'Allquizanswer':Allquizanswer}
    return render(request, 'tutorsapp/tutorquizdetails.html', context)



def DeleteResponse(request, pk):
    response = Response.objects.get(id=pk)
    response.delete()
    return redirect('TutorQuestion')
    return render(request, 'tutorsapp/tutorquestiondetails.html')


def Tutorprofile(request, username):
    userData = user_reg.objects.get(username=username)
    roomdata = Rooms.objects.all()
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'userData':userData, 'data':data, 'roomdata':roomdata}
    return render (request, 'tutorsapp/tutorprofile.html', context)


def Createroom(request):
    if request.method == 'POST':
        user = request.user
        question = request.POST['question']
        tips = request.POST['tips']
        form = Rooms(user = user, question = question, tips=tips)
        form.save()
        messages.success(request, 'Room Created Successfully')
        return redirect('TutorQuestion')
    return render(request, 'tutorsapp/createroom.html')


def Createquiz(request):
    if request.method == 'POST':
        user = request.user
        quiz = request.POST['quiz']
        prize = request.POST['prize']
        notes = request.POST['notes']
        # expiredate = request.POST['expiredate']
        form = Quiz(user = user, quiz = quiz, prize=prize, notes=notes)
        form.save()
        messages.success(request, 'Quiz Created Successfully')
        return redirect('Tutorquiz')
    return render(request, 'tutorsapp/createquiz.html')