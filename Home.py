# Libraries
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from sklearn import preprocessing
import streamlit.components.v1 as components


# Config
st.set_page_config(page_title='', page_icon=':bar_chart:', layout='wide')

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.info('**Chan Kar Chun (20729353)**', icon="💡")
with c2:
    st.info('**Lakhani Harsh Sunil (20910249)**', icon="💻")
with c3:
    st.info('**Tsang Kai Ho (20905476)**', icon="🧠")
with c4:
    st.info('**Wong Yan Ho (20605624)**', icon="👨🏻‍🎓")

st.markdown(f'<h1 style="font-size:65px;font-weight:bold">{"POPULAR VIDEO CONTENT RECOMMENDATION TOOL"}</h1>', unsafe_allow_html=True)

# st.markdown(f'<h1 style="font-size:48px;color:#ff0000;font-weight:bold">{"FOR OVER-THE-TOP STREAMING SERVICES"}</h1>', unsafe_allow_html=True)

# Content
c1, c2, c3, c4 = st.columns(4)
c1.image(Image.open('images/disney-logo.png'), width=200)
c2.image(Image.open('images/HBO-logo.png'), width=200)
c3.image(Image.open('images/netlix-logo.png'), width=200)
c4.image(Image.open('images/prime-logo.png'), width=200)


st.markdown(f'<h1 style="font-size:48px;">{"INTRODUCTION"}</h1>', unsafe_allow_html=True)

# link_text = 'According to [Livingetc](https://www.livingetc.com/advice/netflix-vs-amazon-prime), Netflix is the most popular among all streaming platforms while Prime comes second.'
# markdown_text = f'<h1 style="font-size:20px;">{link_text}</h1>'
# st.markdown(markdown_text, unsafe_allow_html=True)

link = 'https://www.livingetc.com/advice/netflix-vs-amazon-prime'
text = 'Livingetc'
message = f'According to <span style="font-size: 25px;"><a href="{link}">{text}</a></span>, Netflix is the most popular among all streaming platforms while Prime comes second.'
st.write(f'<h1 style="font-size:25px;">{message}</h1>', unsafe_allow_html=True)

with st.container():
    components.iframe("https://public.tableau.com/views/Introduction_16816994091380/Dashboard1?:language=en-US&publish=yes&:display_count=n&:showVizHome=no&:embed=true",
                   height=550) 

st.subheader('Question at hand')

message ='''While content quantity offered by a platform is crucial for its popularity and Amazon Prime puts in a lot of effort in gathering content, why is it still not as popular as Netflix? 
            This shows that popularity is by and large attributed to the content quality. 
            We need to determine how to make content that will gain popularity? 
            We are certain many producers have been thinking about this question.'''
st.write(f'<h1 style="font-size:25px;">{message}</h1>', unsafe_allow_html=True)