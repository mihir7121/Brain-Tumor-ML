from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.landing, name='landing'),
    path("upload", views.upload, name='upload'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("result", views.result, name='result'),
    # path("index", views.index, name='index'),
    # path("rendervideo", views.rendervideo, name='rendervideo'),
    # path("takephoto", views.takephoto, name='takephoto'),
    # path("about", views.aboutus, name='aboutus')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   