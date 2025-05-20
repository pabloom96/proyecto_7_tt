import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(
    'C:\\Users\\usuario\\Desktop\\tripleten_bootcamp_data_scientist\\sprint7-prueba\\proyecto\\proyecto_7_tt\\vehicles_us.csv')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

st.header(
    'Análisis de datos de anuncios de venta de coches en Estados Unidos')
