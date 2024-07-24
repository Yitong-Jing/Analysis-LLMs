# Ausgabe bei LLM - Vicuna-13b
from llama_cpp import Llama
import time
import Kontexterstellung.anfrage_json_Eingabe as antext

a1 = time.time()
def generate_text(model,message):
    prompt = f"[INST] {message.strip()} [/INST]"
    output = model(prompt)
    answer = output["choices"][0]["text"]
    return answer

# Modell laden
model = Llama(model_path = "D:/LLM_Modelle/vicuna_13b/vicuna-13b-v1.5.Q2_K.gguf")

# 10 Frage mit Kontext
text = antext.anfrage_kontext()


antwort = []
for kontext in text:
    generate_Text = generate_text(model, kontext)
    print('\nAnswer:\n')
    print(generate_Text)
    antwort.append(generate_Text)
print('Antwort List:')
print(antwort)
print("")

a2 = time.time()
print(f'the time: {a2 - a1} s')