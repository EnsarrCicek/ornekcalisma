import tkinter as tk
from tkinter import messagebox, ttk
import joblib

# Önceden eğitilmiş model ve vektörizeri yükleyin
model_path = r'C:\Users\muhas\OneDrive\Desktop\duyguanalizi\model.pkl'
clf = joblib.load(model_path)

vectorizer_path = r'C:\Users\muhas\OneDrive\Desktop\duyguanalizi\vectorizer.pkl'
vectorizer = joblib.load(vectorizer_path)

# Metni analiz eden fonksiyon
def analyze_sentiment():
    user_input = entry.get()  # Kullanıcının yazdığı metni al
    if not user_input:
        messagebox.showwarning("Uyarı", "Lütfen bir metin girin.")
        return

    # Girdiyi vektörleştir
    X_input = vectorizer.transform([user_input])
    
    # Modelden tahmin et
    sentiment = clf.predict(X_input)[0]
    
    # Sonucu göster
    if sentiment == 'positive':
        result_text = "Bu yazı **POZİTİF** olarak değerlendirildi!"
        result_label.config(fg="green")
    elif sentiment == 'negative':
        result_text = "Bu yazı **NEGATİF** olarak değerlendirildi!"
        result_label.config(fg="red")
    else:
        result_text = "Bu yazı **NÖTR** olarak değerlendirild!"
        result_label.config(fg="blue")
    
    result_label.config(text=result_text)

# Tkinter arayüzü oluşturma
window = tk.Tk()
window.title("Duygu Analizi")
window.geometry("400x300")  # Pencere boyutu
window.configure(bg="#f0f0f0")  # Arka plan rengi

# Başlık
title_label = tk.Label(window, text="Duygu Analizi", font=('Helvetica', 16, 'bold'), bg="#f0f0f0")
title_label.pack(pady=10)  # Yukarıdan boşluk

# Giriş kutusu
entry_label = tk.Label(window, text="Bir metin girin:", bg="#f0f0f0")
entry_label.pack(pady=5)

entry = tk.Entry(window, width=50, font=('Helvetica', 12), bd=2, relief="groove")
entry.pack(pady=5)

# Analiz butonu
analyze_button = tk.Button(window, text="Analiz Et", command=analyze_sentiment, 
                           bg="#4CAF50", fg="white", font=('Helvetica', 12, 'bold'), 
                           relief="raised", activebackground="#45a049")
analyze_button.pack(pady=15)

# Sonuçların gösterileceği alan
result_label = tk.Label(window, text="", font=('Helvetica', 12), bg="#f0f0f0")
result_label.pack(pady=5)

# Pencereyi çalıştırma
window.mainloop()
