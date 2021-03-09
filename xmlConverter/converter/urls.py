from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('upload/eur1/', views.upload, name="upload"),
    path('message/', views.message, name="message"),
    path('convert_in_word/', views.convert_in_word, name="convert_in_word"),
    path('convert_in_pdf/', views.convert_in_pdf, name="convert_in_pdf"),
    re_path(r'^$', RedirectView.as_view(url='upload/eur1/', permanent=False), name='index'),
]