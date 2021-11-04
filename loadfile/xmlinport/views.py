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
    counter = 0
    if request.method == "POST":


            print("working")

            file_list = list()
            files = os.listdir("media/put_xml_here/")
            print(files)

            for folder in files:
                try:
                    files = os.listdir(f"media/put_xml_here/{folder}")
                    print(folder)
                    print(files)
                    for file in files:
                        print(f'media/put_xml_here/{folder}/{file}')
                        shutil.move(f'media/put_xml_here/{folder}/{file}', f'media/put_xml_here/')
                    os.rmdir(f"media/put_xml_here/{folder}")
                except:
                    pass
            files = os.listdir("media/put_xml_here/")
            try:
                shutil.register_unpack_format('7z', ['.7z'], unpack_7zarchive)
            except:
                pass
            for file in files:
                if file.endswith(".7z"):
                    print(file)

                    shutil.unpack_archive(f'media/put_xml_here/{file}', 'media/put_xml_here/')
                    os.remove(f'media/put_xml_here/{file}')

                # file_list.append(file)
            print(files)
            # data_folder = ""
            try:
                files = os.listdir("media/put_xml_here/")
                for file in files:
                    with open(f"media/put_xml_here/{file}", "r", encoding="utf-16") as xml_file:
                        data_dict = xmltodict.parse(xml_file.read())
                        xml_file.close()

                        json_data = json.dumps(data_dict)
                        os.remove(f"media/put_xml_here/{file}")
                        with open("media/xml/data.json", "w") as json_file:
                            json_file.write(json_data)
                            json_file.close()
                    file = open("media/xml/data.json", "r")
                    json_datafile = file.read()
                    file.close()

                    json_datafile = json.loads(json_datafile)
                    counter +=1
                    print(counter)
                    print("*_"*50)
                    sleep(5)
                    update_products_xml(json_datafile)
            except Exception as ex:
                print(ex)
        # return HttpResponseRedirect(reverse("xml_list"))
# else:
#     form = DocumentForm()
    #
    return render(request, "xmlinport/list_xml.html")
