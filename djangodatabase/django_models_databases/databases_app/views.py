from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    musician_data = models.Musician.objects.all()
    musician_context = {"musicians": musician_data}
    return render(request, 'databases_app/index.html', context=musician_context)
