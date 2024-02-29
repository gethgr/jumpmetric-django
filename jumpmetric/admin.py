from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from jumpmetric.models import Trial
from jumpmetric.models import Instructor
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class TrialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class InstructorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class InstructorInline(admin.StackedInline):
    model = Instructor
    can_delete = False
    verbose_name_plural = 'Instructors'

class CustomizedUserAdmin (UserAdmin):
    inlines = (InstructorInline, )


admin.site.register(Trial, TrialAdmin)
admin.site.register(Instructor, TrialAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
