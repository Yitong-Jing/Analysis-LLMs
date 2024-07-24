from nltk.translate.bleu_score import sentence_bleu
import json
import LLMs_json_input.Openassistant_automatisch as generierterText_LLM

generierterTexte = generierterText_LLM.antwort
#generierterTexte = ['Answer the question briefly:What science fantasy young adult series, told in first person, has a set of companion books narrating the stories of enslaved worlds and alien species? The Hobbit series by J.R.R. Tolkien.</s>', 'Answer the question briefly:Charlie is not quiet. Dave is green. Fiona is quiet. Harry is not furry. If Fiona is smart then Fiona is white. All quiet people are furry. Cold people are green. White people are green. Furry people are cold. If someone is blue and white then they are smart.Fiona is quiet.</s>', 'Answer the question briefly:Who held the record for the longest service in the Australian Parliament for a woman, and was surpassed by  a former Australian politician who was the 29th Speaker of the House of Representatives? Lucy Maud Montgomery MP for New fortuna</s>']

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