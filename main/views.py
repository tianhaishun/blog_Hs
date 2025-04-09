from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Education, Skill, WorkExperience, Project, Post, Comment
from .forms import PostForm, CommentForm

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

def about(request):
    profile = Profile.objects.first()
    return render(request, 'main/about.html', {'profile': profile})

def contact(request):
    profile = Profile.objects.first()
    return render(request, 'main/contact.html', {'profile': profile})

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

def post_list(request):
    posts = Post.objects.filter(status=True).order_by('-created_at')
    return render(request, 'main/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'main/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'main/post_form.html', {'form': form})

@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_form.html', {'form': form})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'main/post_confirm_delete.html', {'post': post})

@login_required
def comment_create(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'main/comment_form.html', {'form': form, 'post': post}) 