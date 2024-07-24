#save
import json
import os

daten = []
'''
with open('E:\\BA\\Datenset\\HotpotQA\\hotpot_dev_fullwiki_v1.json', encoding='utf-8') as f:
    n = 0
    lines = f.readline()
    text = json.loads(lines)
    for i in text:
        extracted_data = {
            "Question": i["question"],
            "Answer": i["answer"]}
        daten.append(extracted_data)


with open('E:\\BA\\Datenset\\2WikiMultihopQA\\dev.json', encoding='utf-8') as f:
    n = 0
    lines = f.readline()
    text = json.loads(lines)
    for i in text:
        extracted_data = {
            "Question": i["question"],
            "Answer": i["answer"]}
        daten.append(extracted_data)
'''

folder_path = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\"
for root, dirs, files in os.walk(folder_path):
    for name in files:
        file = os.path.join(root, name)
        if file.endswith("dev.jsonl"):
            print("loading: ", file)
            with open(file, encoding='utf-8') as f:
                try:
                    while True:
                        lines = f.readline()
                        text = json.loads(lines)

                        for i in text["questions"]:
                            extracted_data = {"Question": text['theory'] + text["questions"][i]["question"], "Answer": text["questions"][i]["answer"]}
                            daten.append(extracted_data)
                            print('正在载入', extracted_data)
                except:
                    print('0')
# json_file = open('E:\\BA\\Datenset\\LLMs_training\\dev\\proofwriter_dev.json', mode='w', encoding='utf-8')
# json_file = open('E:\\BA\\Datenset\\LLMs_training\\dev\\proofwriter_dev.json', mode='w', encoding='utf-8')
json_file = open('E:\\BA\\Datenset\\LLMs_training\\dev\\proofwriter_dev.json', mode='w', encoding='utf-8')
json.dump(daten, json_file)
