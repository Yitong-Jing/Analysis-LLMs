# Kombinieren die drei Trainingsdatensätze zu einem Trainingsdatensatz
import json

daten = []
# proofwriter Datensatz mit 10000 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/proofwriter_train_10000.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
    for i in data:
        daten.append(i)

# 2WikiMultihopQA Datensatz mit 10000 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_train_10000.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
    for i in data:
        daten.append(i)

# HotpotQA Datensatz mit 10000 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/hotpot_train_10000.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
    for i in data:
        daten.append(i)

# Kombination zu einem Datensatz
json_file = open("E:/BA/Datenset/LLMs_training/neu/train.json", mode='w', encoding='utf-8')
json.dump(daten, json_file)

