from django.contrib import admin

# Register your models here.
from .models import Project, Skill, Role, Client, ViewCount, File, ContactRecord, ViewCount

@admin.register(ViewCount)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('project', 'ip', 'date')

@admin.register(ContactRecord)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent_date')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ('name', 'level', 'project')

@admin.register(Client)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')

@admin.register(Role)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')

@admin.register(File)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0

class RoleInline(admin.TabularInline):
    model = Role
    extra = 0

class ClientInline(admin.TabularInline):
    model = Client
    extra = 0

class FileInline(admin.TabularInline):
    model = File
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'demo_url', 'creation_date', 'num_view')
	fields = ['title', 'category', 'status', 'demo_url', 'creation_date',  'summary', 'description', 'team_size', 'cover_pic', 'num_view',]
	#The fields attribute lists just those fields that are to be displayed on the form, in order. Fields are displayed vertically by default, but will display horizontally if you further group them in a tuple (as shown in the "date" fields above).
	inlines = [SkillInline, RoleInline, ClientInline, FileInline]
	list_filter = ('status', 'category', 'skills', 'roles')

