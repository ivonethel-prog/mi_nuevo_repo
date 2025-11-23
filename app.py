import streamlit as st
import pandas as pd
import plotly.express as px

datos = pd.read_csv('vehicles_us.csv')
st.header('Datos de vehículos')
st.dataframe(datos.head())

hist_button = st.button('Construir histogram')
if hist_button:
    st.write("Creacion de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(datos, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    

