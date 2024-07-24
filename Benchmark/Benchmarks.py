# BLEU, Perplexität, ROUGE und WMD zusammen
import json
import LLMs_json_input.Bloomz_lora as gen_Text_LLM
from nltk.translate.bleu_score import sentence_bleu #bleu
import evaluate #perplexity
from rouge import Rouge  #rouge
import gensim.downloader as api #WMD


# Funktion BLEU
def cal_bleu(generierterTexte, data):
    referenztext_list = [str(item['Answer']) for item in data]
    bleu_sum = 0
    n = 0
    for referenztext in referenztext_list:
        referenz_wörte = [referenztext.split()]
        generierte_wörte = generierterTexte[n].split()
        bleu_note = sentence_bleu(referenz_wörte, generierte_wörte, weights=(0.25, 0.25, 0.25, 0.25))
        bleu_sum = bleu_sum + bleu_note
        n += 1
    bleu_avg = bleu_sum / n
    print('bleu Note:', bleu_avg)
    return

# Funktion Perplexität
def cal_ppl(generierterTexte):
    generierterTexte = ['Unknown' if not item else item for item in generierterTexte]
    perplexity = evaluate.load("perplexity", module_type="metric")
    results = perplexity.compute(model_id='gpt2',
                                 add_start_token=True,
                                 predictions=generierterTexte)
    print('ppl Note:', round(results["mean_perplexity"], 7))

    return

# Funktion ROUGE
def cal_rouge(generierterTexte, data):
    referenztext = [str(item['Answer']) for item in data]
    generierterTexte = ['Unknown' if not item else item for item in generierterTexte]

    rouge = Rouge()
    score = rouge.get_scores(generierterTexte, referenztext, avg=True)

    print(score)
    return

# Funktion WMD
def cal_WMD(generierterTexte, data):
    model = api.load('word2vec-google-news-300')

    referenztext_list = [str(item['Answer']) for item in data]
    generierterTexte = ['Unknown' if not item else item for item in generierterTexte]

    wmd_sum = 0
    n = 0
    for referenztext in referenztext_list:
        wmd_note = round(model.wmdistance(generierterTexte[n], referenztext), 7)
        if wmd_note == float('inf'):
            wmd_note = 1
        #print('WMD Note:', wmd_note)
        wmd_sum = wmd_sum + wmd_note
        n += 1

    wmd_avg = wmd_sum / n
    print('WMD avg:', wmd_avg)
    return

# Load some sentences
generierterTexte = gen_Text_LLM.antwort
generierterTexte = generierterTexte[0:10]

with open('E:\\BA\\Datenset\\dev_QA.json') as f:
    data = json.load(f)

cal_bleu(generierterTexte, data)
cal_ppl(generierterTexte)
cal_rouge(generierterTexte, data)
cal_WMD(generierterTexte, data)
