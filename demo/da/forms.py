from django import forms
from da.models import UserProfileInfo,HospitalProfileInfo,PharmacyProfileInfo,disease_prediction,outbreakform
from django.contrib.auth.models import User

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = disease_prediction
        fields = ['symptoms_1', 'symptoms_2', 'symptoms_3', 'symptoms_4', 'symptoms_5']

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model=User
		fields=('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model=UserProfileInfo
		fields=('first_name','last_name','city','dob')

class HospitalProfileInfoForm(forms.ModelForm):
	class Meta():
		model=HospitalProfileInfo
		fields=('hospital_name','hospital_city','hospital_address')

class PharmacyProfileInfoForm(forms.ModelForm):
	class Meta():
		model=PharmacyProfileInfo
		fields=('pharmacy_name','pharmacy_city','pharmacy_address')

class UserOutbreakInfoForm(forms.ModelForm):
	class Meta():
		model=outbreakform
		fields=('from_date','to_date','disease')





