import streamlit as st
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def initialize_zemberek():
    Zemberek = JClass("zemberek.morphology.TurkishMorphology")
    TurkishSentenceNormalizer = JClass("zemberek.normalization.TurkishSentenceNormalizer")
    TurkishTokenizer = JClass("zemberek.tokenization.TurkishTokenizer")

    # Zemberek için gerekli Java sanal makinesini başlatın
    st.warning("Zemberek-NLP'nin başlatılması biraz zaman alabilir. Lütfen bekleyin...")
    st.info("Java sanal makinesi başlatılıyor...")
    getDefaultJVMPath()

    # TurkishMorphology sınıfını başlatın
    st.info("Zemberek-NLP başlatılıyor...")
    morphology = Zemberek.createWithDefaults()

    # TurkishSentenceNormalizer sınıfını başlatın
    normalizer = TurkishSentenceNormalizer(morphology)

    # TurkishTokenizer sınıfını başlatın
    tokenizer = TurkishTokenizer.DEFAULT

    return morphology, normalizer, tokenizer

def normalize_text(normalizer, text):
    return normalizer.normalize(JString(text)).getNormalizedSentence()

def generate_wordcloud(text, morphology, tokenizer):
    # Metni normalize edin
    normalized_text = normalize_text(normalizer, text)

    # Kelimeleri ayıklayın
    tokenized_words = tokenizer.tokenizeToStrings(normalized_text)

    # Kökleri bulun
    stemmed_words = [morphology.stem(word).get(0).getRoot() for word in tokenized_words]

    # Kökleri birleştirin ve tekrar sayın
    word_freq = {}
    for word in stemmed_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

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
                generate_wordcloud(text, morphology, tokenizer)
            else:
                st.warning("Lütfen metin girin.")

    elif option == "Dosya Yükle":
        uploaded_file = st.file_uploader("Metin dosyasını yükleyin", type=["txt"])
        if st.button("Kelime Bulutunu Oluştur"):
            if uploaded_file is not None:
                text = uploaded_file.read().decode("utf-8")
                generate_wordcloud(text, morphology, tokenizer)
            else:
                st.warning("Lütfen bir dosya yükleyin.")

if __name__ == "__main__":
    # Zemberek-NLP'yi başlatın
    morphology, normalizer, tokenizer = initialize_zemberek()

    try:
        main()
    finally:
        # Java sanal makinesini kapatın
        shutdownJVM()