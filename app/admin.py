from django.contrib import admin
from .models import Vote, Category,Student, Branche
from django.contrib.auth.models import Group

class CatAdmin(admin.ModelAdmin):
    list_display = ['category_name','active']
    list_filter = ['category_name','active']
    search_fields = ['category_name','active']
    list_editable = ['active']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll_no','branch','category','active']
    list_filter = ['name','roll_no','branch','category']
    search_fields = ['name','roll_no','branch','category']
    list_editable = ['active']

class VotestAdmin(admin.ModelAdmin):
    list_display = ['user','name','roll_no','branch','category']
    list_filter = ['name','roll_no','branch','category']
    search_fields = ['name','roll_no','branch','category']

admin.site.register(Student, StudentAdmin)
admin.site.register(Branche)
admin.site.register(Vote)
admin.site.register(Category,CatAdmin)
admin.site.unregister(Group)