from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_reg
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from useronboard.models import user_reg


# Create your views here.


# def User(request):
#     return render(request, '')


def Userreg(request):
    if request.method == 'POST':
        # form = user_reg(request.POST, request.FILES)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        fullname = request.POST['username']
        email = request.POST['email']
        track = request.POST['track']
        phonenumber = request.POST['phonenumber']
        dateofbirth = request.POST['dateofbirth']
        password = request.POST['password']
        rtpassword = request.POST['rtpassword']
        GitHub = request.POST['githubacctlink']
        LinkedIn = request.POST['linkedinacctlink']
        Twitter = request.POST['twitteracctlink']
        Facebook = request.POST['facebookacctlink']
        Instagram = request.POST['instagramacctlink']
        PortFolio_Website = request.POST['portfoliowebsitelink']
        Profilepicture = request.FILES['profilepic']
        if password != rtpassword:
            messages.error(request, 'Passwords Are Not Same')
            return redirect('userreg')

        data = user_reg.objects.filter(username=fullname)
        if data:
            messages.error(request, 'Sorry, Username Is Already Taken')
            return redirect('userreg')
        else:
            messages.success(request, 'Registration Successful')
            user = user_reg(firstname=firstname, lastname=lastname, username=fullname, email=email,
                            track=track, phone=phonenumber, dateofbirth=dateofbirth, password=password, repassword=rtpassword, github=GitHub, linkedIn=LinkedIn,
                            twitter=Twitter, facebook=Facebook, instagram=Instagram, portfoliowebsite=PortFolio_Website, profilepicture=Profilepicture)

            user = User.objects.create_user(
                username=fullname, email=email, password=password, first_name=firstname, last_name=lastname)
            login(request, user)
            user.save()
            # form.save()
            return redirect('userlogin')
            messages.success(request, 'Registration Successful')
    return render(request, 'useronboard/fullsignup.html')


# LOGIN FUNCTION
def Login_User(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Login Failed: User Does Not Exit')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, 'Login Successfull')
            return redirect('dashboard')

        else:
            messages.error(request, 'Login Failed: Please Try Again')
            return render(request, 'useronboard/userlogin.html')
    return render(request, 'useronboard/userlogin.html')


def TestPage(request):
    data = user_reg.objects.all()
    context = {'data': data}
    return render(request, 'useronboard/testpage.html', context)


def ProfilePic(request, id):
    return render(request, 'profilepicture.html')


#    if request.user.is_authenticated:
#         data = user_reg.objects.filter(username=request.user.username).first()
#         context = {'data': data}
#         return render(request, 'useronboard/testpage.html', context)
