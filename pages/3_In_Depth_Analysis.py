# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import streamlit.components.v1 as components

import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Config
st.set_page_config(page_title='In Depth Analysis', page_icon=':bar_chart:', layout='wide')

# Title
st.markdown(f'<h1 style="color:#ffffff;font-size:48px;">{"In Depth Analysis"}</h1>', unsafe_allow_html=True)

def parallel_coordinates():
    df =  pd.read_csv('data/titles_all.csv')
    df.drop(columns=['Unnamed: 0', 'description','country_code'], inplace=True)
    categories = [ 'platform', 'id', 'type',
            'age_certification', 'genres',
        'production_countries']
    neg=  [ 'id', 'title', 'imdb_id']
    for  cat in categories:
        df[cat] = df[cat].astype('category')
        

    dimensions = []
    for col in df.columns:
        if col not in neg:
            if col in categories:       
                dim = dict(
                    tickvals=df[col].cat.codes.unique(),
                    ticktext=df[col].cat.categories,
                    label=col, 
                    values=df[col].cat.codes
                )
            else:
                dim = dict(
                    range=[df[col].min(), df[col].max()],
                    constraintrange=[df[col].quantile(0), df[col].quantile(0.9)],
                    label=col, 
                    values=df[col]
                )
            dimensions.append(dim)

    # add custom data to the hover tooltip using the 'customdata' parameter
    fig = go.Figure(
        data=go.Parcoords(dimensions=dimensions,
            line=dict(color=df['id'].cat.codes,
                    colorscale='Electric',
                    showscale=True),
            # customdata=df['title'],
            labelfont=dict(size=20),
            tickfont=dict(size=16),
            rangefont=dict(size=16),
        )                       
    )

    # update the layout to include a title and legend
    fig.update_layout(title='Parallel Coordinate Plot',
                    margin=dict(l=100,),
                    height=1000,)

    st.plotly_chart(fig, use_container_width=True)

def map():    
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

def network():
    with st.container():
        components.iframe("https://public.tableau.com/views/Network_16814579200620/SimpleNetworkGraph?:language=en-US&publish=yes&:display_count=n&:showVizHome=no&:embed=true",
                    height=1800) 



tabs = ["Map","Parallel Coordinates", "Network"]
col1, col2, col3 = st.columns(3)
with col1:
    button1 = st.button(tabs[0],use_container_width=True, )
with col2:
    button2 = st.button(tabs[1],use_container_width=True)
with col3:
    button3 = st.button(tabs[2],use_container_width=True)
    
# set the default tab
if not button1 and not button2 and not button3:
    button1 = True

# click on the tab buttons to switch between tabs
if button1:
    map()
elif button2:
    parallel_coordinates()
elif button3:
    network()
