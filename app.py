import pandas as pd
import streamlit as st
from utils.mapping import (
    imagen,
    render_tabla_progreso,
    render_indicadores
)

df = pd.read_excel("data/proyectos_ficticios_dashboard.xlsx")

st.title("Dashboard de Proyectos")

opciones = ["— Listado de proyectos —"] + df["ID"].tolist()

proyecto_id = st.selectbox(
    "Selecciona un proyecto",
    opciones,
    format_func=lambda x: (
        "— Listado de proyectos —"
        if isinstance(x, str)
        else df.loc[df["ID"] == x, "nombre_proyecto"].values[0]
    )
)

if isinstance(proyecto_id, str):
    st.info("Selecciona un proyecto para visualizar la información.")
    st.stop()

data = df[df["ID"] == proyecto_id].iloc[0]

col_info, col_estado = st.columns([2, 3])

with col_info:
    st.subheader(data["nombre_proyecto"])

    image_path = imagen(proyecto_id)
    st.image(image_path, use_container_width=True)

    st.markdown("### Próximos pasos")
    st.write(data["proximos_pasos"])

with col_estado:
    col_indicadores, col_tabla = st.columns([1, 2])

    with col_indicadores:
        render_indicadores(data)

    with col_tabla:
        render_tabla_progreso(data)
