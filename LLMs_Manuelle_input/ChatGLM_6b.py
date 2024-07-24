# Benutzereingabe - ChatGLM-6b
from transformers import AutoTokenizer, AutoModel
import Kontexterstellung.anfrage_Nutzer as antext

# Change to int4
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).float()
model = model.eval()

# Frage mit Kontext
text = antext.anfrage_kontext()

# Antwort generieren
response, history = model.chat(tokenizer, text, history=[])
print('Antwort:')
print(response)
