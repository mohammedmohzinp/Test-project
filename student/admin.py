from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
        


class StudentMarksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = StudentMarks
        
admin.site.register(StudentMarks, StudentMarksAdmin)

admin.site.register(Department)

admin.site.register(Batch)


admin.site.register(Subjects)
admin.site.register(studentDetails)

