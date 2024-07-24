# Löschen von doppelten Daten
import json

def vorverarbeitung_dataset(old_file, neu_file):
    daten = []
    with open(old_file, encoding='utf-8') as f:
        lines = f.readline()
        data = json.loads(lines)

    # bool zu str
    for i in data:
        if type(i['Answer']) == bool:
            i['Answer'] = str(i['Answer'])
        extracted_data = {
            "Question": i["Question"],
            "Answer": i["Answer"]}
        #print(type(i['Answer']))
        daten.append(extracted_data)

    # Entfernen doppelte Daten
    unique_data = set(tuple(d.items()) for d in daten)
    unique_data = [dict(t) for t in unique_data]

    #Spreichern
    json_file = open(neu_file, mode='w', encoding='utf-8')
    json.dump(unique_data, json_file)

#train_dataset = vorverarbeitung_dataset("E:/BA/Datenset/LLMs_training/train/hotpot_train.json", "E:/BA/Datenset/LLMs_training/neu/hotpot_train.json")
#train_dataset = vorverarbeitung_dataset("E:/BA/Datenset/LLMs_training/train/proofwriter_train.json", "E:/BA/Datenset/LLMs_training/neu/proofwriter_train.json")
#train_dataset = vorverarbeitung_dataset("E:/BA/Datenset/LLMs_training/train/2WikiMultihopQA_train.json", "E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_train.json")

dev_dataset = vorverarbeitung_dataset("E:\\BA\\Datenset\\LLMs_training\\dev\\hotpot_dev.json", "E:/BA/Datenset/LLMs_training/neu/hotpot_dev.json")
#dev_dataset = vorverarbeitung_dataset("E:\\BA\\Datenset\\LLMs_training\\dev\\proofwriter_dev.json", "E:/BA/Datenset/LLMs_training/neu/proofwriter_dev.json")
#dev_dataset = vorverarbeitung_dataset("E:\\BA\\Datenset\\LLMs_training\\dev\\2WikiMultihopQA_dev.json", "E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_dev.json")




