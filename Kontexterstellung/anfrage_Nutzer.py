## Verbinden die Anfrage mit Kontext für Benuzer
# Verbinden Anfrage und gefundte Kontext in Datenbank
import Kontexterstellung.Kontext_OR_AND as kt

def anfrage_kontext():
    anfrage = input('Bitte schreiben Sie die Anfrage: ')
    anfrage = 'Question: ' + anfrage
    kontext = kt.db_info(anfrage) #Ergestellte Anfrage und Kontext
    # Begrenzung der Kontextlänge, max. 1200 Zeichen
    if len(kontext) > 1200:
        kontext = kontext[:1200]
    kontext = '\ncontext: ' + kontext
    anfrage_kontext = anfrage + kontext #Ergestellte Anfrage und Kontext
    #print('Erstellte Kontext: ')
    print(anfrage_kontext)
    return anfrage_kontext

#anfrage_kontext()
