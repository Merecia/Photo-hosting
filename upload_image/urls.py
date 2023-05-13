from django.urls import path, re_path, include

from imageshare import views
from imageshare.models import Image

urlpatterns = [
    re_path(
        r'^$', 
        views.UploadView.as_view(), 
        name='index'
    ),
    re_path(
        r'^view/(?P<pk>[a-z]{6})/$', 
        views.ImageView.as_view(), 
        name='detail'
    ),
    path("imageshare/", include('imageshare.urls'))
]