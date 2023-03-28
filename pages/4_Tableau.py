# Libraries
import streamlit as st
import streamlit.components.v1 as components


# Config
st.set_page_config(page_title='TABLEAU', page_icon=':bar_chart:', layout='wide')


# Title
st.title('💸 TABLEAU')

with st.container():
    components.iframe("https://public.tableau.com/views/Paddy_16799687230860/Story1?:language=en-US&publish=yes&:display_count=n&:showVizHome=no&:embed=true",
                   height=1500) 