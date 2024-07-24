# Diagramm für Vergleichung Bloomz-1b1 und tranierte Bloomz-1b1
import xlrd as xd
import matplotlib.pyplot as plt


data =xd.open_workbook ('E:\\BA\\ergebnis.xlsx')
sheet = data.sheet_by_name('Vergleich')  # Lesen die Daten
d = []
for r in range(sheet.nrows): # Konvertieren die Daten in einer Tabelle in eine Liste
    data1 = []
    for c in range(sheet.ncols):
        data1.append(sheet.cell_value(r,c))
    d.append(list(data1))

kontext = []
bleu_base_model = []
rouge1_base_model = []
rouge2_base_model = []
rougel_base_model = []
ppl_base_model = []
wmd_base_model = []

bleu_lora_model = []
rouge1_lora_model = []
rouge2_lora_model = []
rougel_lora_model = []
ppl_lora_model = []
wmd_lora_model = []
for metrik in d:
    kontext.append(metrik[0])
    bleu_base_model.append(metrik[1])
    ppl_base_model.append(metrik[2])
    rouge1_base_model.append(metrik[3])
    rouge2_base_model.append(metrik[4])
    rougel_base_model.append(metrik[5])
    wmd_base_model.append(metrik[6])

    bleu_lora_model.append(metrik[7])
    ppl_lora_model.append(metrik[8])
    rouge1_lora_model.append(metrik[9])
    rouge2_lora_model.append(metrik[10])
    rougel_lora_model.append(metrik[11])
    wmd_lora_model.append(metrik[12])

#bleu_base_diagramm =plt.plot(kontext, bleu_base_model, 'b', label = u'Bloomz-1b1')
#rouge1_base_diagramm = plt.plot(kontext, rouge1_base_model, 'b', label = u'Bloomz-1b1')
#rouge2_base_diagramm = plt.plot(kontext, rouge2_base_model, 'b', label = u'Bloomz-1b1')
#rougel_base_diagramm = plt.plot(kontext, rougel_base_model, 'b', label = u'Bloomz-1b1')
#ppl_base_diagramm = plt.plot(kontext, ppl_base_model, 'b', label = u'Bloomz-1b1')
wmd_base_diagramm = plt.plot(kontext, wmd_base_model, 'b', label = u'Bloomz-1b1')

#bleu_lora_diagramm =plt.plot(kontext, bleu_lora_model, 'r', label = u'getrainiertes Bloomz-1b1')
#rouge1_lora_diagramm = plt.plot(kontext, rouge1_lora_model, 'r', label = u'getrainiertes Bloomz-1b1')
#rouge2_lora_diagramm = plt.plot(kontext, rouge2_lora_model, 'r', label = u'getrainiertes Bloomz-1b1')
#rougel_lora_diagramm = plt.plot(kontext, rougel_lora_model, 'r', label = u'getrainiertes Bloomz-1b1')
#ppl_lora_diagramm = plt.plot(kontext, ppl_lora_model, 'r', label = u'getrainiertes Bloomz-1b1')
wmd_lora_diagramm = plt.plot(kontext, wmd_lora_model, 'r', label = u'getrainiertes Bloomz-1b1')
plt.legend()
plt.xlabel(u'Kontext')
#plt.ylabel(u'loss')
plt.title('WMD')
plt.show()