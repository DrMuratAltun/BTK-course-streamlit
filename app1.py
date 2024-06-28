# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:29:28 2024

@author: drmurataltun
"""

import streamlit as st
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('MLOPS Streamlit Apps @drmurataltun :flag-tr:')
import pandas as pd
import plotly.express as px
df=pd.read_csv('data/prog_languages_data.csv')
fig=px.pie(df,values='Sum')
st.plotly_chart(fig)
fig2=px.bar(df,x='lang',y='Sum')
st.plotly_chart(fig2)
isim=st.text_input('isminizi girin:', max_chars=20)
file=st.file_upload('dosyayı yükle')
#st.video('data/secret_of_success.mp4')
#st.camera_input('camera')
st.code('''
import pandas as pd
df=pd.read_csv('data/iris.csv')
st.write(df)
	''')
menu=['Ana Sayfa','Makine Öğrenmesi','Bize Ulaşın','hakkımızda']
st.sidebar.selectbox('Menü',menu)
st.success('Başarılı')
st.error('Bir hata oluştu')
st.date_input('tarih seç')
st.time_input('saat seç')
st.text_input('Parola Oluştur :', type='password')
st.text_area('Mesajınız :',height=80)
st.number_input('Yaşınızı giriniz',1,100)
st.radio('Medeni durumu',('evli', 'bekar'))
st.selectbox('Bildiğiniz Programlama Dilleri',('C++', 'Python','Julia', 'QSharp'))
st.multiselect('Bildiğiniz Programlama Dilleri',('C++', 'Python','Julia', 'QSharp'))
#st.video('http://192.168.1.37:8080/video')#telefonu ip camera olarak kullanmak
st.image('data/image_01.jpg')
st.text('<br><b>Murat</b>')
st.divider()
df=pd.read_csv('data/iris.csv')
st.write(df) #st.table tablo olarak
#local de yayın yapmak için aynı ağda bağlı olsun 
#server çalıştır
#streamlit run app.py
#Çalışırken sayfa değişiyor

#Kaynak:https://z-uo.medium.com/live-webcam-with-streamlit-f32bf68945a4
#Nasıl deploy yapılır: https://docs.streamlit.io/streamlit-community-cloud/get-started