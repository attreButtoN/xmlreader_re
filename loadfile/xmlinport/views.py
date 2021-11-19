import io
import json
import os
from django.conf import settings
from time import sleep
from py7zr import unpack_7zarchive
import shutil
import xmltodict
from django.shortcuts import render
from datetime import datetime
from xmlload.load import update_products_xml
import pandas as pd


counter = 0
def list_xml(request):

    if request.method == "POST":


            print("working")

            file_list = list()
            files = os.listdir("media/put_xml_here/")
            print(files)
            file = open("file_view_log.txt", "a")
            file.write(f"Обработка папок,распаковывание архивов...   {datetime.now()}\n")
            file.close()
            print(f"Обработка папок,распаковывание архивов...   {datetime.now()}",flush=True)
            for folder in files:
                try:
                    files = os.listdir(f"media/put_xml_here/{folder}")
                    # print(folder)
                    # print(files)
                    for file in files:
                        # print(f'media/put_xml_here/{folder}/{file}')
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

            files = os.listdir("media/put_xml_here/")
            for file in files:
                try:
                    with open(f"media/put_xml_here/{file}", "r", encoding="utf-16-le") as xml_file:
                        data_dict = xmltodict.parse(xml_file.read())
                        xml_file.close()
                        name = file
                        json_data = json.dumps(data_dict)
                        os.remove(f"media/put_xml_here/{file}")
                        with open("media/xml/data.json", "w") as json_file:
                            json_file.write(json_data)
                            json_file.close()
                    file = open("media/xml/data.json", "r")
                    json_datafile = file.read()
                    file.close()

                    json_datafile = json.loads(json_datafile)
                    global counter
                    counter +=1
                    file = open("file_view_log.txt", "a")
                    file.write(f"В процессе: Файл №{counter},Имя:{name},Файлов осталось {len(files)-counter}    {datetime.now()} \n")
                    file.close()
                    print(f"В процессе: Файл №{counter},Имя:{name},Файлов осталось {len(files)-counter} {datetime.now()}", flush=True)
                    update_products_xml(json_datafile)

                except Exception as ex:
                    file = open("file_view_log.txt", "a")
                    file.write(f"Ошибка: {ex},Имя:{name}    {datetime.now()} \n")

                    file.close()
                    print(f"Ошибка: {ex},Имя:{name}    {datetime.now()}",flush=True)
                    print(f"Ошибка: {ex},Имя:{name}    {datetime.now()}",flush=True)

        # return HttpResponseRedirect(reverse("xml_list"))
# else:
#     form = DocumentForm()
    #
    return render(request, "xmlinport/list_xml.html")

