# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import streamlit.components.v1 as components

# Page Config
st.set_page_config(page_title='INTRODUCTION', page_icon=':bar_chart:', layout='wide')

st.markdown(f'<h1 style=";font-size:48px;">{"INTRODUCTION"}</h1>', unsafe_allow_html=True)

with st.container():
    components.iframe("https://public.tableau.com/views/Introduction_16816994091380/Dashboard1?:language=en-US&publish=yes&:display_count=n&:showVizHome=no&:embed=true",
                   height=1800) 
