# Lesen die Daten
import xlrd as xd

data =xd.open_workbook ('E:\\BA\\ergebnis.xlsx')
sheet = data.sheet_by_name('Sheet1')  #lese Daten in Excel
d = []
for r in range(sheet.nrows):
    data1 = []
    for c in range(sheet.ncols):
        data1.append(sheet.cell_value(r,c))
    d.append(list(data1))

print(d)

