from django import forms
from da.models import UserProfileInfo,HospitalProfileInfo,PharmacyProfileInfo,disease_prediction
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
		fields=('fname','lname','city','dob')

class HospitalProfileInfoForm(forms.ModelForm):
	class Meta():
		model=HospitalProfileInfo
		fields=('h_name','h_city','h_address')

class PharmacyProfileInfoForm(forms.ModelForm):
	class Meta():
		model=PharmacyProfileInfo
		fields=('p_name','p_city','p_address')

class UserOutbreakInfoForm(forms.Form):
	from_date = forms.DateField(label='Enter From date for outbreaks')
	to_date = forms.DateField(label='Enter To date for outbreaks')
	disease = forms.CharField(label='Disease Name',max_length=200)




