import streamlit as st
import pandas as pd

st.title('Desafio Onidevs')
st.markdown("# Parte 1")
st.sidebar.markdown("# Parte 1 ")

df = pd.read_csv('genres_v2.csv')

danceabilityTop5 = df.nlargest(5, ['danceability'])
energyTop5 = df.nlargest(5, ['energy'])
speechinessTop5 = df.nlargest(5, ['speechiness'])
acousticnessTop5 = df.nlargest(5, ['acousticness'])

st.header('Top 5 Danceability')
danceabilityTop5 = danceabilityTop5[['danceability']]
st.table(danceabilityTop5)

st.header('Top 5 Energy')
energyTop5 = energyTop5[['energy']]
st.table(energyTop5)

st.header('Top 5 Speechiness')
speechinessTop5 = speechinessTop5[['speechiness']]
st.table(speechinessTop5)

st.header('Top 5 Acousticness')
acousticnessTop5 = acousticnessTop5[['acousticness']]
st.table(acousticnessTop5)

st.header('Top 10 Most Common Genres')
values = df['genre'].value_counts().nlargest(10)
st.bar_chart(values)

st.header('Max & Min Song Duration')
max_duration = df.nlargest(1, 'duration_ms')
min_duration = df.nsmallest(1, 'duration_ms')
max_min_duration = pd.concat([max_duration, min_duration])
max_min_duration = max_min_duration[['duration_ms']]
st.table(max_min_duration)

st.header('Show Table by Given Id')
number = st.number_input('Insert a number')
given_id = df.loc[[number]]
st.dataframe(given_id)