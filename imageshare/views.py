from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.shortcuts import redirect
from .tasks import save_image_task
from django.urls import reverse
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

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
    
    async def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    async def put(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)
    
    async def delete(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    async def post(self, request):
        form = request.POST
        image = form['image']
        slug = ''.join(random.sample(string.ascii_lowercase, 6))
        save_image_task.delay(image, slug)
        return redirect(reverse('detail', args=(slug,)))

    async def form_invalid(self):
        return redirect(reverse('index'))