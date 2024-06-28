import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Türkçe doğal dil işleme için gerekli veri setlerini indirin
nltk.download('stopwords')
nltk.download('punkt')

def generate_wordcloud(text):
    # Türkçe stop kelimelerini yükleyin
    stop_words = set(stopwords.words('turkish'))

    # Metni küçük harflere dönüştürün
    text = text.lower()

    # Kelimeleri ayıklayın ve stop kelimeleri hariç tutun
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Eklerden kökleri elde edin
    #stemmer = SnowballStemmer('turkish')
    #stemmed_words = [stemmer.stem(word) for word in filtered_words]

    # Kelime frekansını hesaplayın
    word_freq = nltk.FreqDist(filtered_words)

    # Kelime bulutunu oluşturun
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    # Kelime bulutunu görselleştirin
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def main():
    st.title("Türkçe Eklemelerin Köklerini Bulma ve Kelime Bulutu Oluşturma")

    option = st.radio(
        "Metni nasıl girmek istersiniz?",
        ("Metin Yaz", "Dosya Yükle")
    )

    if option == "Metin Yaz":
        text = st.text_area("Metni buraya yazın", height=200)
        if st.button("Kelime Bulutunu Oluştur"):
            if text:
                generate_wordcloud(text)
            else:
                st.warning("Lütfen metin girin.")

    elif option == "Dosya Yükle":
        uploaded_file = st.file_uploader("Metin dosyasını yükleyin", type=["txt"])
        if st.button("Kelime Bulutunu Oluştur"):
            if uploaded_file is not None:
                text = uploaded_file.read().decode("utf-8")
                generate_wordcloud(text)
            else:
                st.warning("Lütfen bir dosya yükleyin.")

if __name__ == "__main__":
    main()