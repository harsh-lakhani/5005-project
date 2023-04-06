# Libraries
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Config
st.set_page_config(page_title='COMPARISONS', page_icon=':bar_chart:', layout='wide')

# Title
st.markdown(f'<h1 style="color:#ffffff;font-size:48px;">{"📊 COMPARISONS"}</h1>', unsafe_allow_html=True)

import plotly.express as px

# GEOSPATIAL PLOT
df = pd.read_csv('data/final_geo.csv')

# group the data by location and genre to calculate the average picture rating
grouped = df.groupby(['latitude', 'longitude', 'genre']).agg({
    'avg_pic': 'mean',
    'genre_count': 'sum'
}).reset_index()

# determine the most common genre in each location
most_common_genre = grouped.groupby(['latitude', 'longitude'])['genre'].agg(lambda x:x.value_counts().index[0]).reset_index()

# join the most common genre with the grouped data
grouped = pd.merge(grouped, most_common_genre, on=['latitude', 'longitude'], how='left')

# add the country column to the grouped data
grouped = pd.merge(grouped, df[['country', 'latitude', 'longitude']].drop_duplicates(), on=['latitude', 'longitude'], how='left')

# create a scatter geo plot using Plotly Express
fig = px.scatter_geo(grouped, 
                     lat="latitude",
                     lon="longitude",
                     color="genre_y", # color the markers by the most common genre
                     size="avg_pic", # size the markers by the average picture rating
                     hover_name="country",
                     projection="natural earth"
                     )

# show the plot within the Streamlit app
st.plotly_chart(fig)


