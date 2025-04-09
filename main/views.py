from django.shortcuts import render
from .models import Profile, Education, Skill, WorkExperience, Project

def home(request):
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('-end_date')
    skills = Skill.objects.all()
    work_experience = WorkExperience.objects.all().order_by('-start_date')
    projects = Project.objects.all().order_by('-start_date')
    
    context = {
        'profile': profile,
        'education': education,
        'skills': skills,
        'work_experience': work_experience,
        'projects': projects,
    }
    return render(request, 'main/home.html', context)

def education(request):
    education = Education.objects.all().order_by('-end_date')
    return render(request, 'main/education.html', {'education': education})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'main/skills.html', {'skills': skills})

def experience(request):
    work_experience = WorkExperience.objects.all().order_by('-start_date')
    return render(request, 'main/experience.html', {'work_experience': work_experience})

def projects(request):
    projects = Project.objects.all().order_by('-start_date')
    return render(request, 'main/projects.html', {'projects': projects}) 