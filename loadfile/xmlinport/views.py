import io
import json
import os
from django.conf import settings
from time import sleep
from py7zr import unpack_7zarchive
import shutil
import xmltodict
from django.shortcuts import render


from xmlload.load import update_products_xml
import pandas as pd


def list_xml(request):
    if request.method == "POST":

        # form = DocumentForm(request.POST, request.FILES)
        # if form.is_valid():

        # for file in request.FILES.getlist("docfile"):
        # if file.content_type == "text/xml":  # "text/xml":
            # filename = str(file)

            # newdoc = Document(docfile=file)
            # l = []
            # l = newdoc
            # newdoc.save()
            # print(newdoc)
            # print(file)
            # sleep(25)
            # global name
            # for doc in Document.objects.all():
            #     document = doc.docfile
            #     print(document)
            #     name = document
            #     doc.delete()
            # # sleep(20)
            # pathfile = str("")
            # print(pathfile)
            print("working")
            file_list = list()
            files = os.listdir(settings.FILES_PATH)
            shutil.register_unpack_format('7z', ['.7z'], unpack_7zarchive)
            for file in files:
                if file.endswith(".7z"):
                    print(file)

                    shutil.unpack_archive(f'{settings.FILES_PATH}/{file}', f'{settings.FILES_PATH}/')
                    os.remove(f'{settings.FILES_PATH}/{file}')

                # file_list.append(file)
            print(files)
            # data_folder = ""
            counter = 0
            try:
                files = os.listdir(f"{settings.FILES_PATH}/")
                for file in files:
                    with open(f"{settings.FILES_PATH}/{file}", "r", encoding="utf-16") as xml_file:
                        data_dict = xmltodict.parse(xml_file.read())
                        xml_file.close()

                        json_data = json.dumps(data_dict)

                        with open("media/xml/data.json", "w") as json_file:
                            json_file.write(json_data)
                            json_file.close()
                    file = open("media/xml/data.json", "r")
                    json_datafile = file.read()
                    file.close()
                    # os.remove(f"media/{pathfile}")
                    json_datafile = json.loads(json_datafile)
                    counter+=1
                    print(f"{counter}")
                    sleep(25)
                    update_products_xml(json_datafile)
            except Exception as ex:
                print(ex)
        # return HttpResponseRedirect(reverse("xml_list"))
# else:
#     form = DocumentForm()
    #
    return render(request, "xmlinport/list_xml.html")
