import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Visualizador de Vehículos Usados")

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

# Mostrar el dataframe si el usuario marca el checkbox
if st.checkbox("Mostrar datos crudos"):
    st.write(df.head())

# Gráfico de precios por tipo de vehículo
st.subheader("Precio de vehículos por tipo")
fig = px.box(df, x="type", y="price", points="all", title="Distribución de precios por tipo de vehículo")
st.plotly_chart(fig)

# Filtro interactivo por tipo
vehicle_type = st.selectbox("Selecciona un tipo de vehículo", df["type"].dropna().unique())
filtered_df = df[df["type"] == vehicle_type]

# Histograma de año de fabricación para el tipo seleccionado
st.subheader(f"Año de fabricación para tipo '{vehicle_type}'")
fig2 = px.histogram(filtered_df, x="model_year", nbins=20, title="Distribución por año")
st.plotly_chart(fig2)

# Gráfico de precios por año de fabricación para el tipo seleccionado
st.subheader(f"Precio por año de fabricación para tipo '{vehicle_type}'")
fig3 = px.scatter(filtered_df, x="model_year", y="price", title="Precio por año de fabricación")
st.plotly_chart(fig3)


# Título
st.title("Análisis de Vehículos Usados")

# Limpiar datos nulos para evitar errores en la gráfica
df = df.dropna(subset=["price", "model_year"])

# Casilla de verificación
if st.checkbox("Mostrar gráfico de precio vs año del modelo"):
    st.subheader("Precio vs Año del Modelo")
    fig = px.scatter(
        df, 
        x="model_year", 
        y="price", 
        color="type",
        hover_data=["model", "condition"],
        title="Relación entre Precio y Año del Modelo"
    )
    st.plotly_chart(fig)

