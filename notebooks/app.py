import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import PortugueseStemmer
from nltk.corpus import stopwords
from selenium import webdriver
import re
from selenium.webdriver.firefox.options import Options
import time

stemmer    = PortugueseStemmer()
stop_words = stopwords.words('portuguese')
analyzer = TfidfVectorizer().build_analyzer()
def stemmed_words(doc):
    return (stemmer.stem(w) for w in analyzer(doc))
stem_vectorizer = TfidfVectorizer(analyzer=stemmed_words,stop_words=stop_words,max_features=3700)
model = pickle.load(open('lr_model.pkl','rb'))
#nltk.download('stopwords')
st.title('Análise de coméntarios')

option = st.selectbox(
     'Selecione uma opção:',
     ('URL-Magazine luiza', 'Texto'))
txt = ''
if option == 'URL-Magazine luiza':
    txt = st.text_input("digite a URL aqui")
    if txt != '':

        options = Options()
        driver = webdriver.Firefox()
        #driver.get("https://www.magazineluiza.com.br/creme-de-leite-integral-piracanjuba-200g/p/226146500/me/crml/")
        driver.get(txt)
        codigo = driver.page_source.split('Código ')[1].split(' ')[0]
        index_i = driver.page_source.find('class="showcase-product__big-img js-showcase-big-img ls-is-cached lazyloaded"')
        st.image(
            driver.page_source[index_i:index_i+450].split('src="')[1].split(' ')[0].replace('"',''),
            width=400, # Manually Adjust the width of the image as per requirement
        )
        time.sleep(np.random.randint(1,10))
        driver.get("https://www.magazineluiza.com.br/review/"+codigo+"/?page=1")
        txt = re.sub('<[^<]+?>', '', driver.page_source).replace('JSONDados brutosCabeçalhosSalvarCopiarFormatar','')
        
        df = pd.read_json(txt).to_dict()#.append(pd.read_json(txt2))
        for comment in range(len(df['data']['objects'])):
            if df['data']['objects'][comment]['review_text'] != None:
                if model.predict([df['data']['objects'][comment]['review_text']]) == 0:
                    st.markdown(df['data']['objects'][comment]['review_text']+' ❌')
                else:
                    st.markdown(df['data']['objects'][comment]['review_text']+' ✅')
                driver.get("https://www.magazineluiza.com.br/review/"+codigo+"/?page=2")
        time.sleep(np.random.randint(1,10))
        if len(df['data']['objects']) == 10:
            driver.get("https://www.magazineluiza.com.br/review/"+codigo+"/?page=2")
            txt2 = re.sub('<[^<]+?>', '', driver.page_source).replace('JSONDados brutosCabeçalhosSalvarCopiarFormatar','')
            df = pd.read_json(txt2).to_dict()#.append(pd.read_json(txt2))
            for comment in range(len(df['data']['objects'])):
                if df['data']['objects'][comment]['review_text'] != None:
                    if model.predict([df['data']['objects'][comment]['review_text']]) == 0:
                        st.markdown(df['data']['objects'][comment]['review_text']+' ❌')
                    else:
                        st.markdown(df['data']['objects'][comment]['review_text']+' ✅')
        driver.quit()
                    
else:
    txt = st.text_area("digite o texto")

if txt != '':
    st.write(model.predict_proba([txt]))


