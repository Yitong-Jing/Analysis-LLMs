# Ausgabe bei LLM - Bloomz-1b1
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import Kontexterstellung.anfrage_json_Eingabe as antext

a1 = time.time()
# Bloomz - 1b1 Modell
checkpoint = "bigscience/bloomz-1b1"

# Tokenizer und Modell laden
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

# 10 Frage mit Kontext
text = antext.anfrage_kontext()

antwort = []
for kontext in text:
    print(kontext)
    inputs = tokenizer.encode(kontext, return_tensors="pt") #prompt
    outputs = model.generate(inputs, min_length=50, max_new_tokens=100, do_sample=True)
    decode = tokenizer.decode(outputs[0])
    antwort.append(decode)
    print('\n Answer:\n')
    print(decode)
print('Antwort List:')
print(antwort) #Verwenden den Tokenizer, um die generierten Ergebnisse zu dekodieren

a2 = time.time()
print(f'time cost is {a2 - a1} s')
