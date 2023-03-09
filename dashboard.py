# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:29:39 2023

@author: vasee
"""

#import relevant libraries 
import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime
###############################################################################

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://docs.streamlit.io/streamlit-cloud/troubleshooting',
         'Report a bug': "https://github.com/streamlit/streamlit/issues",
         'About': "# Espotrs industry analysis!"
     }
 )

# loading datasets and some reengineering
def load_data():
    df = pd.read_csv(r'C:/Users/vasee/Desktop/stats/df/HomeC.csv')

    return df

df = load_data()
df = df.drop(503910)
df['cloudCover'].replace(['cloudCover'], method='bfill', inplace=True)
df['cloudCover'] = df['cloudCover'].astype('float')
df.columns = [i.replace(' [kW]', '') for i in df.columns]
df.time=pd.DatetimeIndex(pd.date_range('2016-01-01 05:00', periods=len(df),  freq='min'))
df.set_index('time',inplace=True)

###############################################################################

#Data reengineering









###############################################################################
#Start building Streamlit App

st.sidebar.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/pic.png?raw=true',use_column_width = 'always')
st.sidebar.header('Energy Consuption')
st.sidebar.markdown('Analysing energy use of an household with weather information')


menu = st.sidebar.radio(
    "Menu:",
    ('Energy use','Weather Info','Model evaluations'),
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)




   #game_details()
if menu == 'Energy use':
    

    st.title('ANALYSIS')
    st.text("")
    
    scale = st.radio('',('Hourly','Daily','Weekly','Monthly'),key='data')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    cols = ['House overall', 'Dishwasher', 'Home office', 'Fridge', 'Wine cellar',
           'Garage door', 'Barn', 'Well', 'Microwave', 'Living room', 'Solar',
           'Furnace','Kitchen']
    
    if scale=='Hourly':
        scaled_df = df.resample('h').mean()
    elif scale == 'Daily':
        scaled_df = df.resample('d').mean()
    elif scale == 'Weekly':
        scaled_df = df.resample('w').mean()
    else:
        scaled_df = df.resample('m').mean()
     
    #Line chart
    col1,col2 = st.columns(2)
    with col1:
        
        atrbt = st.selectbox('', cols,key = 'line')
        st.header('Chart') 
        fig1 = px.line(scaled_df, x=scaled_df.index, y=atrbt)
        fig1.update_layout(hovermode="x unified")
        st.plotly_chart(fig1)
    
    with col2:
        #AVg Use
        atrbt3 = st.selectbox('', cols,key="avg")
        st.header('Average use')
        if scale=='Hourly':
            avg_df = scaled_df.groupby(scaled_df.index.hour).mean()
            fig3 = px.line(avg_df,x=avg_df.index, y= atrbt3)
            st.plotly_chart(fig3)
        elif scale == 'Daily':
            avg_df = scaled_df.groupby(scaled_df.index.day_of_week).mean()
            fig3 = px.line(avg_df,x=avg_df.index, y= atrbt3)
            st.plotly_chart(fig3)
        elif scale == 'Weekly':
           avg_df = scaled_df.groupby(scaled_df.index.week).mean()
           fig3 = px.line(avg_df,x=avg_df.index, y= atrbt3)
           st.plotly_chart(fig3)
        else:
            avg_df = scaled_df.groupby(scaled_df.index.month).mean()
            fig3 = px.line(avg_df,x=avg_df.index, y= atrbt3)
            st.plotly_chart(fig3)
        
    #boxplot
    atrbt2 = st.selectbox('', cols,key="bar")
    st.header('Boxplot')
    if scale=='Hourly':
        fig, ax = plt.subplots(figsize=(20, 6))
        sns.boxplot(data=df, x=df.index.hour, y= atrbt2)
        st.pyplot(fig)
    elif scale == 'Daily':
        fig, ax = plt.subplots(figsize=(20, 6))
        sns.boxplot(data=df, x=df.index.day_of_week, y= atrbt2)
        st.pyplot(fig)
    elif scale == 'Weekly':
       fig, ax = plt.subplots(figsize=(20, 6))
       sns.boxplot(data=df, x=df.index.week, y= atrbt2)
       st.pyplot(fig)
    else:
        fig, ax = plt.subplots(figsize=(20, 6))
        sns.boxplot(data=df, x=df.index.month, y= atrbt2)
        st.pyplot(fig)
        
        
        
       





#Weather info

elif menu == 'Weather Info':
    
    st.title('WEATHER INFORMATION')
    st.text("")
    
    scale2 = st.radio('',('Hourly','Daily','Weekly','Monthly'),key='weather')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    weather = ['temperature', 'humidity', 'visibility', 'pressure', 'windSpeed','cloudCover', 'windBearing', 'precipIntensity']
    if scale2=='Hourly':
        scaled_df2 = df.resample('h').mean()
    elif scale2 == 'Daily':
        scaled_df2 = df.resample('d').mean()
    elif scale2 == 'Weekly':
        scaled_df2 = df.resample('w').mean()
    else:
        scaled_df2 = df.resample('m').mean()
     
        
     
    #LIne  
    atrbt4 = st.selectbox('', weather,key = 'wline')
    st.header('Chart') 
    fig4 = px.line(scaled_df2, x=scaled_df2.index, y=atrbt4,width=1300,height=650)
    fig4.update_layout(hovermode="x unified")
    st.plotly_chart(fig4)
    
    
    #boxplot
    atrbt5 = st.selectbox('', weather,key="wbar")
    st.header('Boxplot')
    if scale2=='Hourly':
        fig, ax = plt.subplots(figsize=(20, 8))
        sns.boxplot(data=df, x=df.index.hour, y= atrbt5)
        st.pyplot(fig)
    elif scale2 == 'Daily':
        fig, ax = plt.subplots(figsize=(20, 8))
        sns.boxplot(data=df, x=df.index.day_of_week, y= atrbt5)
        st.pyplot(fig)
    elif scale2 == 'Weekly':
       fig, ax = plt.subplots(figsize=(20, 8))
       sns.boxplot(data=df, x=df.index.week, y= atrbt5)
       st.pyplot(fig)
    else:
        fig, ax = plt.subplots(figsize=(20, 8))
        sns.boxplot(data=df, x=df.index.month, y= atrbt5)
        st.pyplot(fig)
        
        
        
    #AVg Use
    atrbt6 = st.selectbox('', weather,key="wavg")
    st.header('Average use')
    if scale2=='Hourly':
        avg_df = scaled_df2.groupby(scaled_df2.index.hour).mean()
        fig5 = px.line(avg_df,x=avg_df.index, y= atrbt6,width=1300,height=650)
        st.plotly_chart(fig5)
    elif scale2 == 'Daily':
        avg_df = scaled_df2.groupby(scaled_df2.index.day_of_week).mean()
        fig5 = px.line(avg_df,x=avg_df.index, y= atrbt6,width=1300,height=650)
        st.plotly_chart(fig5)
    elif scale2 == 'Weekly':
       avg_df = scaled_df2.groupby(scaled_df2.index.week).mean()
       fig5 = px.line(avg_df,x=avg_df.index, y= atrbt6,width=1300,height=650)
       st.plotly_chart(fig5)
    else:
        avg_df = scaled_df2.groupby(scaled_df2.index.month).mean()
        fig5 = px.line(avg_df,x=avg_df.index, y= atrbt6,width=1300,height=650)
        st.plotly_chart(fig5)   
        


else:
    st.title('BEST MODEL PERFORMANCE')
    st.text("")
    cols2 = ['House overall', 'Dishwasher', 'Home office', 'Fridge', 'Wine cellar',
           'Garage door', 'Barn', 'Well', 'Microwave', 'Living room', 'Solar',
           'Furnace','Kitchen']
    option = st.selectbox(
    "",
    cols2,key ='model')
    col1, col2 = st.columns([2, 1])
    if option == 'House overall':
        
        
        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/1lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error  =  0.02')
            st.write('root mean squared error =  0.03')
            
    elif option == 'Dishwasher':
        
        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/2sx.png?raw=true')
        with col2:
            st.header('SARIMAX')
            st.write('mean absolure error is =  0.23')
            st.write('root mean squared error is =  0.26')
            
            
    elif option == 'Home office':
            
        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/3lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error is =  0.08')
            st.write('root mean squared error is =  0.10')
    
    elif option == 'Fridge':
        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/4lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error =  0.05')
            st.write('root mean squared error =  0.06')
    
    
    elif option == 'Wine cellar':
        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/5lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error =  0.01')
            st.write('root mean squared error =  0.01')
            
    elif option == 'Garage door':

        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/6xgb.png?raw=true')
        with col2:
            st.header('XGBoost')
            st.write('mean absolure error =  0.06')
            st.write('root mean squared error =  0.09')
    
    elif option == 'Barn':

        with col1:
           st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/7ro_srma.png?raw=true')
        with col2:
            st.header('SARIMA with RFO')
            st.write('mean absolure error =  0.06')
            st.write('root mean squared error is =  0.15')
            
    elif option == 'Well':

        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/8lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error =  0.08')
            st.write('root mean squared error =  0.10')
            
            
    elif option == 'Microwave':

        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/9xgb.png?raw=true')
        with col2:
            st.header('XGBoost')
            st.write('mean absolure error =  0.11')
            st.write('root mean squared error =  0.13')
            
    elif option == 'Living room':

        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/10prophet.png?raw=true')
        with col2:
            st.header('Prophet')
            st.write('mean absolure error =  0.14')
            st.write('root mean squared error =  0.18')
            
    elif option == 'Solar':

        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/11lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error =  0.14')
            st.write('root mean squared error =  0.17')
            
            
    elif option == 'Furnace':
        
        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/12lstm.png?raw=true')
        with col2:
            st.header('LSTM')
            st.write('mean absolure error =  0.03')
            st.write('root mean squared error =  0.03')
            
            
    else :

        with col1:
            st.image('https://github.com/Ne04ever/Electricity-prediction/blob/main/13prophet.png?raw=true')
        with col2:
            st.header('Prophet')
            st.write('mean absolure error =  0.11')
            st.write('root mean squared error =  0.18')
            
            
        
       