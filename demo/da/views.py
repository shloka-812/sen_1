import datetime
from django.shortcuts import render
from da.forms import UserForm,UserProfileInfoForm,HospitalProfileInfoForm,PharmacyProfileInfoForm,UserOutbreakInfoForm,DiseaseForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Outbreak,HospitalProfileInfo,PharmacyProfileInfo,Outbreak,disease_prediction,citymap,countrymap
from django.contrib.auth.models import User
import requests as rq
import json
from django.http import JsonResponse
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
import pickle

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

facts = ['When Syphilis first surfaced, the English called it the ‘French disease’, the French called it the ‘Spanish disease’, Germans called it the ‘French evil’, Russians called it ‘Polish disease’, Poles called it ‘Turkish disease’, Turks called it ‘Christian disease’ and Japan called it ‘Chinese pox.’',
'After needing 13 liters of blood for a surgery at the age of 13, a man named James Harrison pledged to donate blood once he turned 18. It was discovered that his blood contained a rare antigen which cured Rhesus disease. He has donated blood a record 1,000 times and saved 2,000,000 lives.',
'Farmers feed large magnets to cows to prevent “Hardware Disease.” Cow Magnets sit in their “stomach” for the lifetime of the cow and prevent accidentally eaten pieces of metal from lodging in the stomach folds causing illness.',
'Scurvy was documented as a disease by Hippocrates, and Egyptians have recorded its symptoms as early as 1550 BC. The knowledge that consuming foods containing vitamin C is a cure for scurvy has been repeatedly rediscovered and forgotten into the early 20th century.',
'Superior canal dehiscence is a rare medical condition that affects the inner ear and amplifies all internal sounds. It gets to the point where the sound of the eyeballs moving in their sockets sounds like “sandpaper on wood.”',
'While many woodland creatures harbor ticks and spread Lyme disease, opossums kill 96.5% of ticks that land on them and that a single opossum may be “hoovering up and killing” 4,000 ticks every week and thereby protecting us from Lyme disease.',
'During the AIDS epidemic of the 1980s, education about the disease was limited for political reasons. Surgeon General C. Everett Koop ended up infuriating members of both parties after he ordered that every home in America be mailed a letter explaining what AIDS was and how to protect from it.',
'King Philip the Fair of France (1268-1314) made skin diseases a punishable offence. He thought lepers should be buried alive.',
'The longest word in the Oxford Dictionary is pneumonoultramicroscopicsilicovolcanoconiosis, which is a 45-letter lung disease.',
'SDLqPlayStation palmar hidradentitisSDRq is a skin disease caused by gripping the console too tight.',
'Malaria was once used to treat syphilis. Dr. Wagner von Jauregg injected sufferers with malaria-infected blood, causing an extremely high fever that would ultimately kill the disease. Jauregg won the Nobel Prize for the treatment and it remained in use until the development of penicillin.',
'Alzheimer’s disease does not affect emotional memory as strongly as informational memory. As a result, Alzheimer’s patients given bad news will quickly forget the news, but will remain sad and have no idea why.',
'In 5,000 years of human history, only 2 diseases have been eradicated: smallpox and rinderpest.'
]

filename='da/modelpick'

