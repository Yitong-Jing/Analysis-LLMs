# Kombinieren die drei Validierungsdatensätze zu einem Validierungsdatensatz
import json

daten = []
# proofwriter Datensatz mit 1200 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/proofwriter_dev_1200.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
    for i in data:
        daten.append(i)

# 2WikiMultihopQA Datensatz mit 1200 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_dev_1200.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
    for i in data:
        daten.append(i)

# HotpotQA Datensatz mit 1200 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/hotpot_dev_1200.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
    for i in data:
        daten.append(i)

# Kombination zu einem Datensatz
json_file = open("E:/BA/Datenset/LLMs_training/neu/dev.json", mode='w', encoding='utf-8')
json.dump(daten, json_file)

