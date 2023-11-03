import sqlite3

# veriler.db isimli veri tabanı kur
baglanti = sqlite3.connect("veriler.db")

# tablo yaratma, silme ve diğer işlemler için cursor nesnesi oluştur
imlec = baglanti.cursor()
sorgu = "CREATE TABLE IF NOT EXISTS kullanicilar (ad TEXT, email TEXT, sifre TEXT)"

# sorguyu çalıştır
imlec.execute(sorgu)
baglanti.commit() # yapılan tüm işlemleri kaydet

# tabloya veri kaydet
sorgu = "INSERT INTO kullanicilar VALUES('Selim', 'ornek@hotmail.com', '1234')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "DELETE FROM kullanicilar WHERE ad ='Selim'"
imlec.execute(sorgu)
baglanti.commit()
