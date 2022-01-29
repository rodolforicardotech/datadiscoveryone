import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import PortugueseStemmer
from nltk.corpus import stopwords
from selenium import webdriver
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import urllib.parse
import urllib
import requests
import base64
import plotly.express as px
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt


stemmer    = PortugueseStemmer()
stop_words = stopwords.words('portuguese')
analyzer = TfidfVectorizer().build_analyzer()
def stemmed_words(doc):
    return (stemmer.stem(w) for w in analyzer(doc))
stem_vectorizer = TfidfVectorizer(analyzer=stemmed_words,stop_words=stop_words,max_features=3700)
model = pickle.load(open('app/lr_model.pkl','rb'))
#nltk.download('stopwords')
st.title('Análise de coméntarios')

option = st.selectbox(
     'Selecione uma opção:',
     ( 'URL-Amazon', 'URL-Magazine luiza', 'Texto'))
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
elif option == 'URL-Amazon':
    url = st.text_input("digite a URL aqui") 
    if url != '':
        #st.write(url)

        message_bytes = url.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        start_button = st.empty()
        img = st.empty()
        option_visual = st.empty()
        json_txt = requests.get('https://api.datadiscovery.acilab.com.br/get_coments/'+urllib.parse.quote(base64_message,safe='')).json()
        cont = [0,0]
        df_cont = pd.DataFrame()
        count = 0
        msgs = []
        msgs_positivas = []
        msgs_negativas = []
        for x in (json_txt):
            #x['comment']
            try:
                msgs.append(x['comment'])
                pred = model.predict([x['comment']])
                if pred == 0:
                    msgs_negativas.append(x['comment'])
                    if count <20:
                        pass
                        st.markdown((x['comment'])+' ❌')
                    cont[0] += 1
                    #df_cont = pd.DataFrame([{'Classificações Positivas':cont[1],'Classificações Negativas':cont[0]}])
                else:
                    msgs_positivas.append(x['comment'])
                    if count <20:
                        pass
                        st.markdown(str(x['comment'])+' ✅')
                    cont[1] += 1
                    #df_cont = pd.DataFrame([{'Classificações Positivas':cont[1],'Classificações Negativas':cont[0]}])
                count += 1
                #fig = px.bar(df_cont,x=[0,1], y=cont)
                df_cont = pd.DataFrame([{'Classificações Positivas':cont[1],'Classificações Negativas':cont[0]}])
                fig = px.bar(df_cont, y=['Classificações Positivas','Classificações Negativas'], barmode='group')
                fig.update_layout(yaxis_range=[0,int(len(json_txt))])
                start_button.write(fig, use_container_width=True)
                if (count %50 ==0 or count == 1 ):
                    # adicionando uma variavel chamada STOPWRODS e lendo um arquivo com stopwords em português
                    stopwords0 = pd.read_csv("app/stopwords.txt", sep=" ", header=None)
                    stopwords0 = stopwords0[0].values.tolist()
                    msgs_plot = [word for word in msgs if word not in stopwords0]
                    text3 = " ".join(title for title in msgs_plot)

                    # Creating word_cloud with text as argument in .generate() method
                    word_cloud3 = WordCloud(collocations = False, background_color = 'white').generate(text3)
                    # Plot1
                    plt.title('Nuvem de palavras')
                    plt.axis('off')
                    plt.tight_layout()
                    plt.imshow(word_cloud3)
                    img.pyplot()
            except:
                pass
                #'erro'
        a= """
        option5 = option_visual.selectbox(
             'Opções de visualização',
             ('Nuvem de palavras GERAL', 'Amostragem de Classificações', 'Nuvem de Palavras Positivas','Nuvem de Palavras Negativas'))

        st.write('Sua seleção:', option)
        if option5 == 'Nuvem de palavras GERAL':
            stopwords0 = pd.read_csv("app/stopwords.txt", sep=" ", header=None)
            stopwords0 = stopwords0[0].values.tolist()
            msgs_plot = [word for word in msgs if word not in stopwords0]
            text3 = " ".join(title for title in msgs_plot)

            # Creating word_cloud with text as argument in .generate() method
            word_cloud3 = WordCloud(collocations = False, background_color = 'white').generate(text3)
            # Plot1
            plt.title('Nuvem de palavras')
            plt.axis('off')
            plt.tight_layout()
            plt.imshow(word_cloud3)
            img.pyplot()
        elif option5 == 'Nuvem de Palavras Positivas':
            stopwords0 = pd.read_csv("app/stopwords.txt", sep=" ", header=None)
            stopwords0 = stopwords0[0].values.tolist()
            msgs_plot = [word for word in msgs_positivas if word not in stopwords0]
            text3 = " ".join(title for title in msgs_plot)

            # Creating word_cloud with text as argument in .generate() method
            word_cloud3 = WordCloud(collocations = False, background_color = 'white').generate(text3)
            # Plot1
            plt.title('Nuvem de palavras')
            plt.axis('off')
            plt.tight_layout()
            plt.imshow(word_cloud3)
            img.pyplot()
    """

    else:
        pass            
else:
    txt = st.text_area("digite o texto")
    if txt != '':
        pred = model.predict([txt])
        if pred == 0:
            st.markdown((txt)+' ❌')
        elif pred == 1:
            st.markdown(str(txt)+' ✅')
        st.write(model.predict_proba([txt]))


#if txt != '':
#    st.write(model.predict_proba([txt]))



