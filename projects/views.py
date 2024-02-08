from django.shortcuts import render
from projects.models import Project, Resume

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)

def resume(request):
    resume = Resume.objects.all()
    context = {
        'resume': resume
    }
    return render(request, 'projects/resume.html', context)