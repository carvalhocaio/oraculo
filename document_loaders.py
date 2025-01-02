import os
from time import sleep
import streamlit as st
from langchain_community.document_loaders import (
    WebBaseLoader,
    YoutubeLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader
)
from fake_useragent import UserAgent


# url_site = 'http://2025.pythonbrasil.org.br/'
def carrega_site(url_site):
    documento = ''
    for i in range(5):     
        try:
            os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url_site, verify_ssl=False, raise_for_status=True)
            lista_documentos = loader.load()
            documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
            break
        except:
            print(f'Erro ao carregar o site {i+1}')
            sleep(3)
    
    if documento == '':
        st.error('Não foi possível carregar o site')
        st.stop()
    return documento


# url_youtube = 'HDL6IbrQhgU'
def carrega_youtube(url_youtube):
    loader = YoutubeLoader(url_youtube, add_video_info=False, language=['pt'])
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

# csv_path = 'data/nfl_teams.csv'
def carrega_csv(csv_path):
    loader = CSVLoader(csv_path)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

# pdf_path = 'data/nfl_teams.pdf'
def carrega_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

# txt_path = 'data/nfl_teams.txt'
def carrega_txt(txt_path):
    loader = TextLoader(txt_path)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento
