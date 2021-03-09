from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('upload/eur1/', views.upload_eur1, name="upload_eur1"),
    path('upload/atr/', views.upload_atr, name="upload_atr"),
    path('message/', views.message, name="message"),
    path('convert_in_word/', views.convert_in_word, name="convert_in_word"),
    path('convert_eur1_in_pdf/', views.convert_eur1_in_pdf, name="convert_eur1_in_pdf"),
    path('convert_atr_in_pdf/', views.convert_atr_in_pdf, name="convert_atr_in_pdf"),
    re_path(r'^$', RedirectView.as_view(url='upload/eur1/', permanent=False), name='index'),
]