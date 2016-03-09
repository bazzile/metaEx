# -*- coding: utf-8 -*-
import xlrd
from xlwt import Workbook, easyxf

col_names = [
    'SOURCE', 'SPECTRUM', 'STEREO', 'DATE', 'PROCESS', 'CLOUD', 'SUN_ELEV', 'SUN_AZIM', 'ANGLE', 'RESOLUT',
    'COORDIN', 'EXT_Xmin', 'EXT_Ymin', 'EXT_Xmax', 'EXT_Ymax', 'FILENAME', 'SPECTR_R', 'RADIOM_R', 'M_CONT_N',
    'M_CONT_D', 'SOURCE_F', 'BRANCH', 'S_CONT_N', 'S_CONT_D'
]

book = Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Каталог')
for i in range(len(col_names)):
    sheet1.write(0, i + 1, col_names[i], easyxf(
        'font: bold true;'
    ))
    sheet1.col(i).width = 3000 # 360 * len(col_names[i])

# sheet1.write(0, 0, 'A1')
# sheet1.write(0, 1, 'B1')
# row1 = sheet1.row(1)
# row1.write(0, 'A2')
# row1.write(1, 'B2')
# sheet1.col(0).width = 10000
# sheet2 = book.get_sheet(1)
# sheet2.row(0).write(0, 'Sheet 2 A1')
# sheet2.row(0).write(1, 'Sheet 2 B1')
# sheet2.flush_row_data()
# sheet2.write(1, 0, 'Sheet 2 A3')
# sheet2.col(0).width = 5000
# sheet2.col(0).hidden = True
book.save('Catalog.xls')
