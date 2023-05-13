from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .tasks import save_image_task
from django.urls import reverse
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
import string
import random
import asyncio
from .models import Image

def rules(request):
    return render(request, 'rules.html')

def about(request):
    return render(request, 'about.html')

class ImageView(DetailView):
    model = Image

class UploadView(CreateView):
    model = Image
    fields = ['image']
    
    def form_valid(self, form):
        image = form.cleaned_data['image']
        slug = ''.join(random.sample(string.ascii_lowercase, 6))
        save_image_task.delay(image, slug)
        return redirect(reverse('detail', args=(slug,)))

    def form_invalid(self, form):
        return redirect(reverse('index'))