from django.urls import include, re_path

from imageshare import views
from imageshare.models import Image

urlpatterns = [
    re_path(
        r'^$', 
        views.UploadView.as_view(fields='__all__'), 
        name='index'
    ),
    re_path(
        r'^view/(?P<pk>[a-z]{6})/$', 
        views.ImageView.as_view(), 
        name='detail'
    ),
]