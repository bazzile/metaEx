# -*- coding: utf-8 -*-
import os
import re
import time
import zipfile
from datetime import datetime
from lxml import etree


def get(tag_name):
    for i in root.iter(tag_name):
        tag_name = i.text
        return tag_name

# Корневая директория
root_folder = r"Data"

img_list = []

counter = 0
start_time = time.time()

for root_dir, dirname, filenames in os.walk(root_folder):
    for filename in filenames:
        img = {}
        if re.match(r'\d{2}\D{3}.+P\d+\.XML', filename, re.IGNORECASE) is not None:  # DG
            counter += 1
            # print("Scanning", filename)

            xml = etree.parse(os.path.join(root_dir, filename))
            root = xml.getroot()
            img['satID'] = get("SATID")  # название спутника

            img['gsd'] = get("PRODUCTGSD")  # размер пиксела

            img['offNadir'] = get("MEANOFFNADIRVIEWANGLE")

            img['sunEl'] = get("MEANSUNEL")

            stringDATE = get("FIRSTLINETIME")
            img['date'] = datetime.strptime(stringDATE, '%Y-%m-%dT%H:%M:%S.%fZ')
            img_list.append(img)
            del img

print(img_list)
print "Отсканировано файлов: %i" % counter
elapsed_time = time.time() - start_time
