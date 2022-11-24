from django.shortcuts import render, redirect
from .models import *
from useronboard.models import *
from tutorsapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.


@login_required
def VideoUpload(request):
    return request(request,  template_name='videoupload.html')


@login_required
def Dashboard(request):
    userData = user_reg.objects.all()
    quizes = Quiz.objects.all().first()
    video = Video_upload.objects.all()
    assign = Assignment.objects.all()
    room = Rooms.objects.all().first()
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'video': video, 'userData': userData,
               'data': data, "quiz": room, "assign": assign, 'quizes':quizes}
    return render(request, 'lmsapp/dashboard.html', context)


@login_required()
def TrackList(request):
    # if request.user.is_authenticated:
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
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'fellows': fellows, 'data':data, "trackresult": trackresult}
    return render(request, 'lmsapp/tracks.html', context)


@login_required()
def Tutorial(request):
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    video = Video_upload.objects.all()
    context = {'video': video, 'data': data}
    return render(request, 'lmsapp/tutorials.html', context)


@login_required()
def Room(request):
    roomdata = Rooms.objects.all()
    userData = user_reg.objects.all()
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'roomdata': roomdata, 'userData':userData, 'data':data}
    return render(request, 'lmsapp/rooms.html', context)


@login_required()
def RoomDetails(request, pk):
    room = Rooms.objects.get(id=pk)
    responses = room.response_set.all().order_by('-created')
    count_responses = responses.count()

    if request.method == 'POST':
        response = Response.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        # else:
        #     messages.error(request, 'Fill The Form Properly')
        return redirect('RoomDetails', pk=room.id)

    context = {'quiz': room, "responses": responses,
               "count_responses": count_responses}
    return render(request, 'lmsapp/RoomDetails.html', context)


@login_required()
def Assignment_page(request, pk):
    assin = Assignment.objects.get(id=pk)
    if request.method == "POST":
        user = request.user
        assignment = assin
        submission = request.POST['submission']
        form = Assignment_submission(
            user=user, assignment=assignment, submission=submission)
        form.save()
        messages.success(request, 'Assignment Submission Was Successful')
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'assin': assin, 'data' : data}
    return render(request, 'lmsapp/assignment.html', context)


def AllAssignments(request):
    query = request.GET.get('query') if request.GET.get(
        'query') != None else ''

    assin = Assignment.objects.filter(
        Q(title__icontains=query) |
        Q(track__icontains=query) |
        Q(detailed_description__icontains=query)
    )
    context = {"assin": assin}
    return render(request, 'lmsapp/allassignments.html', context)


def AssignmentSumList(request, pk):
    assign = Assignment.objects.get(id=pk)
    sub = assign.assignment_submission_set.all().order_by('-created')
    numberofsubmit = sub.count()
    if request.method == 'POST':
        assignment = assign
        name = request.POST['fellowname']
        submission = request.POST['assignment']
        time_of_submission = request.POST['submissiontime']
        score = request.POST['assignmentscore']
        feedback = request.POST['feedback']
        form = GradeStudent(assignment = assignment, name = name, submission=submission, time_of_submission=time_of_submission, score=score, feedback=feedback)
        form.save()
        return redirect('AllAssignments')
        messages.success(request, 'Assignment Grading Done Successfully')
    context = {"sub": sub, "assign": assign,
               "numberofsubmit": numberofsubmit}
    return render(request, 'lmsapp/assignmentsumlist.html', context)



def logoutUser(request):
    logout(request)
    return redirect('/useronboard/')


def NavBar(request):
    # if request.user.is_authenticated:
    # if request.user.is_authenticated:
    data = user_reg.objects.all()
    # data = user_reg.objects.filter(username=request.user.username).first()
    context = {'data': data}
    return render(request, 'general.html', context)


def CreateRoom(request):
    if request.method == 'POST':
        user = request.user
        question = request.POST['question']
        tips = request.POST['tips']
        form = Rooms(user = user, question = question, tips=tips)
        form.save()
        messages.success(request, 'Room Created Successfully')
        return redirect('Room')
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context= {'data':data}
    return render(request, 'lmsapp/createroom.html', context)


def ReportSubmit(request):
    if request.method == 'POST':
        user = request.user
        addressto = request.POST['address']
        report = request.POST['reportproper']
        form = Report(user=user,addressto=addressto,report=report)
        form.save()
        messages.success(request, 'Report Submitted Successfully');
        return redirect('Report')
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context= {'data':data}
    return render(request, 'lmsapp/report.html', context)




def DeleteRoom(request, pk):
    room = Rooms.objects.get(id = pk)
    room.delete()
    return redirect('Room')
    messages.success(request, 'Room Deleted Successfully')
    return render(request, 'lmsapp/rooms.html')
    
    
    
def DeleteResponse(request, pk):
    response = Response.objects.get(id=pk)
    response.delete()
    return redirect('Room')
    messages.success(request, 'Response Deleted Successfully') 
    return render(request, 'lmsapp/rooms.html')         


def Profile(request, username):
    userData = user_reg.objects.get(username=username)
    roomdata = Rooms.objects.all()
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'userData':userData, 'data':data, 'roomdata':roomdata}
    return render (request, 'lmsapp/profile.html', context)


def AllScores(request):
    grades = GradeStudent.objects.all()
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
    context = {'grades':grades, 'data':data}
    return render(request, 'lmsapp/allScores.html', context)


def Quizsection(request):
    quizes = Quiz.objects.all()
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
        context = {'data':data, 'quizes':quizes}
    return render(request, 'lmsapp/quiz.html', context)


def Quizdetails(request, pk):
    quiz = Quiz.objects.get(id = pk)
    if request.method == 'POST':
        response = Answer.objects.create(
        user=request.user,
        quiz=quiz,
        response=request.POST.get('response')
    )
        messages.success(request, 'Response Submitted Successfully') 
    if request.user.is_authenticated:
        data = user_reg.objects.filter(username=request.user.username).first()
        context = {'data':data, 'quiz':quiz}
    return render(request, 'lmsapp/quizdetails.html', context)
    