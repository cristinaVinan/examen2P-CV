import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from collections import namedtuple
from math import acos, asin, cos, sin, atan, sqrt, radians, degrees

#Título
st.title("Historial de producción del Campo Volve")

# Descripción
st.markdown("Información relacionada a una producción de petróleo y gas del campo Volve")

#Imagen en página principal
image = Image.open("Resources/producción.jpg")
st.image(image, width=100, use_column_width=True)

#Menú
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "clipboard2-data", "bar-chart-fill"])
#Codigo para opciones
# def data(dataframe):
#     st.subheader("**View dataframe**")
#     st.write(dataframe.head())
#     st.subheader("**Historia de producción**")
#     st.write(dataframe.describe())

# if file:
#     df = pd.read_csv(file)
#
#     if options == "Data":
#         data(df)

# def plots(dataframe):
#     st.subheader("Visualize the 3D trajectory of a well")
#     Volo_vs_t= st.selectbox("Choose DispNS", dataframe.columns)
#     Volg_vs_t = st.selectbox("Choose DispEW", dataframe.columns)
#     Volg_Volw_vs_t = st.selectbox("Choose tvd", dataframe.columns)
#     Volo
#     fig = px.line_3d(dataframe, x, y, z)
#     st.plotly_chart(fig)

