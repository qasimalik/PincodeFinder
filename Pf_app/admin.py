from django.contrib import admin
from .models import PinCode_Fetcher
from import_export.admin import ImportExportModelAdmin

#Extending the site 
@admin.register(PinCode_Fetcher)

#importing and exporting the file(raw dataset)
class ViewAdmin(ImportExportModelAdmin):
    pass