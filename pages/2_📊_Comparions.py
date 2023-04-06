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

# create a folium map centered on the first location in the dataframe
m = folium.Map(location=[0,0], zoom_start=1)

# create a marker cluster layer for each location
marker_cluster = folium.plugins.MarkerCluster().add_to(m)

# iterate through each location and create a circle marker for each genre
for i, row in grouped.iterrows():
    # calculate the size of the circle based on the average picture rating
    size = row['avg_pic'] 
    
    # determine the color of the circle based on the most common genre
    color_dict = {'action': 'red', 'comedy': 'green', 'drama': 'blue'}
    color = color_dict.get(row['genre_y'])
    
    # create the circle marker and add it to the marker cluster layer
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=size,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=f"{row['genre_x']} ({row['avg_pic']:.1f})<br>Count: {row['genre_count']}"
    ).add_to(marker_cluster)

# display the map in Streamlit
folium_static(m)


