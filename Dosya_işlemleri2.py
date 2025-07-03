import json
import csv
import os

# Klasör oluştur
os.makedirs("veri", exist_ok=True)

# ----------------
# JSON İşlemleri
# ----------------
ogrenci = {
    "ad": "Mithat",
    "yas": 24,
    "diller": ["Python", "C", "Flutter"],
    "aktif": True
}

# JSON dosyasına yazma
json_yolu = "veri/ogrenci.json"
with open(json_yolu, "w", encoding="utf-8") as jf:
    json.dump(ogrenci, jf, ensure_ascii=False, indent=4)

# JSON dosyasını okuma
with open(json_yolu, "r", encoding="utf-8") as jf:
    veri = json.load(jf)
    print("JSON'dan okunan veri:", veri)

# ----------------
# CSV İşlemleri
# ----------------
csv_yolu = "veri/notlar.csv"
basliklar = ["isim", "vize", "final"]
veriler = [
    ["Ali", 70, 85],
    ["Ayşe", 80, 90],
    ["Mehmet", 60, 75]
]

# CSV'ye yazma
with open(csv_yolu, "w", newline='', encoding="utf-8") as cf:
    writer = csv.writer(cf)
    writer.writerow(basliklar)
    writer.writerows(veriler)

# CSV'den okuma
with open(csv_yolu, "r", encoding="utf-8") as cf:
    reader = csv.reader(cf)
    for satir in reader:
        print("CSV Satırı:", satir)
