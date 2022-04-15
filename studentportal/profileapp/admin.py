from codecs import register
from sqlite3 import register_adapter
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(profileInfo)
admin.site.register(result)
admin.site.register(cgpa)
admin.site.register(paymentdesc)
admin.site.register(sgpadashboard)
