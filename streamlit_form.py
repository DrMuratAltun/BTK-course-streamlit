import streamlit as st
import pandas as pd
import re
from datetime   import datetime
st.title("Streamlit Form 💔")
isim = st.text_input('İsim')
soyisim = st.text_input('Soyisim')
#parola = st.text_input('Parola', type='password')
min_date = datetime(1949, 1, 1)
dogum_tarihi = st.date_input('Doğum Tarihi', min_value=min_date)
yas = st.slider('Yaş', 18, 60)
mail_adresi = st.text_input('E-posta')
telefon = st.text_input('Telefon')

# Eğer "form.csv" dosyası varsa oku, yoksa oluştur
try:
    df = pd.read_csv('form.csv')
except FileNotFoundError:
    st.error('Kayıt dosyası bulunamadı')
    df = pd.DataFrame(columns=['İsim', 'Soyisim', 'Doğum Tarihi', 'Yaş', 'E-posta', 'Telefon'])
    df.to_csv('form.csv', index=False)

if st.button('Gönder'):
    try:
        # Alanların zorunlu olmasını kontrol et
        if not isim or not soyisim or not dogum_tarihi or yas is None:
            st.error('Tüm alanları doldurmanız gerekmektedir')
        elif mail_adresi and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', mail_adresi):
            st.error('Geçersiz e-posta adresi')
        elif telefon and len(telefon) != 10:
            st.error('Telefon numarası 10 karakter olmalıdır')
        else:
            df.loc[len(df)] = [isim, soyisim, dogum_tarihi, yas, mail_adresi, telefon]
            df.to_csv('form.csv', index=False)
            st.success('Gönderildi')

            # Kaydedilen veri listesini görüntüle
            st.subheader("Kaydedilen Veriler")
            st.dataframe(df)

    except Exception as e:
        st.error('Gönderilemedi: ' + str(e))