from django.shortcuts import render
from apps.portfolio.models import Projects

# Create your views here.
def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render(request, 'index.html', {})


def projects(request):
    projects= Projects.objects.all()
    context={
        'projects':projects,
    }
    return render(request, 'projects.html', context)