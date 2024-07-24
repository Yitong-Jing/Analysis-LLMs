## Verbinden die Anfrage mit Kontext für Experiment
# Verbinden Anfrage und gefundte Kontext in Datenbank
import Kontexterstellung.Kontext_OR_AND as kt
import json

def anfrage_kontext():
    erstellte_Kontext = []
    with open("E:\\BA\\Datenset\\dev_QA.json", encoding='utf-8') as f: # Lesen die 10 Fragen
        lines = f.readline()
        text = json.loads(lines)
        for fra in text:
            frage = 'Question: \n' + fra['Question']
            print(frage)
            kontext = kt.db_info(frage)  # str
            if len(kontext) > 1200:
                kontext = kontext[:600]
                lang = '{:.0%}'.format(len(kontext)/1200)
                kontext = "\nContext  (%s): \n" % (lang) + kontext
            anfrage_kontext = frage + kontext  # str
            #anfrage_kontext = kontext
            erstellte_Kontext.append(anfrage_kontext) #10 Fragen verbinden mit qo Kontext
    print('erstellte Kontext: ')
    print(erstellte_Kontext)
    return erstellte_Kontext

#anfrage_kontext()
