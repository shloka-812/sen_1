
from django.shortcuts import render
from da.forms import UserForm,UserProfileInfoForm,HospitalProfileInfoForm,PharmacyProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Outbreak,HospitalProfileInfo,PharmacyProfileInfo
from django.contrib.auth.models import User
import requests as rq
import json
from django.http import JsonResponse


def index(request):
    return render(request,'da/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request,'da/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def register_h(request):
    registered=False
    if request.method == 'POST':
        h_user_form = UserForm(data=request.POST)
        h_profile_form = HospitalProfileInfoForm(data=request.POST)
        if h_user_form.is_valid() and h_profile_form.is_valid():
            h_user= h_user_form.save()
            h_user.set_password(h_user.password)
            h_user.save()
            profile = h_profile_form.save(commit=False)
            profile.h_user = h_user
            profile.save()
            registered = True
        else:
            print(h_user_form.errors,h_profile_form.errors)
    else:
        h_user_form = UserForm()
        h_profile_form = HospitalProfileInfoForm()
    return render(request,'da/registration_h.html',{'h_user_form':h_user_form,'h_profile_form':h_profile_form,'registered':registered})

def register_p(request):
    registered=False
    if request.method == 'POST':
        p_user_form = UserForm(data=request.POST)
        p_profile_form = PharmacyProfileInfoForm(data=request.POST)
        if p_user_form.is_valid() and p_profile_form.is_valid():
            p_user= p_user_form.save()
            p_user.set_password(p_user.password)
            p_user.save()
            profile = p_profile_form.save(commit=False)
            profile.p_user = p_user
            profile.save()
            registered = True
        else:
            print(p_user_form.errors,p_profile_form.errors)
    else:
        p_user_form = UserForm()
        p_profile_form = PharmacyProfileInfoForm()
    return render(request,'da/registration_p.html',{'p_user_form':p_user_form,'p_profile_form':p_profile_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password:{}".format(username,password))
            return HttpResponse("Invalid login details given")

    else:
        return render(request, 'da/login.html', {})

def newsfeed(request):
    #url = ('https://newsapi.org/v2/everything?'
     #  'q=Outbreaks&'
     #  'from=2019-04-08&'
     #  'sortBy=popularity&'
     #  'apiKey=962af2e30f5740c39bd6b0cb5a8b5de3')
    #response = rq.get(url)
    #return render_to_response("da/newsfeed.html", {"obj_as_json": json.dumps(response)})
    #return render(request,'da/newsfeed.html',response.json())
    #return HttpResponse(response, content_type='application/json')
    #return render(request,'da/newsfeed.html',{'current_date':'now'})
    #import requests
    url = ('https://newsapi.org/v2/everything?'
        'q=Outbreaks&'
        'from=2019-04-08&'
        'sortBy=popularity&'
        'apiKey=962af2e30f5740c39bd6b0cb5a8b5de3')
    response = rq.get(url)
    dict = response.json()
    count = 0
    text = ""
    for i in dict["articles"]:
        text = text + "Source :" + i["source"]["name"] + "<br>"
        if(i["author"]!=None):
            text = text + "Author :" + i["author"] + "<br>"
        text = text + "Description:" + i["description"] + "<br>"
        text = text + "url" + i["url"] + "<br>"
        text = text + "About" + i["content"] + "<br>"
        text= text +  "<br><br>"
        count = count + 1
        if(count == 10):
            break
    return render(request,'da/newsfeed.html',{'sent':text})

    
def keyfacts(request):
    return render(request,'da/keyfacts.html')

def outbreaks(request):
    return render(request,'da/outbreaks.html')

def prediction(request):
    return render(request,'da/prediction.html')

def aboutus(request):
    return render(request,'da/aboutus.html')

def help(request):
    return render(request,'da/help.html')

def feeddata(request):
    return render(request,'da/feeddata.html')

def outbreak(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
    try:
        h=HospitalProfileInfo.objects.filter(h_user = username)
        p=PharmacyProfileInfo.objects.filter(p_user = username)
        if h.exists() or p.exists():
            return render(request,'da/feed_data.html')

        else:
            return HttpResponse("sorry u cant enter the data")
    except HospitalProfileInfo.DoesNotExist:
        return HttpResponse("sorry u cant enter the data")


def outbreak_submission(request):
    disease_name = request.POST["disease_name"]
    no_of_deaths = request.POST["no_of_deaths"]
    no_of_affected = request.POST["no_of_affected"]
    location = request.POST["location"]
    date = request.POST["date"]

    outbrk = Outbreak(disease_name=disease_name, no_of_deaths = no_of_deaths, no_of_affected=no_of_affected, location=location, date=date)
    outbrk.save()
    return render(request,'da/feed_data.html')

