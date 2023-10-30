from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
import ms_identity_web
from project import settings

ms_identity_web = settings.MS_IDENTITY_WEB


# Create your views here.

def index(request):
    return render(request, 'auth/status.html')

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')

@ms_identity_web.login_required
def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

@ms_identity_web.login_required
def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)


class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['shelter', 'name', 'description']
