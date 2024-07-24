# Speichern Attribut "questions" und "answer" in originalem proofwriter Datensatz in neuem proofwriter Datensatz
import json
import os

n = 0
daten = []
# Ordner durchsuchen
folder_path = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\"
for root, dirs, files in os.walk(folder_path):
    for name in files:
        file = os.path.join(root, name)
        if file.endswith("train.jsonl"): # Trainingsdatensatz
        # if file.endswith("dev.jsonl"): # Validierungsdatensatz
            print("loading: ", file)
            with open(file, encoding='utf-8') as f:
                try:
                    while True:
                        lines = f.readline()
                        text = json.loads(lines)
                        # Extrahieren die Attribute "questions" und "answer" und dann spreichen in einem list
                        for i in text["questions"]:
                            extracted_data = {"Question": text['theory'] + text["questions"][i]["question"], "Answer": text["questions"][i]["answer"]}
                            daten.append(extracted_data)
                            n += 1
                            #print(u'Loading the % Data......' % n)
                            #print('Loading', extracted_data)
                except:
                    print('0')

json_file = open("E:/BA/Datenset/LLMs_training/train/proofwriter_train.json", mode='w', encoding='utf-8') # Trainingsdatensatz
# json_file = open('E:/BA/Datenset/LLMs_training/dev/proofwriter_dev.json', mode='w', encoding='utf-8') # Validierungsdatensatz
json.dump(daten, json_file)
