from django.conf.urls import url, include
from .views import *
from django.conf import settings

app_name = 'notes'
urlpatterns = [
    url(r'^notes/$', NotesView.as_view(), name='note'),
    url(r'^delete/(?P<id>[0-9]+)/$', DeleteView.as_view(), name='delete'),
    url(r'^edit/(?P<id>[0-9]+)/$', EditView.as_view(), name='edit'),
]