# Speichern Attribut "questions" und "answer" in originalem HotpotQA Datensatz in neuem HotpotQA Datensatz
import json

# Lesen Daten
with open('E:\\BA\\Datenset\\HotpotQA\\hotpot_train_v1.1.json', encoding='utf-8') as f: # Trainingsdatensatz
# with open('E:\\BA\\Datenset\\HotpotQA\\hotpot_dev_fullwiki_v1.json', encoding='utf-8') as f: # Validierungsdatensatz
    n = 0
    lines = f.readline()
    text = json.loads(lines)
    daten = []
    # Extrahieren die Attribute "questions" und "answer" und dann spreichen in einem list
    for i in text:
        extracted_data = {
            "Question": i["question"],
            "Answer": i["answer"]}
        daten.append(extracted_data)


json_file = open('E:/BA/Datenset/LLMs_training/train/hotpot_train.json', mode='w', encoding='utf-8') # Trainingsdatensatz
# json_file = open('E:/BA/Datenset/LLMs_training/dev/hotpot_dev.json', mode='w', encoding='utf-8') # Validierungsdatensatz
json.dump(daten, json_file)