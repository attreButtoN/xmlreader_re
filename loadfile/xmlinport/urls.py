from django.urls import path
from xmlinport.views import *


urlpatterns = [
    path("list/", list, name="list"),
    path("xml/", list_xml, name="xml_list"),
]
