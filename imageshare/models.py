from pyuploadcare.dj.models import ImageField
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
import string
import random

def minimum_size(min_width=None, min_height=None):
    def validator(image):
        if not image.is_image:
           raise ValidationError('File should be image.')
        
        image_width = image.info['content_info']['image']['width']
        image_height = image.info['content_info']['image']['height']

        errors = []
        if min_width is not None and image_width < min_width:
           errors.append('Width should be > {} px.'.format(min_width))
        if min_height is not None and image_height < min_height:
           errors.append('Height should be > {} px.'.format(min_height))
        raise ValidationError(errors)
    
    return validator

class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=True)
    image = ImageField(manual_crop="", validators=[minimum_size(100, 100)])

    def __repr__(self):
        return u'<Image slug={0} image={1}>'.format(self.slug, self.image)

    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=(self.slug,))