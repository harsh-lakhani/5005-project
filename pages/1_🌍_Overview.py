# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Page Config
st.set_page_config(page_title='OVERVIEW', page_icon=':bar_chart:', layout='wide')

st.markdown(f'<h1 style="color:#ffffff;font-size:48px;">{"🌍 OVERVIEW"}</h1>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
c1.markdown(f'<p style="color:#ffffff;font-size:12px;">{"Data Description"}</p>', unsafe_allow_html=True)
c11, c12 = c1.columns(2)
data = {'Total Content': ['Number of attributes'], 20550: [''], 'Target Variable': ['Popularity']}
c11.write('Total Content')
c11.write('Number of attributes')
c11.write('Target Variable')
c12.write('20,550')
c12.write('18')
c12.write('Popularity')

"^ Need to make the above data into a table ^"

c3, c4 = st.columns(2)
df = pd.read_csv('data/titles_all.csv')

def interactive_plot():
    plot = px.bar(data_frame=df.groupby("type")["pic"].mean().reset_index(), x="type", y="pic")
    st.plotly_chart(plot, use_container_width=True)

with c3:    
    "Number of content on each platform"
    interactive_plot()
    "As you can see, creating a movie or a show does not affect the popularity"

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