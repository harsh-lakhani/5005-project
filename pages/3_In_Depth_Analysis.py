# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import streamlit.components.v1 as components
import numpy as np
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Config
st.set_page_config(page_title='IN DEPTH ANALYSIS', page_icon=':bar_chart:', layout='wide')

# Title
st.markdown(f'<h1 style=";font-size:48px;">{"IN DEPTH ANALYSIS"}</h1>', unsafe_allow_html=True)

def parallel_coordinates():
    df =  pd.read_csv('data/titles_all.csv')
    df.drop(columns=['Unnamed: 0', 'description','country_code'], inplace=True)
    # log scale the pic column
    df['pic'] = df['pic'].drop(df[df['pic'] ==0].index)
    df['pic'] = np.log(df['pic'])
    
    categories = [ 'platform', 'id', 'type', 'age_certification', 'genres',  'production_countries']
    column_order = ['platform', 'type','release_year', 'age_certification', 'genres', 'runtime', 'pic']
    neg=  [ 'id', 'title', 'imdb_id']
    for  cat in categories:
        df[cat] = df[cat].astype('category')
        
    pic_slider = st.slider('Select the PIC Range', min_value=0.0, max_value=1.0, value=st.session_state['pic_slider'], step=0.05)
    if pic_slider != st.session_state['pic_slider']:
        st.session_state['pic_slider'] = pic_slider
    dimensions = []
    for col in column_order:
        if col not in neg:
            if col in categories:    
                dim = dict(
                    tickvals=df[col].cat.codes.unique(),
                    ticktext=df[col].cat.categories,
                    label=col, 
                    values=df[col].cat.codes,
                )
            else:
                constraint_range = [df[col].min(), df[col].max()]
                if col == 'runtime':
                    constraint_range = [df[col].quantile(0), df[col].quantile(0.9)]
                elif col == 'pic':
                    constraint_range = [df[col].quantile(st.session_state['pic_slider'][0]), df[col].quantile(st.session_state['pic_slider'][1])]
                dim = dict(
                    range=[df[col].min(), df[col].max()],
                    constraintrange=constraint_range,
                    label=col, 
                    values=df[col]
                )
            dimensions.append(dim)

    # add custom data to the hover tooltip using the 'customdata' parameter
    fig = go.Figure(
        data=go.Parcoords(dimensions=dimensions,
            line=dict(color=df['id'].cat.codes,
                    # colorscale='Electric',
                    colorscale = [[0,'orange'],[1,'orange']]
                    # showscale=True
                    ),
            # customdata=df['title'],
            labelfont=dict(size=20),
            tickfont=dict(size=16),
            rangefont=dict(size=16),
        )                       
    )

    # update the layout to include a title and legend
    fig.update_layout(title='Parallel Coordinate Plot',
                    margin=dict(l=120,r=100),
                    height=800,)

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
                        projection="natural earth",
                        )

    # update the layout to include a title and legend
    fig.update_layout( title='Average Content Rating by Genre and Location',
                    height=700,)
    # show the plot within the Streamlit app
    st.plotly_chart(fig, use_container_width=True)

def network():
    with st.container():
        components.iframe("https://public.tableau.com/views/Network_16814579200620/SimpleNetworkGraph?:language=en-US&publish=yes&:display_count=n&:showVizHome=no&:embed=true",
                    height=1800) 

tabs = ["Location-Genre Plot","Parallel Coordinates Plot", "Actor-Director Network"]
col1, col2, col3 = st.columns(3)
with col1:
    button1 = st.button(tabs[0],use_container_width=True, )
with col2:
    button2 = st.button(tabs[1],use_container_width=True)
with col3:
    button3 = st.button(tabs[2],use_container_width=True)

if 'tab' not in st.session_state:
    st.session_state.tab = 0
if 'pic_slider' not in st.session_state:
    st.session_state['pic_slider']= (0.0, 0.9)
# click on the tab buttons to switch between tabs
if button1:
    st.session_state.tab = 0
elif button2:
    st.session_state.tab = 1
elif button3:
    st.session_state.tab = 2

if st.session_state.tab == 0:
    map()
elif st.session_state.tab == 1:
    parallel_coordinates()
elif st.session_state.tab == 2:
    network()