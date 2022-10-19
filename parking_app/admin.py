from django.contrib import admin
from parking_app.models import Parkings, Users, Userpark
# Register your models here.
admin.site.register(Parkings)
admin.site.register(Users)
admin.site.register(Userpark)