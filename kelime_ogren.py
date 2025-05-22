import tkinter as tk  # kelime öğrenme uygulaması için tkinter kütüphanesini seçtim ve içe aktarıp
from PIL import Image, ImageTk  # görsel olarak arka plan resmi eklemek istediğim için PIL kütüphanesini içe aktardım
import random     # rastgele kelime seçimi için de random kütüphanesini de yazdım.

# Kelime listesi A1 seviyesindeki kelimeleri yazdım 
kelimeler = [
    {"tr": "anne", "eng": "mother", "fr": "la mère"},
    {"tr": "baba", "eng": "father", "fr": "le père"},
    {"tr": "kız evlat", "eng": "daughter", "fr": "la fille"},
    {"tr": "erkek evlat", "eng": "son", "fr": "le fils"},
    {"tr": "kedi", "eng": "cat", "fr": "la chat"},
    {"tr": "ev","eng":"home","fr": "le maison"},
    {"tr": "mavi","eng":"blue","fr":"le bleu(e)"},
    {"tr":"kütüphane","eng":"library","fr":"la bibliothèque"},
    {"tr":"hastane","eng":"hospital","fr": "l'hôpital"},
    {"tr":"okul","eng":"school","fr":"l'école"},
    {"tr": "öğrenci","eng": "student","fr": "l'étudiant"},
    {"tr":"öğretmen", "eng": "teacher", "fr": "le professeur"}
]

# Yeni kelime seçme  
def yeni_kelime():
    global secili_kelime
    secili_kelime = random.choice(kelimeler)  # Kelimeler listesinden rastgele bir kelime seçilir
    lbl_turkce.config(text=secili_kelime["tr"])  # Türkçe kelimeyi etiket üzerinde gösterir
    lbl_ingilizce.config(text="")  # İngilizce anlamını sıfırlar
    lbl_fransizca.config(text="")  # Fransızca anlamını sıfırlar

# Anlamını göster
def anlamini_goster():
    lbl_ingilizce.config(text="İngilizce: " + secili_kelime["eng"])  # İngilizce anlamı etiket üzerinde gösterir
    lbl_fransizca.config(text="Fransızca: " + secili_kelime["fr"])  # Fransızca anlamı etiket üzerinde gösterir

# Arayüz oluştur
pencere = tk.Tk()  # Tkinter penceresini başlatır
pencere.title("Kelime Öğren")  # Pencerenin başlığını ayarlar 
pencere.geometry("300x200")  # Pencerenin boyutunu ayarlar (300x200)  
# Arka plan resmi
arkaplan_img = Image.open("arka_plan.jpg")
arkaplan_img = arkaplan_img.resize((200, 100))
arkaplan = ImageTk.PhotoImage(arkaplan_img)
# Arka plan label
lbl_arkaplan = tk.Label(pencere, image=arkaplan)
lbl_arkaplan.place(x=0, y=0, relwidth=1, relheight=1)  # Arka planı pencereye yerleştirir

# Etiketler

lbl_turkce = tk.Label(pencere, text="", font=("Verdana", 18), fg= "darkblue")  # Türkçe kelimeyi gösterecek etiket
lbl_turkce.pack(pady=10)  # Etiketi pencereye ekler ve üstten 10px boşluk bırakır

frame_ingilizce = tk.Frame(pencere, highlightbackground="gray", highlightthickness=1,bd=0) # çerçevenin rengi, kalınlığı
frame_ingilizce.pack(pady=1)    # font renk gibi görsel özellikler buraya yazdım
lbl_ingilizce = tk.Label(frame_ingilizce, text="", font=("Helvetica", 12), fg="darkblue")  # İngilizce anlamı gösterecek etiket
lbl_ingilizce.pack()  # Etiketi pencereye ekler

frame_fransizca = tk.Frame(pencere, highlightbackground="gray", highlightthickness=1,bd=0)  #çerçeve rengi, kalınlığı
frame_fransizca.pack(pady=1)         
lbl_fransizca = tk.Label(frame_fransizca, text="", font=("Helvetica ", 12), fg="darkblue")  # Fransızca anlamı gösterecek etiket
lbl_fransizca.pack()  # Etiketi pencereye ekler


# Butonlar
btn_anlam = tk.Button(
    pencere,
    text="Anlamını Göster",
    command=anlamini_goster,
    bg="#D4A5A5",       # Arka plan rengi
    fg="white",         # Yazı rengi
    activebackground="#C48B8B",  # Tıklanınca arka plan rengi
    font=("Helvetica", 10, "bold"),
    relief="flat"
)
btn_anlam.pack(pady=3) # butonlar arasındaki boşluk yazdım 

btn_sonraki = tk.Button( 
    pencere,
    text="Sonraki Kelime",  # Sonraki kelimeyi gösterecek buton
    command=yeni_kelime,    # Yeni kelime seçme fonksiyonunu çağırır
    bg="#D4A5A5",           # Arka plan rengi
    fg="white",             # Yazı rengi
    activebackground="#C48B8B",   # Tıklanınca arka plan rengi
    font=("Helvetica", 10, "bold"),
    relief="flat",
    padx=3
)
btn_sonraki.pack(pady=3)  

# İlk kelimeyi göster
yeni_kelime()  # İlk kelimeyi rastgele seçer ve ekranı günceller



# Uygulamayı başlat

pencere.mainloop()  # Tkinter penceresini sürekli açık tutar ve olayları dinler
