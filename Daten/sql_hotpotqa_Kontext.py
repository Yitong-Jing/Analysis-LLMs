# Speichern Attribut "_id" and "setences" im Datensatz in Tabelle "hotpot_kontext"
import pymysql
import json
import os

# Erstellung der Tabelle "hotpot_kontext"
def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data) # Überprüfen, ob die Verbindung erfolgreich hergestellt wurde.
  cursor.execute("DROP TABLE IF EXISTS hotpot_kontext")
  sql = """CREATE TABLE hotpot_kontext (
       id CHAR(50) NOT NULL,
       context TEXT NOT NULL
       )"""
  cursor.execute(sql)

# Speichern Attribut "_id" and "setences" im Datensatz in Tabelle "hotpot_kontext"
def data_insert(db):
    sum_daten_number = 0
    folder_path = "E:\\BA\\Datenset\\HotpotQA\\"
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file = os.path.join(root, name)
            with open(file, encoding='utf-8') as f:
                print('loading: ', file)
                while True:
                    try:
                        lines = f.readline()
                        if not lines:
                            break
                        text = json.loads(lines)
                        daten_number = len(text)
                        print(daten_number)
                        for i in text:
                            id = i['_id']
                            daten = []
                            result = []
                            for j in range(len(i['context'])):
                                result.extend(i['context'][j][1])
                            context = ' '.join(result)
                            daten.append((id, context))
                            print(daten)
                            insert_re = "insert into hotpot_kontext(id, context) values (%s, %s)"
                            cursor = db.cursor()
                            cursor.executemany(insert_re, daten)
                            db.commit()
                    except Exception as e:
                        db.rollback()
                        print(str(e))
                        break

            #print('a daten : ', daten_number)
            #sum_daten_number = daten_number + sum_daten_number
            #print('sum: ', sum_daten_number)

# Datenbank initialisieren
if __name__ == "__main__":
  db = pymysql.connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='inferenz_daten')
  cursor = db.cursor()
  prem(db)
  data_insert(db)
  cursor.close()