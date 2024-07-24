# Wählen für jeden Datensatz 10.000 Daten als Trainingsdaten aus
import json
import random

with open("E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_train.json", encoding='utf-8') as f:
# with open("E:/BA/Datenset/LLMs_training/neu/hotpot_train.json", encoding='utf-8') as f:
# with open("E:/BA/Datenset/LLMs_training/neu/proofwriter_train.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
print(len(data))

sampled_data = random.sample(data, 10000)
json_file = open("E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_train_10000.json", mode='w', encoding='utf-8')
# json_file = open("E:/BA/Datenset/LLMs_training/neu/hotpot_train_10000.json", mode='w', encoding='utf-8')
# json_file = open("E:/BA/Datenset/LLMs_training/neu/proofwriter_train_10000.json", mode='w', encoding='utf-8')
json.dump(sampled_data, json_file)
