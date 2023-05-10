from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Image

def rules(request):
    return render(request, 'rules.html')

def about(request):
    return render(request, 'about.html')

class UploadView(CreateView):
    model = Image

class ImageView(DetailView):
    model = Image