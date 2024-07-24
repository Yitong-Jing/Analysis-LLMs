# loss Diagramm für verschiedene Learning Rate
import json
import matplotlib.pyplot as plt

#Lesen Daten in Logdatei
with open('E:\\BA\\Bloomz_lora\\loss_4\\1e-3\\checkpoint-750-20240713T102906Z-001\\checkpoint-750\\trainer_state.json', encoding='utf-8') as f:
    text = json.load(f)

#Spreichen die Daten in List
step_list = []
loss_list = []
for i in text['log_history']:
    step = i['step']
    loss = i['loss']
    step_list.append(step)
    loss_list.append(loss)

train_loss_diagramm =plt.plot(step_list, loss_list)

#plt.legend()
plt.xlabel(u'steps')
plt.ylabel(u'loss')
plt.title('Training-Loss für Bloomz-1b1 Modell (Lr: 1e-3)')
plt.show()


