import pandas as pd
import streamlit as st
import plotly_express as px
from st_aggrid import AgGrid, GridOptionsBuilder

df_vehiculos = pd.read_csv ('vehicles_us.csv')
st.header('VEHICLE DATA')

df_group = df_vehiculos.groupby('model')['price'].sum()
st.dataframe(df_group, use_container_width=True)

hist_button = st.checkbox('build histogram')


if hist_button: # al hacer clic en el botón
       # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(df_vehiculos, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# creacion de boton para grafico de dispersion
disp_button = st.checkbox ('build dispersion')


if disp_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(df_vehiculos, x="odometer", y="price") # crear un gráfico de dispersión

    st.plotly_chart(fig, use_container_width=True)