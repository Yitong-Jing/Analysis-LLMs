# Speichern Attribut "questions" und "answer" in originalem 2WikiMultihopQA Datensatz in neuem 2WikiMultihopQA Datensatz
import json

# Lesen Daten
with open('E:\\BA\\Datenset\\2WikiMultihopQA\\train.json', encoding='utf-8') as f: # Trainingsdatensatz
# with open('E:\\BA\\Datenset\\2WikiMultihopQA\\dev.json', encoding='utf-8') as f: # Validierungsdatensatz
    n = 0
    lines = f.readline()
    text = json.loads(lines)
    daten = []
    # Extrahieren die Attribute "questions" und "answer" und dann spreichen in einem list
    for i in text:
        extracted_data = {"Question": i["question"], "Answer": i["answer"]}
        daten.append(extracted_data)

json_file = open('E:/BA/Datenset/LLMs_training/train/2WikiMultihopQA_train.json', mode='w', encoding='utf-8') # Trainingsdatensatz
# json_file = open('E:/BA/Datenset/LLMs_training/dev/2WikiMultihopQA_dev.json', mode='w', encoding='utf-8') # Validierungsdatensatz
json.dump(daten, json_file)
