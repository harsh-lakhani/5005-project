# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Confit
st.set_page_config(page_title='OVERVIEW', page_icon=':bar_chart:', layout='wide')

st.markdown(f'<h1 style="color:#ffffff;font-size:48px;">{"🌍 OVERVIEW"}</h1>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
c1.markdown(f'<p style="color:#ffffff;font-size:12px;">{"Data Description"}</p>', unsafe_allow_html=True)
df = pd.read_csv('data/titles_all_genre_mod.csv')
c11, c12 = c1.columns(2)
data = {'Total Content': ['Number of attributes'], 20550: [''], 'Target Variable': ['Popularity']}
df1 = pd.DataFrame(data)
c11.write('Total Content')
c11.write('Number of attributes')
c11.write('Target Variable')
c12.write('20,550')
c12.write('18')
c12.write('Popularity')

# df_heatmap = df.drop(columns=['id', 'title', 'description', 'imdb_id'], axis=1)

# # label_encoder object knows how to understand word labels.
# label_encoder = preprocessing.LabelEncoder()

# # Encode labels in categorial columns
# df_heatmap['platform']= label_encoder.fit_transform(df_heatmap['platform'])
# df_heatmap['type']= label_encoder.fit_transform(df_heatmap['type'])
# df_heatmap['age_certification']= label_encoder.fit_transform(df_heatmap['age_certification'])
# df_heatmap['genres']= label_encoder.fit_transform(df_heatmap['genres'])
# df_heatmap['production_countries']= label_encoder.fit_transform(df_heatmap['production_countries'])
# df_heatmap['main_prod_ctry']= label_encoder.fit_transform(df_heatmap['main_prod_ctry'])
# df_heatmap['main_prod_ctry_full']= label_encoder.fit_transform(df_heatmap['main_prod_ctry_full'])

# fig, ax = plt.subplots()
# sns.heatmap(df_heatmap.corr(), ax=ax)
# st.write(fig)

df = pd.read_csv('titles_all.csv')