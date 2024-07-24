# Benutzereingab - trainierte Bloomz-1b1
from transformers import AutoModelForCausalLM, AutoTokenizer
#from peft import LoraConfig, get_peft_model
from peft import PeftModel
import Kontexterstellung.anfrage_Nutzer as antext

# Bloomz-1b1
checkpoint = "bigscience/bloomz-1b1"

# Tokenizer und Modell laden
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

# trainierte Bloomz-1b1
model_id_lora = "E:/BA/Bloomz_lora/checkpoint-750"
peft_model = PeftModel.from_pretrained(model, model_id_lora)

# Frage mit Kontext
text = antext.anfrage_kontext()
print(text)

# Antwort generieren
inputs = tokenizer.encode(text, return_tensors="pt") #prompt
outputs = peft_model.generate(inputs, min_length=50, max_new_tokens=100, do_sample=True)
decode = tokenizer.decode(outputs[0])
print('\nAnswer:\n')
print(decode)

