from django.db import models
from django.contrib.auth.models import User

l1=(('back_pain','back_pain'),('constipation','constipation')
,('abdominal_pain','abdominal_pain'),('diarrhoea','diarrhoea'),('mild_fever','mild_fever'),('yellow_urine','yellow_urine'),
 ('yellowing_of_eyes','yellowing_of_eyes'),('acute_liver_failure','acute_liver_failure'),('fluid_overload','fluid_overload'),('swelling_of_stomach','swelling_of_stomach'),
('swelled_lymph_nodes','swelled_lymph_nodes'),('malaise','malaise'),('blurred_and_distorted_vision','blurred_and_distorted_vision'),('phlegm','phlegm'),('throat_irritation','throat_irritation'),
('redness_of_eyes','redness_of_eyes'),('sinus_pressure','sinus_pressure'),('runny_nose','runny_nose'),('congestion','congestion'),('chest_pain','chest_pain'),('weakness_in_limbs','weakness_in_limbs'),
('fast_heart_rate','fast_heart_rate'),('pain_during_bowel_movements','pain_during_bowel_movements'),('pain_in_anal_region','pain_in_anal_region'),('bloody_stool','bloody_stool'),
('irritation_in_anus','irritation_in_anus'),('neck_pain','neck_pain'),('dizziness','dizziness'),('cramps','cramps'),('bruising','bruising'),('obesity','obesity'),('swollen_legs','swollen_legs'),
('swollen_blood_vessels','swollen_blood_vessels'),('puffy_face_and_eyes','puffy_face_and_eyes'),('enlarged_thyroid','enlarged_thyroid'),('brittle_nails','brittle_nails'),
('swollen_extremeties','swollen_extremeties'),('excessive_hunger','excessive_hunger'),('extra_marital_contacts','extra_marital_contacts'),('drying_and_tingling_lips','drying_and_tingling_lips'),
('slurred_speech','slurred_speech'),('knee_pain','knee_pain'),('hip_joint_pain','hip_joint_pain'),('muscle_weakness','muscle_weakness'),('stiff_neck','stiff_neck'),('swelling_joints','swelling_joints'),
('movement_stiffness','movement_stiffness'),('spinning_movements','spinning_movements'),('loss_of_balance','loss_of_balance'),('unsteadiness','unsteadiness'),
('weakness_of_one_body_side','weakness_of_one_body_side'),('loss_of_smell','loss_of_smell'),('bladder_discomfort','bladder_discomfort'),('foul_smell_of urine','foul_smell_of urine'),
('continuous_feel_of_urine','continuous_feel_of_urine'),('passage_of_gases','passage_of_gases'),('internal_itching','internal_itching'),('toxic_look_(typhos)','toxic_look_(typhos)'),
('depression','depression'),('irritability','irritability'),('muscle_pain','muscle_pain'),('altered_sensorium','altered_sensorium'),('red_spots_over_body','red_spots_over_body'),('belly_pain','belly_pain'),
('abnormal_menstruation','abnormal_menstruation'),('dischromic _patches','dischromic _patches'),('watering_from_eyes','watering_from_eyes'),('increased_appetite','increased_appetite'),('polyuria','polyuria'),('family_history','family_history'),('mucoid_sputum','mucoid_sputum'),
('rusty_sputum','rusty_sputum'),('lack_of_concentration','lack_of_concentration'),('visual_disturbances','visual_disturbances'),('receiving_blood_transfusion','receiving_blood_transfusion'),
('receiving_unsterile_injections','receiving_unsterile_injections'),('coma','coma'),('stomach_bleeding','stomach_bleeding'),('distention_of_abdomen','distention_of_abdomen'),
('history_of_alcohol_consumption','history_of_alcohol_consumption'),('fluid_overload','fluid_overload'),('blood_in_sputum','blood_in_sputum'),('prominent_veins_on_calf','prominent_veins_on_calf'),
('palpitations','palpitations'),('painful_walking','painful_walking'),('pus_filled_pimples','pus_filled_pimples'),('blackheads','blackheads'),('scurring','scurring'),('skin_peeling','scurring'),
('silver_like_dusting','silver_like_dusting'),('small_dents_in_nails','small_dents_in_nails'),('inflammatory_nails','inflammatory_nails'),('blister','blister'),('red_sore_around_nose','red_sore_around_nose'),
('yellow_crust_ooze','yellow_crust_ooze'))

class UserProfileInfo(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	fname=models.CharField(max_length=100, default='')
	lname=models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	dob = models.DateField(blank=True,null=True,verbose_name="dob")

	def __str__(self):
		return self.user.username

class HospitalProfileInfo(models.Model):
	h_user=models.OneToOneField(User, on_delete=models.CASCADE)
	h_name=models.CharField(max_length=100, default='')
	h_city=models.CharField(max_length=100, default='')
	h_address=models.TextField(max_length=200,default='')

	def __str__(self):
		return self.h_user.username

class PharmacyProfileInfo(models.Model):
	p_user= models.OneToOneField(User, on_delete=models.CASCADE)
	p_name= models.CharField(max_length=100, default='')
	p_city=models.CharField(max_length=100, default='')
	p_address=models.TextField(max_length=200,default='')

	def __str__(self):
		return self.p_user.username

class Outbreak(models.Model):
	disease_name =models.CharField(max_length=100,default='')
	no_of_deaths = models.IntegerField(default=0)
	no_of_affected = models.IntegerField(default=0)
	location = models.CharField(max_length=100,default='')
	date = models.DateField(verbose_name="date")

	def __str__(self):
		return self.location

class disease_prediction(models.Model):
	symptoms_1 = models.CharField(max_length=30, choices=l1)
	symptoms_2 = models.CharField(max_length=30, choices=l1)
	symptoms_3 = models.CharField(max_length=30, choices=l1)
	symptoms_4 = models.CharField(max_length=30, choices=l1)
	symptoms_5 = models.CharField(max_length=30, choices=l1)

class citymap(models.Model):
	city = models.CharField(max_length=100)
	lat = models.FloatField(default=0.0)
	lng = models.FloatField(default=0.0)

class countrymap(models.Model):
	country = models.CharField(max_length=100)
	lat = models.FloatField(default=0.0)
	lng = models.FloatField(default=0.0)





