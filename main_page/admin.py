from django.contrib import admin
from .models import Feedback
from .models import update_log
from .models import Crona_data
from import_export.admin import ImportExportModelAdmin


# Register your models here.

admin.site.register(Feedback)
admin.site.register(update_log)

@admin.register(Crona_data)
class ViewAdmin(ImportExportModelAdmin):
    pass

