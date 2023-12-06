import sqlite3

conn = sqlite3.connect("sludinajumi.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE sludinajumi (
  id INTEGER PRIMARY KEY,
  kategorija TEXT,
  marka TEXT,
  modelis TEXT,
  izlaiduma_gads TEXT,
  motors TEXT,
  motora_tilpums TEXT,
  ātrumkārba TEXT,
  nobraukums TEXT,
  krāsa TEXT,
  virsbūves_tips TEXT,
  tehniskā_apskate TEXT,
  cena TEXT,
  īpašuma_veids TEXT,
  pilsēta TEXT,
  platība TEXT,
  iela TEXT
);
""")


def attelot_sludinajumus():
  cursor.execute("SELECT * FROM sludinajumi")
  sludinajumi = cursor.fetchall()
  for sludinajums in sludinajumi:
    print(sludinajums)

def izveidot_sludinajumu():
  kategorija = input("Izvēlieties kategoriju: ")
  if kategorija == "Automašīna":
    marka = input("Marka: ")
    modelis = input("Modelis: ")
    izlaiduma_gads = input("Izlaiduma gads: ")
    motors = input("Motors: ")
    motora_tilpums = input("Motora tilpums: ")
    ātrumkārba = input("Ātrumkārba: ")
    nobraukums = input("Nobraukums: ")
    krāsa = input("Krāsa: ")
    virsbūves_tips = input("Virsbūves tips: ")
    tehniskā_apskate = input("Tehniskā apskate: ")
    cena = input("Cena: ")
    cursor.execute("""
      INSERT INTO sludinajumi (
        kategorija,
        marka,
        modelis,
        izlaiduma_gads,
        motors,
        motora_tilpums,
        ātrumkārba,
        nobraukums,
        krāsa,
        virsbūves_tips,
        tehniskā_apskate,
        cena
      ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
      );
    """, (kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, ātrumkārba, nobraukums, krāsa, virsbūves_tips, tehniskā_apskate, cena))
    conn.commit()
  elif kategorija == "Privātais īpašums":
    īpašuma_veids = input("Īpašuma veids: ")
    pilsēta = input("Pilsēta: ")
    rajons = input("Rajons: ")
    platība = input("Platība: ")
    iela = input("Iela: ")
    cena = input("Cena: ")
    cursor.execute("""
      INSERT INTO sludinajumi (
        kategorija,
        īpašuma_veids,
        pilsēta,
        rajons,
        platība,
        iela,
        cena
      ) VALUES (
        ?, ?, ?, ?, ?, ?, ?
      );
    """, (kategorija, īpašuma_veids, pilsēta, rajons, platība, iela, cena))

def parbaudit_laucinus():
  kategorija = input("Izvēlieties kategoriju: ")
  if kategorija == "Automašīna":
    marka = input("Marka: ")
    modelis = input("Modelis: ")
    izlaiduma_gads = input("Izlaiduma gads: ")
    motors = input("Motors: ")
    motora_tilpums = input("Motora tilpums: ")
    ātrumkārba = input("Ātrumkārba: ")
    nobraukums = input("Nobraukums: ")
    krāsa = input("Krāsa: ")
    virsbūves_tips = input("Virsbūves tips: ")
    tehniskā_apskate = input("Tehniskā apskate: ")
    cena = input("Cena: ")
    if marka == "" or modelis == "" or izlaiduma_gads == "" or motora_tilpums == "" or nobraukums == "" or krāsa == "" or virsbūves_tips == "" or tehniskā_apskate == "" or cena == "":
      return False
    else:
      return True
  elif kategorija == "Privātais īpašums":
    īpašuma_veids = input("Īpašuma veids: ")
    pilsēta = input("Pilsēta: ")
    rajons = input("Rajons: ")
    platība = input("Platība: ")
    iela = input("Iela: ")
    cena = input("Cena: ")
    if īpašuma_veids == "" or pilsēta == "" or rajons == "" or platība == "" or cena == "":
      return False
    else:
      return True

def main():
  attelot_sludinajumus()
  while True:
    izvēlne = input("Izvēlieties darbību: ")
    if izvēlne == "1":
      if parbaudit_laucinus():
        izveidot_sludinajumu()
      else:
        print("Ne visi lauciņi ir aizpildīti!")
    elif izvēlne == "2":
      break
    else:
      print("Nepareiza darbība!")

if __name__ == "__main__":
  main()
