from django.contrib import admin
from import_export import resources
from  import_export.admin import ImportExportModelAdmin
from apps.user.models import UserApp

# Register your models here.

class UserResource(resources.ModelResource):
	class Meta:
		model = UserApp

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ("name", "last_name", "usuid", "rol")
	list_display = ("name", "last_name", "usuid", "rol")
	list_filter = ("usuid", "rol")
	resource_class = UserResource

admin.site.register(UserApp, UserAdmin)