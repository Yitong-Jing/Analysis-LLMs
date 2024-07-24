# Ausgabe bei LLM - tranierte Bloomz-1b1 Modell
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import time
import Kontexterstellung.anfrage_json_Eingabe as antext

a1 = time.time()

# Modell und Tokenizer laden
checkpoint = "bigscience/bloomz-1b1"
base_model = AutoModelForCausalLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# Tranierte Modell laden
model_id_lora = "E:/BA/Bloomz_lora/checkpoint-750"
model_peft = PeftModel.from_pretrained(base_model, model_id_lora)

# 10 Frage mit Kontext
text = antext.anfrage_kontext()

antwort = []
for kontext in text:
    inputs = tokenizer.encode(kontext, return_tensors="pt") #prompt
    outputs = model_peft.generate(inputs, min_length=50, max_new_tokens=100, do_sample=True)
    decode = tokenizer.decode(outputs[0])
    antwort.append(decode)
    print('eine Antwort:')
    print(decode)
print('Antwort List:')
print(antwort) #Verwenden den Tokenizer, um die generierten Ergebnisse zu dekodieren

a2 = time.time()
print(f'time cost is {a2 - a1} s')
