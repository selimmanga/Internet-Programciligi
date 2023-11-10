import sqlite3

# veriler.db isimli veri tabanı kur
baglanti = sqlite3.connect("veriler.db")

# tablo yaratma, silme ve diğer işlemler için cursor nesnesi oluştur
imlec = baglanti.cursor()

# sorgu = "CREATE TABLE IF NOT EXISTS kullanicilar (ad TEXT, email TEXT, sifre TEXT)"

# # sorguyu çalıştır
# imlec.execute(sorgu)
# baglanti.commit() # yapılan tüm işlemleri kaydet

# # tabloya veri kaydet
# sorgu = "INSERT INTO kullanicilar VALUES('Selim', 'mangaselim004@outlook.com', 'hardiez94')"
# imlec.execute(sorgu)
# baglanti.commit()

# Ürün tablomuzu oluşturalım
sorgu = """CREATE TABLE IF NOT EXISTS urunler (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                               kod TEXT, 
                                               ad TEXT,
                                               fiyat REAL)"""

imlec.execute(sorgu)
baglanti.commit()

# Rastgele kod üretmek için kullandık
import random
semboller = "0123456789abcdefghijklmnoprstABCDEFGHIJKLMNOPRST"
urunkodu = "".join(random.choices(semboller, k=5))

sorgu = f"INSERT INTO urunler (kod, ad, fiyat) VALUES ('{urunkodu}', 'Ekmek', 7.5)"
imlec.execute(sorgu)
baglanti.commit()

