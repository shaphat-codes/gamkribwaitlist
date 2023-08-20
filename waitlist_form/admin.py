from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *
# Register your models here.


class WaitlistFormAdmin(ImportExportModelAdmin):
     resource_class = WaitlistResource   

admin.site.register(WaitlistForm, WaitlistFormAdmin)   