from xlwt import Workbook
import io

filename = r"85bbd3d0-3db6-4218-bd36-01ba0b5137fa.xls"

manila_file = io.open(filename, "r", encoding="utf-8")
data = manila_file.readlines()

xldoc = Workbook()
sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)

for i, row in enumerate(data):
    for j, val in enumerate(row.replace('\n', '').split('\t')):
        sheet.write(i, j, val)

xldoc.save('manila_converted.xls')

# import pandas as pd

# df = pd.ExcelFile('manila_converted.xls').parse('Sheet1')
