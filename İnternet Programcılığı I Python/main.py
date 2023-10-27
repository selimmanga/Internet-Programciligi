# flask kütüphanesinden büyük F ile başlayak Flask sınıfını getir
from flask import Flask, render_template

# flask nesnesi oluştur ve app isimli değişkende sakla
app = Flask(__name__)

# @app.route("/") # Anasayfa açıldığında olacaklar, "/" işareti varsa anasayfa anlamına gelir.
# def hello_world():
#     icerik = "<p>Hello, World!</p><br>"
#     icerik += '<a href="/selim">Selimin sayfasına gitmek için buraya tıklayın</a>'
#     return icerik

# @app.route("/selim") # Anasayfa açıldığında olacaklar, "/" işareti varsa anasayfa anlamına gelir.
# def selimin_sayfasi():
#     icerik = "<h1>Selimin sayfası</h1><br>"
#     icerik += '<a href="/">Anasayfaya gitmek için buraya tıklayın</a>'
#     return icerik


# render_template(): bulunduğu dizindeki html dosyalarını yüklemek için kullanılan bir fonksiyondur
@app.route("/") 
def hello_world():
    return render_template("index.html")

@app.route("/selim") 
def selimin_sayfasi():
    return render_template("selim.html")

app.run(debug=True)