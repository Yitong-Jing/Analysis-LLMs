# Speichern Attribut "_id" and "setences" im Datensatz in Tabelle "proofwriter_kontext"
import pymysql
import os
import json

# Erstellung der Tabelle "proofwriter_kontext"
def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data)
  cursor.execute("DROP TABLE IF EXISTS proofwriter_kontext")
  sql = """CREATE TABLE proofwriter_kontext (
       id CHAR(50) NOT NULL,
       context TEXT NOT NULL,
       PRIMARY KEY(id)
       )"""
  cursor.execute(sql)


# Speichern Attribut "_id" and "setences" im Datensatz in Tabelle "proofwriter_kontext"
def data_insert(db):
    sum_daten_number = 0
    folder_path = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\"
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file = os.path.join(root, name)
            with open(file, encoding='utf-8') as f:
                daten_number = 0
                while True:
                    try:
                        lines = f.readline()
                        if not lines:
                            break
                        text = json.loads(lines)
                        result = []
                        result.append((text['id'], text['theory']))
                        print(result)
                        daten_number += 1

                        insert_re = "insert into proofwriter_kontext(id, context) values (%s, %s)"
                        cursor = db.cursor()
                        cursor.executemany(insert_re, result)
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
