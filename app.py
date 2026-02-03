import pandas as pd
import streamlit as st
from utils.mapping import (
    load_image_64,
    imagen_proyecto,
    render_tabla_progreso,
    render_indicadores
)

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================

st.set_page_config(
    page_title="Dashboard de Proyectos",
    layout="wide"
)

with open("assets/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# CARGA DE DATOS
# =========================

df = pd.read_excel("data/proyectos_ficticios_dashboard.xlsx")

# =========================
# TÍTULO PRINCIPAL
# =========================

st.markdown(
    f"<h1 style='color:#009f98;'> FICHA DE PROYECTOS PRIORIZADOS</h1>",
    unsafe_allow_html=True
)

# =========================
# SELECTOR DE PROYECTO
# =========================

opciones = ["— Listado de proyectos —"] + df["ID"].tolist()

proyecto_id = st.selectbox(
    "Selecciona un proyecto",
    opciones,
    format_func=lambda x: (
        "Proyectos"
        if isinstance(x, str)
        else df.loc[df["ID"] == x, "nombre_proyecto"].values[0]
    )
)

if isinstance(proyecto_id, str):
    st.info("Selecciona un proyecto para visualizar la información.")
    st.stop()

data = df[df["ID"] == proyecto_id].iloc[0]

# =========================
# CONTENIDO
# =========================
st.divider()
st.markdown(
    f"<h1 style='color:#009f98;'>  {data['nombre_proyecto']} </h1><br>",
    unsafe_allow_html=True
)

col_info, col_estado = st.columns([2, 3])

# Columna de información general
with col_info:
    st.markdown(
        f"<h3 style='color:#262C60;'> Descripción </h3>",
        unsafe_allow_html=True
    )
    st.write(data["descripcion"])

    image_path = imagen_proyecto(proyecto_id)
    st.image(image_path, width=1000)
    
    st.markdown(
        f"<h3 style='color:#262C60;'> Próximos pasos</h3>",
        unsafe_allow_html=True
    )
    st.write(data["proximos_pasos"])


# Columna del estado del proyecto
with col_estado:
    col_indicadores, col_tabla = st.columns([1, 2])

    with col_indicadores:
        render_indicadores(data)

    with col_tabla:
        render_tabla_progreso(data)

logo_base64 = load_image_64("assets/images/LOGO.png")
st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{logo_base64}" width="200">
    </div>
    """,
    unsafe_allow_html=True
)