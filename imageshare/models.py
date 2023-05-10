import string
import random

from pyuploadcare.dj.models import ImageField
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=True)
    image = ImageField(manual_crop="")

    def __repr__(self):
        return u'<Image slug={0} image={1}>'.format(self.slug, self.image)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=(self.slug,))