def prediction(request):
    # if this is a POST request we need to process the form data
    form = DiseaseForm(request.POST or None)
    obj=disease_prediction()
    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)
    response=form.fields
    print(response)
    if request.POST:
        if form.is_valid():
            data = request.POST.copy()
            psymptoms = [data.get('symptoms_1'),data.get('symptoms_2'),data.get('symptoms_3'),data.get('symptoms_4'),data.get('symptoms_5')]
            loaded_model = pickle.load(open(filename, 'rb'))
           
            for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1
            inputtest = [l2]
            predict = loaded_model.predict(inputtest)
            predicted=predict[0]

            h='no'

            for a in range (0, len(disease)):
                if(predicted == a):
                    h='yes'
                    break
            if(h=='yes'):
                print(disease[a])
                form = DiseaseForm()
                
            return render(request,'da/prediction.html',{'diseasepredicted':disease[a],'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DiseaseForm()
    
    return render(request,'da/prediction.html',{'form': form})
    

def index(request):
    randchoice = np.random.randint(0,13)
    return render(request,'da/index.html',{'fact':facts[randchoice]})

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
	url = ('https://newsapi.org/v2/everything?'
		'q=Outbreaks&'
		'from=2019-04-08&'
		'sortBy=popularity&'
		'apiKey=962af2e30f5740c39bd6b0cb5a8b5de3')
	response = rq.get(url)
	dict = response.json()
	return render(request,'da/newsfeed.html',{'news':dict["articles"]})

	
def keyfacts(request):
    return render(request,'da/keyfacts.html')

def outbreaks(request):
    if request.method == 'POST':
        form = UserOutbreakInfoForm(request.POST)
        if form.is_valid():
            fdf = request.POST.get('from_date')
            tdf = request.POST.get('to_date')
            dnf = request.POST.get('disease')
            q = Outbreak.objects.all()
            q1 = q.filter(date__lte=tdf)
            q2 = q1.filter(date__gte=fdf)
            q3 = q2.filter(disease_name=dnf)
            if q3.exists():
                queryset = q3
            else:
                if q2.exists():
                    queryset = q2
                else: 
                    days100 = timezone.now() - datetime.timedelta(days=100)
                    queryset = Outbreak.objects.filter(date__gte=days100)
            i=0
            j=0
            k=0
            dloc={}
            aloc1={}
            aloc2={}
            dnum={}
            anum1={}
            anum2={}
            avga=0
            drefined = queryset.raw('SELECT 1 as id,location,SUM(no_of_deaths) as no_deaths FROM da_Outbreak GROUP BY location')
            arefined = queryset.raw('SELECT 1 as id,location,SUM(no_of_affected) as no_affected FROM da_Outbreak GROUP BY location')
            totala=0
            totalo=0
            for each in arefined:
                totala=totala+each.no_affected
                totalo=totalo+1
            avga=totala/totalo
            for each in drefined:
                loc = each.location
                cityobj = citymap.objects.filter(city=loc)
                if cityobj.exists() == False:
                    cityobj = countrymap.objects.filter(country=loc)
                if cityobj.exists():
                    if each.no_deaths > 0:
                        dloc[i] = [cityobj[0].lng,cityobj[0].lat]
                        dnum[i] = each.no_deaths
                        i=i+1
            for each in arefined:
                loc = each.location
                cityobj = citymap.objects.filter(city=loc)
                if cityobj.exists() == False:
                    cityobj = countrymap.objects.filter(country=loc)
                if cityobj.exists():
                    if each.no_affected > 0 :
                        if each.no_affected > avga :
                            aloc2[j] = [cityobj[0].lng,cityobj[0].lat]
                            anum2[j] = each.no_affected
                            j=j+1
                        else:
                            aloc1[k] = [cityobj[0].lng,cityobj[0].lat]
                            anum1[k] = each.no_affected
                            k=k+1
            return render(request, 'da/outbreaks.html', {'dq':dloc,'aq1':aloc1,'aq2':aloc2,'dn':dnum,'an1':anum1,'an2':anum2,'form':form,'fromDate':fdf,'toDate':tdf,'diseaseName':dnf})
    else:
        days100 = timezone.now() - datetime.timedelta(days=100)
        queryset = Outbreak.objects.filter(date__gte=days100)
        i=0
        j=0
        k=0
        dloc={}
        aloc1={}
        aloc2={}
        dnum={}
        anum1={}
        anum2={}
        avga=0
        drefined = queryset.raw('SELECT 1 as id,location,SUM(no_of_deaths) as no_deaths FROM da_Outbreak GROUP BY location')
        arefined = queryset.raw('SELECT 1 as id,location,SUM(no_of_affected) as no_affected FROM da_Outbreak GROUP BY location')
        totala=0
        totalo=0
        for each in arefined:
            totala=totala+each.no_affected
            totalo=totalo+1
        avga=totala/totalo
        for each in drefined:
            loc = each.location
            cityobj = citymap.objects.filter(city=loc)
            if cityobj.exists() == False:
                cityobj = countrymap.objects.filter(country=loc)
            if cityobj.exists():
                if each.no_deaths > 0:
                    dloc[i] = [cityobj[0].lng,cityobj[0].lat]
                    dnum[i] = each.no_deaths
                    i=i+1
        for each in arefined:
            loc = each.location
            cityobj = citymap.objects.filter(city=loc)
            if cityobj.exists() == False:
                cityobj = countrymap.objects.filter(country=loc)
            if cityobj.exists():
                if each.no_affected > 0 :
                    if each.no_affected >avga :
                        aloc2[j] = [cityobj[0].lng,cityobj[0].lat]
                        anum2[j] = each.no_affected
                        j=j+1
                    else:
                        aloc1[k] = [cityobj[0].lng,cityobj[0].lat]
                        anum1[k] = each.no_affected
                        k=k+1
        form = UserOutbreakInfoForm()

    return render(request, 'da/outbreaks.html', {'dq':dloc,'aq1':aloc1,'aq2':aloc2,'dn':dnum,'an1':anum1,'an2':anum2,'form': form})

def aboutus(request):
    return render(request,'da/aboutus.html')

def help(request):
    return render(request,'da/help.html')

def feeddata(request):
    username = None
    if request.user.is_authenticated:
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

