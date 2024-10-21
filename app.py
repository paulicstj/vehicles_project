import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') 

st.header('Visualización de datos de vehículos en venta')

hist_button= st.button('Construir histograma.')

if hist_button:
    st.write('Creación de un histograma.')

    fig= px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width= True)

scat_button= st.button('Construir gráfico de dispersión')

if scat_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de anuncios de venta de coches')

    fig_scat= px.scatter(car_data, x="odometer")
    st.plotly_chart (fig_scat, use_container_width= True)

condition= car_data.groupby('condition')['price'].mean()
condition_df= condition.reset_index()

condition_graph= st.checkbox('Creación de un gráfico de barras.')
if condition_graph:
    st.write('Creación de un gráfico que muestra la condición del vehículo vs el precio de venta.')

    fig_bar= px.bar(condition_df, x='condition', y='price')
    st.plotly_chart(fig_bar, use_container_width= True)