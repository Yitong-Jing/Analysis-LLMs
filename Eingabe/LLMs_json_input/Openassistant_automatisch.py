# Ausgabe bei LLM - Openassistant
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time
import Kontexterstellung.anfrage_json_Eingabe as antext

a1 = time.time()
# Modell und Tokenizer laden
tokenizer = AutoTokenizer.from_pretrained("D:/LLM_Modelle/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
model = AutoModelForCausalLM.from_pretrained("D:/LLM_Modelle/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", torch_dtype=torch.bfloat16)

# 10 Frage mit Kontext
text = antext.anfrage_kontext()


antwort = []
for kontext in text:
    inputs = tokenizer(kontext, return_tensors='pt').to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
    output_str = tokenizer.decode(outputs[0])
    print('\nAnswer:\n')
    print(output_str)
    antwort.append(output_str)
print('Antwort List:')
print(antwort)


a2 = time.time()
print(f'the time: {a2 - a1} s')