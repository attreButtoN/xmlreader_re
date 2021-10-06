import io
import json
from datetime import datetime, date, timedelta
from time import sleep

import xmltodict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from xmlinport.models import *
from xmlinport.forms import *

from xmlload.load import update_products_xml
import pandas as pd


def list_xml(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            for file in request.FILES.getlist("docfile"):
                if file.content_type == "text/xml":  # "text/xml":
                    filename = str(file)

                    newdoc = Document(docfile=file)
                    l = []
                    l = newdoc
                    newdoc.save()
                    print(newdoc)
                    print(file)
                    # sleep(25)
                    global name
                    for doc in Document.objects.all():
                        document = doc.docfile
                        print(document)
                        name = document
                        doc.delete()
                    # sleep(20)
                    pathfile = str(name)
                    with open(f"media/{pathfile}", "r", encoding="utf-16") as xml_file:
                        data_dict = xmltodict.parse(xml_file.read())
                        xml_file.close()
                        json_data = json.dumps(data_dict)

                        with open("media/xml/data.json", "w") as json_file:
                            json_file.write(json_data)
                            json_file.close()
                    file = open("media/xml/data.json", "r")
                    json_datafile = file.read()
                    file.close()

                    json_datafile = json.loads(json_datafile)

                    # print(json_datafile["TradePlaceList"][0][0])
                    # tradeplacelist = json_datafile["TradePlaceList"]["TradePlace"][0]
                    # print(tradeplacelist)
                    update_products_xml(json_datafile)
                    # print(json_datafile)

            return HttpResponseRedirect(reverse("xml_list"))
    else:
        form = DocumentForm()

    return render(request, "xmlinport/list_xml.html", {"form": form})
