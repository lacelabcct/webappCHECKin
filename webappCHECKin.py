#libraries
#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import datetime
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTN00fNo-fKTaMHme6ed2fTMkmqvoCxUA_u1PmkL9bADZ-OXrVcTvmw4o3yrgRjGdP09vOd51Za2uPE/pub?gid=0&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)

NregD = len(dfD)

# eliminar as colunas com valores ausentes
summary = dfD.dropna(subset=['Mensagem'], axis=0)['Mensagem']
# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "ou", "os", "ser", "só"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1600, height=800).generate(all_summary)
# mostrar a imagem final
#fig, ax = plt.subplots(figsize=(10,6))
#ax.imshow(wordcloud, interpolation='bilinear')
#ax.set_axis_off()
plt.imshow(wordcloud);
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#st.pyplot()
wordcloud.to_file("Nuvem_de_Palavras_Mensagem.png")
image01 = Image.open('ImagemLateral.jpg')
st.sidebar.image(image01, width=300, caption='Mack Week CCT 2022') 
st.title("PAINEL FabLab")

st.header("Principais Dúvidas:")
st.pyplot() #Este método faz exibirt a nuvem de palavras
st.set_option('deprecation.showPyplotGlobalUse', False)

#st.subheader("Sub Cabeçalho")
#st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
menu = ["Dúvidas",
        "Respostas"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.info("By: Prof. Massaki de O. Igarashi")
