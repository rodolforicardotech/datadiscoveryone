#Número de comentários positivos e negativos
#adicionar as variáveis "positivos" e "negativos" no loop for e contar
if model.predict([df['data']['objects'][comment]['review_text']]) == 0:
    st.markdown(df['data']['objects'][comment]['review_text']+' ❌')
    positivos = df['data']['objects'][comment]['review_text']+' ❌'
    positivos_contagem = positivos.sum()
else:
    st.markdown(df['data']['objects'][comment]['review_text']+' ✅')
    negativos = df['data']['objects'][comment]['review_text']+' ❌'
    negativos_contagem = negativos.sum()

print('Comentários Positivos: ' + positivos_contagem)
print('Comentários Negativos: ' + negativos_contagem)

#Adicionando nota média
#A tag da nota no html: <span class="js-rating-value">4,5</span>
nota_media = driver.page_source.find('class="js-rating-value"')
print('A nota média do produto é: ' + str(nota_media))

#Criando uma Nuvem de Palavras
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(background_color="white").generate('')#```aqui fica o DF ou df['reviews']```

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()