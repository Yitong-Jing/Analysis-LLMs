# Berechnung rouge mit rouge
import json
from rouge import Rouge
import LLMs_json_input.Openassistant_automatisch as generierterText_LLM

# Load some sentences
generierterTexte = generierterText_LLM.antwort

with open('E:\\BA\\Datenset\\dev_QA9.json') as f:
    data = json.load(f)
referenztext = [str(item['Answer']) for item in data]

rouge = Rouge()
score = rouge.get_scores(generierterTexte, referenztext, avg=True)

print(score)
