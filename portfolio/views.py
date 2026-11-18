from django.shortcuts import render
from .models import Profile, Sckill, Project
from django.shortcuts import render, get_object_or_404

def home(request):
    profile = Profile.objects.first()
    skills = Sckill.objects.all()
    projects = Project.objects.filter(is_published=True)
    
    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
    }
    return render(request, "portfolio/home.html", context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project})