## Speichern Tabelle "proofwriter_kontext", "2wikiMultihop_kontext" und "hotpot_kontext" in Tabelle
import pymysql

# Erstellung der Tabelle "kontext"
def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data)
  cursor.execute("DROP TABLE IF EXISTS kontext")
  sql = """CREATE TABLE kontext (
       id CHAR(50) NOT NULL,
       Kontext TEXT NOT NULL
       )"""
  cursor.execute(sql)


# Verbinden Tabelle "proofwriter_kontext", "2wikiMultihop_kontext" und "hotpot_kontext"
def datenverbinden(db):
    verbinden_proofwriter_context = "insert into kontext(id, Kontext) select * from proofwriter_kontext"
    cursor.execute(verbinden_proofwriter_context)
    verbinden_wikimultihopqa = "insert into kontext(id, Kontext) select * from 2wikimultihop_kontext"
    cursor.execute(verbinden_wikimultihopqa)
    verbinden_wikimultihopqa = "insert into kontext(id, Kontext) select * from hotpot_kontext"
    cursor.execute(verbinden_wikimultihopqa)
    db.commit()
    print('fertig')

# Datenbank initialisieren
if __name__ == "__main__":
  db = pymysql.connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='inferenz_daten')
  cursor = db.cursor()
  prem(db)
  datenverbinden(db)
  cursor.close()
