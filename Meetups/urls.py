from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="all-meetups"),
    path('/<slug:my_slug>', views.index_detail, name="meetup-details")
]