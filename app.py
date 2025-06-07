
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de Vehículos Usados", layout="wide")

st.title("🚗 Dashboard de Vehículos Usados en Estados Unidos")
st.markdown("""
Bienvenido al visualizador de datos de vehículos usados. 
Aquí puedes explorar información detallada sobre distintas marcas, modelos, precios y condiciones de vehículos listados en EE.UU.

Usa los filtros y visualizaciones para analizar el mercado de autos usados y descubrir tendencias importantes.
""")

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Mostrar datos

st.subheader("Vista previa de los datos")
st.dataframe(df.head(10))

# Histograma del precio
st.subheader("Distribución de precios de vehículos")
fig = px.histogram(df, x='price', nbins=50, title='Histograma de precios de vehículos usados')
fig.update_layout(xaxis_title='Precio (USD)', yaxis_title='Cantidad de vehículos')
st.plotly_chart(fig, use_container_width=True)


# Gráfico de dispersión: Precio vs Año del modelo
st.subheader("Relación entre el precio y el año del vehículo")
fig2 = px.scatter(df, x='model_year', y='price',
                  title='Precio de vehículos según el año del modelo',
                  labels={'model_year': 'Año del Modelo', 'price': 'Precio (USD)'},
                  opacity=0.6)
fig2.update_layout(xaxis_title='Año del Modelo', yaxis_title='Precio (USD)')
st.plotly_chart(fig2, use_container_width=True)




# Histograma por marca seleccionada
st.subheader("Distribución de modelos por marca seleccionada")
marcas = df['manufacturer'].dropna().unique()
marca_seleccionada = st.selectbox("Selecciona una marca:", sorted(marcas))

df_filtrado = df[df['manufacturer'] == marca_seleccionada]
fig4 = px.histogram(df_filtrado, x='model', color='condition',
                    title=f'Modelos de vehículos para la marca: {marca_seleccionada}',
                    labels={'model': 'Modelo', 'condition': 'Condición'},
                    barmode='group')
fig4.update_layout(xaxis_title='Modelo', yaxis_title='Cantidad de vehículos')
st.plotly_chart(fig4, use_container_width=True)