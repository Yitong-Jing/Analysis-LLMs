# Ausgabe bei LLM - ChatGLM-6b-int4
from transformers import AutoTokenizer, AutoModel
import time
import Kontexterstellung.anfrage_json_Eingabe as antext

a1 = time.time()
# Modell und Tokenizer laden
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).float()
model = model.eval()

# 10 Frage mit Kontext
text = antext.anfrage_kontext()

antwort = []
for kontext in text:
    print(kontext)
    response, history = model.chat(tokenizer, kontext, history=[])
    antwort.append(response)
    print('\nAnswer:\n')
    print(response)
print('Antwort List:')
print(antwort)

a2 = time.time()
print(f'the time cost: {a2 - a1} s')