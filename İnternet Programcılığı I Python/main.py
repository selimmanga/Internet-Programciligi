# flask kütüphanesinden büyük F ile başlayak Flask sınıfını getir
from flask import Flask, render_template, request, redirect, session
import sqlite3

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

app.run(debug=True)