# -*- coding: utf-8 -*-
import os
import re
import datetime
from xml.etree.ElementTree import ElementTree
import xlwt


def get(tag_name):
    for i in root.iter(tag_name):
        tag_name = i.text
        return tag_name


# Корневая директория
root_folder = os.path.join(os.getcwd(), '..', '..')

img_list = []

counter = 0
for root_dir, dirname, filenames in os.walk(root_folder):
    for filename in filenames:
        img = {}
        if re.match(r'\d{2}\D{3}.+P\d+\.XML', filename, re.IGNORECASE) is not None:  # DG
            counter += 1
            # print("Scanning", filename)

            xml = ElementTree(file=os.path.join(root_dir, filename))
            root = xml.getroot()

            img['PATH'] = str(os.path.abspath(os.path.join(root_dir, filename)))
            img['SOURCE'] = get("SATID")  # название спутника
            img['RESOLUT'] = round(float(get("PRODUCTGSD")), 1)  # размер пиксела
            img['ANGLE'] = round(float(get("MEANOFFNADIRVIEWANGLE")), 1)
            img['SUN_ELEV'] = round(float(get("MEANSUNEL")), 1)
            stringDATE = get("FIRSTLINETIME")
            DATE = datetime.datetime.strptime(stringDATE, '%Y-%m-%dT%H:%M:%S.%fZ')
            img['DATE'] = datetime.datetime.strftime(DATE, '%d.%m.%Y')
            img_list.append(img)
            del img

# Запись excel
col_names = ['PATH', 'SOURCE', 'RESOLUT', 'ANGLE', 'SUN_ELEV', 'DATE']
# col_names = [
#     'SOURCE', 'SPECTRUM', 'STEREO', 'DATE', 'PROCESS', 'CLOUD', 'SUN_ELEV', 'SUN_AZIM', 'ANGLE', 'RESOLUT',
#     'COORDIN', 'EXT_Xmin', 'EXT_Ymin', 'EXT_Xmax', 'EXT_Ymax', 'FILENAME', 'SPECTR_R', 'RADIOM_R', 'M_CONT_N',
#     'M_CONT_D', 'SOURCE_F', 'BRANCH', 'S_CONT_N', 'S_CONT_D'
# ]

book = xlwt.Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Каталог')
for i in range(len(col_names)):
    sheet1.write(0, i + 1, col_names[i], xlwt.easyxf(
        'font: bold true;'
    ))
    sheet1.col(i).width = 3000  # 360 * len(col_names[i])
for i in range(len(img_list)):
    # for col_index in sheet1.ncols:
    for col_name in range(len(col_names)):
        sheet1.write(i + 1, col_name + 1, img_list[i][col_names[col_name]])

book.save('Catalog.xls')

