# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Config
st.set_page_config(page_title='In Depth Analysis', page_icon=':bar_chart:', layout='wide')

# Title
st.markdown(f'<h1 style="color:#ffffff;font-size:48px;">{"In Depth Analysis"}</h1>', unsafe_allow_html=True)


df =  pd.read_csv('data/titles_all_genre_mod.csv')

df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1','description',  'production_countries', 'main_prod_ctry_full'], inplace=True)
categories = [ 'platform', 'id', 'type',
        'age_certification', 'genres',
       'main_prod_ctry']
neg=  [ 'id', 'title', 'imdb_id']
for  cat in categories:
    df[cat] = df[cat].astype('category')
    

dimensions = []
for col in df.columns:
    if col not in neg:
        if col in categories:
            new_cat = df[col].dropna()            
            dim = dict(
                tickvals=new_cat.cat.codes.unique(),
                ticktext=new_cat.cat.categories,
                label=col, 
                values=new_cat.cat.codes
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
        labelfont=dict(size=18),
        tickfont=dict(size=16),
    )                       
)

# update the layout to include a title and legend
fig.update_layout(title='Parallel Coordinate Plot',
                  margin=dict(l=100,),
                  height=1000,)


fig.update_traces(
        customdata=df['title'],
)

def handle_hover(trace, points, state):
    if points.point_inds:
        print(f"Hovered over line {points.point_inds[0]}")

fig.data[0].on_hover(handle_hover)

st.plotly_chart(fig, use_container_width=True)