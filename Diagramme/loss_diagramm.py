# loss Diagramm für 1e-3 Learning Rate
import xlrd as xd
import matplotlib.pyplot as plt


data =xd.open_workbook ('E:\\BA\\train_ergebnis\\train_val_loss.xlsx')
sheet = data.sheet_by_name('750')  #Lesen Daten in Excel
d = []

#Spreichen die Daten in List
for r in range(sheet.nrows):
    data1 = []
    for c in range(sheet.ncols):
        data1.append(sheet.cell_value(r,c))
    d.append(list(data1))

steps = []
train_loss = []
dev_loss = []
for step in d:
    steps.append(step[0])
    train_loss.append(step[1])
    dev_loss.append(step[2])

train_loss_diagramm =plt.plot(steps, train_loss, 'b', label = u'train') #train_loss

dev_loss_diagramm = plt.plot(steps, dev_loss, 'r', label = u'validation') #dev_loss
plt.legend()
plt.xlabel(u'steps')
plt.ylabel(u'loss')
plt.title('Loss für Bloomz-1b1 Modell')
plt.show()