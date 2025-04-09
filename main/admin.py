from django.contrib import admin
from .models import Profile, Education, Skill, WorkExperience, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status')
    search_fields = ('name', 'email')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'department', 'start_date', 'end_date')
    list_filter = ('school', 'degree')
    search_fields = ('school', 'degree', 'department')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'department', 'start_date', 'end_date', 'current')
    list_filter = ('company', 'current')
    search_fields = ('company', 'position', 'department')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'role', 'start_date', 'end_date', 'current')
    list_filter = ('company', 'current')
    search_fields = ('title', 'company', 'role', 'description') 