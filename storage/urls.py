from django.urls import path

from storage.views import index, workshop

urlpatterns = [
    path('', index, name='home'),
    path('workshop', workshop, name='workshop')
]
