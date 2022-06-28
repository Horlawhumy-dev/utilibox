from django.contrib import admin
from .models import ApplicantRecord

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_num', 'name', 'email', 'sex')

admin.site.register(ApplicantRecord,ApplicationAdmin)