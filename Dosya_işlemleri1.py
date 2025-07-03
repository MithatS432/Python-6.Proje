import os

# 1. Dosya yolu tanımlama (göreli yol)
dosya_adi = "veri/dosya1.txt"

# Eğer klasör yoksa oluştur
os.makedirs(os.path.dirname(dosya_adi), exist_ok=True)

# 2. Yazma modunda dosya oluşturma (w: yazma, varsa üzerine yazar)
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba Mithat!\n")
    dosya.write("Bu dosya Python ile oluşturuldu.\n")

# 3. Ekleme modunda dosyaya yeni satır ekleme (a: append)
with open(dosya_adi, "a", encoding="utf-8") as dosya:
    dosya.write("Yeni bir satır daha eklendi.\n")

# 4. Okuma modunda dosyayı açma ve içerik yazdırma (r: read)
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("Dosya İçeriği:\n", icerik)

# 5. Okuma ve yazma bir arada (r+)
with open(dosya_adi, "r+", encoding="utf-8") as dosya:
    dosya.seek(0)
    ilk_satir = dosya.readline()
    print("İlk Satır:", ilk_satir.strip())
