from django.urls import path
from xmlinport.views import *
from loadfile import  *

urlpatterns = [
    path("list/", list, name="list"),
    path("xml/", list_xml, name="xml_list"),
    path('xml_load/',list_xml,name="load"),
]
