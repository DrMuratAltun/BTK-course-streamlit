import streamlit as st
import pandas as pd
import pickle

st.title('Maaş Modeli : heavy:heavy_dollar_sign:')
model=pickle.load(open('salary.pkl','rb'))
tecrube=st.number_input('Tecrübe',1,10)
yazili=st.number_input('Sınav',1,10)
mulakat=st.number_input('Mülakat',1,10)
if st.button('Hesapla'):
	tahmin=model.predict([[tecrube,yazili,mulakat]])
	tahmin=round(tahmin[0],2)
	st.write(f'Tahmini Maaş: {tahmin}')


