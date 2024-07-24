# Berechnen die BLEU von generierter Text
from nltk.translate.bleu_score import sentence_bleu
import json
import LLMs_json_input.Openassistant_automatisch as generierterText_LLM

generierterTexte = generierterText_LLM.antwort

with open('E:\\BA\\Datenset\\dev_QA9.json') as f:
    data = json.load(f)
referenztext_list = [str(item['Answer']) for item in data]

bleu_sum = 0
n = 0
for referenztext in referenztext_list:
    referenz_wörte = referenztext.split()
    generierte_wörte = generierterTexte[n].split()
    bleu_note = sentence_bleu(referenz_wörte, generierte_wörte, weights=(0.25, 0.25, 0.25, 0.25))
    bleu_sum = bleu_sum + bleu_note
    print(bleu_note)
    print('nummer n Frage：', n)
    n += 1
bleu_avg = bleu_sum / n
print(bleu_avg)
