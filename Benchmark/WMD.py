import gensim.downloader as api
import json
import LLMs_json_input.Openassistant_automatisch as generierterText_LLM

model = api.load('word2vec-google-news-300')

with open('E:\\BA\\Datenset\\test\\dev.json') as f:
    data = json.load(f)
referenztext_list = [str(item['Answer']) for item in data]
generierterTexte = generierterText_LLM.antwort

wmd_sum = 0
n = 0
for referenztext in referenztext_list:
    wmd_note = round(model.wmdistance(generierterTexte[n], referenztext), 2)
    print(wmd_note)
    wmd_sum = wmd_sum + wmd_note
    n += 1

print('wmdsum', wmd_sum)
print('n = ', n)
wmd_avg = wmd_sum / n
print(wmd_avg)
