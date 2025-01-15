"""Proyecto sprint 7"""

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Llenar valores nulos
car_data['model_year'] = car_data['model_year'].fillna(1900)
car_data['cylinders'] = car_data['cylinders'].fillna(0)
car_data['odometer'] = car_data['odometer'].fillna(-1)
car_data['paint_color'] = car_data['paint_color'].fillna('other')
car_data['is_4wd'] = car_data['is_4wd'].fillna(0)

st.header('Gráficas para mostrar la relación de colores de anuncios de ventas de autos')

hist_button = st.button('Construir histograma') # crear un botón
scatter_checkbox = st.checkbox('Construir dispersión') # crear otro botón

def show_chart(chart):
    """Muestra una gráfica en la página web"""
    st.plotly_chart(chart, use_container_width=True)

if hist_button: # al hacer clic en el botón
    # mensaje
    st.write('Histograma de la cantidad de anuncios por color')

    # histograma
    color_hist = px.histogram(car_data, x='paint_color')

    # mostrar un gráfico Plotly interactivo
    show_chart(color_hist)

if scatter_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfica de dispersión para la relación color/precio de los anuncios')

    # crear un diagrama de dispersión
    color_scatter = px.scatter(car_data, x='paint_color', y='price')

    # mostrar un gráfico Plotly interactivo
    show_chart(color_scatter)
