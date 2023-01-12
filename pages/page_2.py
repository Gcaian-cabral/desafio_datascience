import streamlit as st
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

st.markdown("# Parte 2 ")
st.sidebar.markdown("# Parte 2 ")

st.write('Tabela mostrando o artista favorito e seus ouvintes mensais')

r = requests.get("https://open.spotify.com/artist/1Bl6wpkWCQ4KVgnASpvzzA")

soup = bs(r.content)

headers = soup.find("h1")
artist_name = headers.string

div = soup.find('div', attrs={'data-testid': 'monthly-listeners-label'})
monthly_listeners = div.string

st.write(pd.DataFrame({
    'Artista Favorito': artist_name,
    'Ouvintes Mensais': monthly_listeners,
}, index=[0]))