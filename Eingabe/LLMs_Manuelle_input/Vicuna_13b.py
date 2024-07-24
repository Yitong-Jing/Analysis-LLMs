# Ausgabe bei LLM - Vicuna-13b
from llama_cpp import Llama
import Kontexterstellung.anfrage_Nutzer as antext

def generate_text(model,message):
    prompt = f"[INST] {message.strip()} [/INST]"
    output = model(prompt)
    answer = output["choices"][0]["text"]
    return answer

# Tokenizer laden
model = Llama(model_path = "D:/LLM_Modelle/vicuna_13b/vicuna-13b-v1.5.Q2_K.gguf")

# Frage mit Kontext
text = antext.anfrage_kontext()

# Antwort generieren
print('Antwort:')
print(generate_text(model, text))
print("")

