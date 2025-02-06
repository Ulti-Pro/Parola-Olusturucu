import random

# 1. Adım: Karakter kümesi
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# 2. Adım: Kullanıcıdan parola uzunluğunu alma
parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))

# 3. Adım: Parola için boş bir değişken oluşturma
parola = ""

# 4. Adım: Döngü ile rastgele karakter seçip parolayı oluşturma
for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)

# 5. Adım: Sonucu yazdırma
print("Oluşturulan parola: ", parola)
