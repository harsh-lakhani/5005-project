# Libraries
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Confit
st.set_page_config(page_title='', page_icon=':bar_chart:', layout='wide')

# Title
# st.title('BEST VIDEO CONTENT for OVER-THE-TOP (OTT) STREAMING SERVICE')

st.markdown(f'<h1 style=";font-size:48px;">{"BEST VIDEO CONTENT for OVER-THE-TOP (OTT) STREAMING SERVICE"}</h1>', unsafe_allow_html=True)

# Content
c1, c2, c3, c4 = st.columns(4)
c1.image(Image.open('images/disney-logo.png'), width=200)
c2.image(Image.open('images/HBO-logo.png'), width=200)
c3.image(Image.open('images/netlix-logo.png'), width=200)
c4.image(Image.open('images/prime-logo.png'), width=200)

st.write(
    """
    According to [**Livingetc**](https://www.livingetc.com/advice/netflix-vs-amazon-prime), Netflix is the most popular among all streaming platforms while Prime comes to the second. 
    However, as you can see that (our graph) the quantity of content ranks as Prime>Netflix>HBO>Disney. 
    """
)

df =  pd.read_csv('data/titles_all_genre_mod.csv')

def interactive_plot():
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    plot = px.bar(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

"Number of content on each platform"

# interactive_plot()

# st.bar_chart(df, y = 'Type', x='Month')
# chart_data = pd.DataFrame(df, columns=["type"])
# st.bar_chart(chart_data)

st.write(
    """
    However, as you can see that (our graph) the quantity of content ranks as Prime>Netflix>HBO>Disney. 
    """
)

st.subheader('Question at hand')
st.write(
    """
    Doubtless, content quantity offered by a platform is crucial for its popularity as .... 
    But why does Prime put so much effort in gathering videos worldwide but still is not as popular as Netflix? This shows that popularity is by and large attributed to the content quality. 
    How to produce a video that will gain popularity? 
    We are certain many producers have been thinking about this question.
    """
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.info('**Chan Kar Chun (20729353)**', icon="💡")
with c2:
    st.info('**Lakhani Harsh Sunil (20910249)**', icon="💻")
with c3:
    st.info('**Tsang Kai Ho (20905476)**', icon="🧠")
with c4:
    st.info('**Wong Yan Ho (20605624)**', icon="👨🏻‍🎓")