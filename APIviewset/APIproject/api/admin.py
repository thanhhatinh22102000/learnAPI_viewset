from django.contrib import admin
from .models import Staff
# Register your models here.
class adminregister(admin.ModelAdmin):
    list_display = ('name','age','address','salary')
    def active(self,obj):
        return obj.is_active==1
    active.boolean = True
admin.site.register(Staff,adminregister)
