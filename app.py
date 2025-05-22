import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header(
    'Análisis de datos de anuncios de venta de coches en Estados Unidos')

file_path = 'vehicles_us.csv'

car_data = pd.read_csv(file_path)


hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)


scatt_button = st.checkbox('Construir gráfico de dispersión')
if scatt_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
