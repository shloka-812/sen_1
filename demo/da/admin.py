from django.contrib import admin
from da.models import UserProfileInfo,HospitalProfileInfo,PharmacyProfileInfo,User,Outbreak

admin.site.register(UserProfileInfo)
admin.site.register(HospitalProfileInfo)
admin.site.register(PharmacyProfileInfo)
admin.site.register(Outbreak)