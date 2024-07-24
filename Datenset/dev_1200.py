# Wählen für jeden Datensatz 1200 Daten als Validierungsdatensatz aus
import json
import random

# proofwriter Datensatz mit 1200 Einträge
with open("E:/BA/Datenset/LLMs_training/neu/proofwriter_dev.json", encoding='utf-8') as f:
# 2WikiMultihopQA Datensatz mit 1200 Einträge
# with open("E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_dev.json", encoding='utf-8') as f:
# HotpotQA Datensatz mit 1200 Einträge
# with open("E:/BA/Datenset/LLMs_training/neu/hotpot_dev.json", encoding='utf-8') as f:
    lines = f.readline()
    data = json.loads(lines)
print(len(data))

sampled_data = random.sample(data, 1200)
json_file = open("E:/BA/Datenset/LLMs_training/neu/proofwriter_dev_1200.json", mode='w', encoding='utf-8')
# json_file = open("E:/BA/Datenset/LLMs_training/neu/2WikiMultihopQA_dev_1200.json", mode='w', encoding='utf-8')
# json_file = open("E:/BA/Datenset/LLMs_training/neu/hotpot_dev_1200.json", mode='w', encoding='utf-8')
json.dump(sampled_data, json_file)
