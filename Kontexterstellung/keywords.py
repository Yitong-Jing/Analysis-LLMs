#Keywords mit Llama_cpp generieren
from llama_cpp import Llama
import re

def generate_text(model, message):
    prompt = f"[INST] {message.strip()} [/INST]"
    output = model(prompt)
    answer = output["choices"][0]["text"]
    return answer

#Normalisierte Schlüsselwörter
def keywords_process(keywords):
    keywords_list = keywords.split('\n')  # Enter weglassen
    del keywords_list[0]
    keywords_list = list(filter(None, keywords_list))
    keywords_list = [i for i in keywords_list if 'Keywords:' not in i]
    keywords_result = []
    for i in keywords_list:
        i = re.sub('[\d+.]', '', i)  # remove number
        i = i.replace("*", "")
        i = i.strip()  # remove_leer
        keywords_result.append(i)

    return keywords_result


def keywords_output(anfrage):
    # llama.cpp für Extrahierung von Schlüsselwörter
    model = Llama(model_path="C:/Users/11609/.conda/envs/llama2_jing/Lib/site-packages/pip/_internal/models/Lamada/7B/llama-2-7b-chat.Q4_0.gguf")
    text = anfrage
    tip = 'Extract only the keywords from the sentence below.'
    keywords = generate_text(model, tip + text)
    result = keywords_process(keywords)
    keywords_list = []
    for keyword in result:
        if keyword in text:
            keywords_list.append(keyword)

    print('Keywords: ', keywords_list)
    return keywords_list

#keywords_output()