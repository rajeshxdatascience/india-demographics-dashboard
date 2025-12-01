import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:\Users\rajes\CampusXDSMP1.0\PlotlyProject\india.csv')

st.title("India District Demographics & Development Dashboard")


state_list = list(df['State'].unique())
state_list.insert(0,'Overall India')

st.set_page_config(layout='wide')

st.sidebar.title('India District Demographics & Development Dashboard')

selected_state = st.sidebar.selectbox('Select a state',state_list)
primary = st.sidebar.selectbox('Select Primary Paramter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Paramter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text("Size represents the primary parameter")
    st.text("Color represents the secondary parameter")

    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',size=primary,color=primary,color_continuous_scale='Turbo',
                        zoom=3.6,mapbox_style='carto-positron',width=1200,height=700,hover_name='District',hover_data={
                            primary: ':.2f',
                            secondary: ':.2f'
                        })
        
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for satte
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',size=primary,color=secondary,color_continuous_scale='Turbo',
                        zoom=6,mapbox_style='carto-positron',width=1200,height=700,hover_name='District',hover_data={
                            primary: ':.2f',
                            secondary: ':.2f'
                        })
        
        st.plotly_chart(fig,use_container_width=True)