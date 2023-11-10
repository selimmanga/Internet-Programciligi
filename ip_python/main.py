# flask kütüphanesinden büyük F ile başlayak Flask sınıfını getir
from flask import Flask, render_template, request, redirect, session
import sqlite3
import random

# flask nesnesi oluştur ve app isimli değişkende sakla
app = Flask(__name__)
app.secret_key = "selim"

# render_template(): bulunduğu dizindeki html dosyalarını yüklemek için kullanılan bir fonksiyondur
@app.route("/") 
def anasayfa():

    if "ad" in session: 
        return render_template("index.html")
    else:
        return render_template("giris.html")

@app.route("/kayit") 
def kayit_sayfasi():
    return render_template("kayit.html")

@app.route("/cikis") 
def cikis():
    session["ad"] = None
    session["sifre"] = None
    return redirect("/giris")

@app.route("/giris") 
def giris_sayfasi():
    return render_template("giris.html")

@app.route("/bilgiler", methods=["POST"])
def kayit():
    isim = request.form["isim"]
    email = request.form["email"]
    sifre = request.form["sifre"]

    baglanti = sqlite3.connect("veriler.db")
    sorgu = f"SELECT * FROM kullanicilar WHERE ad = '{isim}'"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayitlar = imlec.fetchall() # fetchall(): tüm kayıtları getir
    baglanti.commit()
    baglanti.close()

    if len(kayitlar) == 0:
        sorgu = f"INSERT INTO kullanicilar VALUES('{isim}', '{email}', '{sifre}')"
        imlec.execute(sorgu)
        baglanti.commit()
        return render_template('index.html')
    else:
        return render_template('kayit.html', hata = "Bu kullanıcı zaten kayıtlı.")

@app.route("/girisbilgileri", methods=["POST"])
def giris_kontrol():
    isim = request.form["isim"]
    sifre = request.form["sifre"]

    baglanti = sqlite3.connect("veriler.db")
    sorgu = f"SELECT * FROM kullanicilar WHERE ad = '{isim}' AND sifre = '{sifre}'"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayitlar = imlec.fetchall() # fetchall(): tüm kayıtları getir

    if len(kayitlar) == 0:
        return render_template("giris.html", hata = "Kullanıcı bilgileri hatalı!")
    else:
        session["ad"] = isim
        session["sifre"] = sifre
        return redirect("/")

@app.route("/urunler")
def urunler():

    baglanti = sqlite3.connect("veriler.db")
        
    sorgu = "SELECT * FROM urunler"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayitlar = imlec.fetchall() # fetchall(): tüm kayıtları getir
    baglanti.commit()
    baglanti.close()
    return render_template("urunler.html", urunler=kayitlar)

@app.route("/urunler/sil/<urunid>")
def urun_sil(urunid):
    baglanti = sqlite3.connect("veriler.db")  
    sorgu = f"DELETE FROM urunler WHERE id={int(urunid)}"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    baglanti.commit()
    baglanti.close()
    return redirect("/urunler")

@app.route("/urunler/guncelle/<urunid>")
def urun_guncelle(urunid):
    baglanti = sqlite3.connect("veriler.db")
        
    sorgu = f"SELECT * FROM urunler WHERE id = {int(urunid)}"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayit = imlec.fetchone() # fetchone(): # tek bir kaydı çeker
    baglanti.close()
    return render_template("urun_guncelle.html", urun=kayit)

@app.route("/urunler/guncelle", methods=["POST"])
def urun_kaydet():
    id = request.form["id"]
    kod = request.form["kod"]
    ad = request.form["ad"]
    fiyat = request.form["fiyat"]

    baglanti = sqlite3.connect("veriler.db")
    sorgu = f"UPDATE urunler SET kod='{kod}', ad='{ad}', fiyat={float(fiyat)} WHERE id = {int(id)}"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayit = imlec.fetchone()
    baglanti.commit()
    baglanti.close()
    return redirect("/urunler")

@app.route("/urunler/urun_ekle", methods=["POST"])
def urun_ekle():
    
    ad = request.form["ad"]
    fiyat = request.form["fiyat"]

    baglanti = sqlite3.connect("veriler.db")
    imlec = baglanti.cursor()

    semboller = "0123456789abcdefghijklmnoprstABCDEFGHIJKLMNOPRST"
    urunkodu = "".join(random.choices(semboller, k=5))

    sorgu = f"INSERT INTO urunler (kod, ad, fiyat) VALUES ('{urunkodu}', '{ad}', {float(fiyat)})"
    imlec.execute(sorgu)
    baglanti.commit()
    baglanti.close()
    return redirect("/urunler")

app.run(debug=True)