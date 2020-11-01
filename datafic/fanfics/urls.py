from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^fandoms$', views.FandomListView.as_view(), name='fandoms'),
    url(r'^languages$', views.LanguageListView.as_view(), name='languages'),
    path(r'fandom/<int:pk>', views.FandomDetailView.as_view(), name='fandom-detail'),
    path(r'language/<int:pk>', views.LanguageDetailView.as_view(), name='language-detail'),
]
