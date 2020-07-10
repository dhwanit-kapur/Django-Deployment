from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Importing django built-ins for login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save user form data to the database
            user = user_form.save()

            # Generate password using hash algorithms(i.e. the hash password)
            user.set_password(user.password)

            # Save the hash password to the database
            user.save()

            # Deal with the extra attributes
            profile = profile_form.save(commit=False)
            # Establishing the OneToOne relationship inside views.py
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form':user_form,
                                                           'profile_form':profile_form,
                                                           'registered':registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("User authentication failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login credentials entered")
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in! Welcome!")
