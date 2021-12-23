from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'data','valuta', 'descrizione', 'addebiti', 'accrediti', 'descrizioneestesa')