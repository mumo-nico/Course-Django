from django.contrib import admin
from .models import Profile
# Register your models here.

#from django.contrib.auth.models import User
#user = User.objects.fiter(username='mumo').first()
#user.profile.image
admin.site.register(Profile)