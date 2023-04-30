# Libraries
import streamlit as st
import pandas as pd
import numpy as np

from sklearn import preprocessing
# Page Config
st.set_page_config(page_title='RECOMMENDATION', page_icon=':bar_chart:', layout='wide')

def our_insights():
    st.title('INSIGHTS')

    message = "Important insights for reference to users using the tool below:"
    st.write(f'<h1 style="font-size:30px;">{message}</h1>', unsafe_allow_html=True)

    message = "Depending on whether the user wants to create a movie or show, the table below shows the optimal settings:"
    st.write(f'<h1 style="font-size:18px;">{message}</h1>', unsafe_allow_html=True)

    table_data = [
        ["", "Age Certification", "Runtime", "Genres"],
        ["Shows", "TV-Y7", "128 min", "scifi, action, fantasy"],
        ["Movies", "PG-13", "208 min", "fantasy, animation, scifi"],
    ]

    df = pd.DataFrame(table_data[1:], columns=table_data[0], index=None)
    df = df.set_index("")

    table_style = [
    {"selector": "table", "props": [("width", "50px"), ("font-size", "12px")]}
    ]

    c1, c2 = st.columns(2)
    c1.table(df)

    message = '''\
    <div style="font-size: 18px;">
        <div>*Note:</div>
        <div>On average, considering all genres, actor-director combinations do not have a high PIC, therefore, for recommendations, select the combination based on other factors (genre, budget, type).</div>
        <div>Please experiment with the tool below to get a recommendation.</div>
        <div>Navigate to previous pages for a deeper analysis if required.</div>
    </div>
    '''

    st.write(f'{message}', unsafe_allow_html=True)

def get_recommendations():
    st.markdown(f'<h1 style=";font-size:48px;">{"RECOMMENDATION"}</h1>', unsafe_allow_html=True)
    df =  pd.read_csv('data/titles_all.csv')
    df = df.rename(columns={
        'genres': 'Genre',
        'type': 'Type',
        'age_certification': 'Age Certification',
        'runtime': 'Runtime',
        'platform': 'Platform'
    })
    df = df.drop(columns=['Unnamed: 0', 'description', 'country_code', 'freqword', 'wordcount'])

    # init a session state
    if 'selected_attributes' not in st.session_state:
        st.session_state.selected_attributes = []

    # Define a dictionary of available attributes and their corresponding selectors
    all_attributes = {
        'Content Type': {
            'df_column': 'Type', # the column name in the dataframe
            'options': df['Type'].dropna().unique().tolist(),
        },
        'Platform': {
            'df_column': 'Platform', # the column name in the dataframe
            'options': df['Platform'].dropna().unique().tolist(),
        },
        'Age Certification': { 
            'df_column': 'Age Certification', # the column name in the dataframe
            'options': df['Age Certification'].dropna().unique().tolist(),
        },
        'Genre': {
            'df_column': 'Genre', # the column name in the dataframe
            'options': df['Genre'].dropna().unique().tolist(),
        },
        'Runtime': {
            'df_column': 'Runtime', # the column name in the dataframe
            'min': int(df['Runtime'].min()),
            'max': int(df['Runtime'].max()),
            'value': (int(df['Runtime'].min()), int(df['Runtime'].max())),
        },
    }

    available_attributes = [k for k,v in all_attributes.items() if not k in [kv[0] for kv in st.session_state.selected_attributes]]

    att_col, add_col = st.columns([4,1])
    with att_col:
        # Create a selectbox to allow the user to choose an attribute
        selected_attribute = st.selectbox('Select Attributes For Filter', available_attributes,help='Select an attribute to filter the data')
    with add_col:
        # Create an add button to add the selected attribute to the filter list
        if st.button('Add', use_container_width=True,):   
            if selected_attribute in available_attributes: 
                if 'options' in all_attributes[selected_attribute]:
                    all_attributes[selected_attribute]['value'] = [all_attributes[selected_attribute]['options'][0]]
                st.session_state.selected_attributes.append((selected_attribute, all_attributes[selected_attribute]))
                st.experimental_rerun()


    filtered = df.drop(columns=['production_countries', 'id', 'release_year']).copy()
    filtered = filtered.rename(columns={'pic':'Score', 'title':'Name'})
    for attribute, value in st.session_state.selected_attributes:
        df_column = value['df_column']
        if 'options' in value:
            if len(value['value']) == 0:
                continue
            filtered = filtered[filtered[df_column].isin(value['value'])]
        else:
            filtered = filtered[(filtered[df_column] >= value['value'][0]) & (filtered[df_column] <= value['value'][1])]
            
    filtered = filtered.sort_values(by=['Score'], ascending=False)
    filtered = filtered.reset_index(drop=True)
    st.markdown(f'<h2 style=";font-size:48px;">{"Top 5 Recommendations"}</h2>', unsafe_allow_html=True)
    st.table(filtered.head(5))

    # Display the filter list
    for idx,(attribute,value) in enumerate(st.session_state.selected_attributes):
        att_value = all_attributes[attribute]
        select_col, delete_col = st.columns([4,1])
        new_value = value.copy()
        
        if 'options' in value:
            sopts , svalue = value['options'],  value['value']
            with select_col:
                ovalue = st.multiselect(f'Select for {attribute}', sopts, default=svalue,key = attribute)
        else:
            smin , smax, svalue =value['min'], value['max'], value['value']
            with select_col:
                ovalue = st.slider(f'Range for {attribute}', smin , smax, svalue,key = attribute)
        with delete_col:
            if st.button('Delete', key=attribute+'delete', use_container_width=True,):
                st.session_state.selected_attributes.remove((attribute, value))
                st.experimental_rerun()
                
        if ovalue != value['value']:
            new_value['value'] = ovalue        
            st.session_state.selected_attributes[idx] = (attribute, new_value)
            st.experimental_rerun()

our_insights()
get_recommendations()