"""
Utilidades para el mapeo de proyectos a imágenes e iconos.
"""

# Libraries
import os
import streamlit as st
import base64


# Load image as base64
def load_image_64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Imagenes de proyectos
def imagen_proyecto(project_id):
    """
    Devuelve la ruta de la imagen asociada a un proyecto dado su ID.
    Si no existe una imagen específica para el proyecto, devuelve la ruta de una imagen por defecto.
    """
    ruta_base = "assets/images/proyects/"
    ruta_imagen = f"{ruta_base}{project_id}.jpg"
    ruta_default = f"{ruta_base}default.png"

    if os.path.exists(ruta_imagen):
        return ruta_imagen
    else:
        return ruta_default



# Iconos de indicadores
INDICADORES = [
    {
        "label": "Multiplicador del empleo",
        "column": "multiplicador de empleo",
        "icon": "assets/images/empleo.svg"
    },
    {
        "label": "Multiplicador del producto",
        "column": "multiplicador de producto",
        "icon": "assets/images/producto.svg"
    },
    {
        "label": "Beneficiarios directos",
        "column": "beneficiarios directos",
        "icon": "assets/images/beneficio.svg"
    },
]
def render_indicadores(project_data):
    for ind in INDICADORES:
        # Convertir a base64
        icon_base64 = load_image_64(ind['icon'])

        # Imagen centrada y más grande
        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="data:image/svg+xml;base64,{icon_base64}" width="100">
            </div>
            """,
            unsafe_allow_html=True
        )
        # Label en negrita, centrado
        st.markdown(
            f"<div style='text-align:center;'><strong>{ind['label']}</strong></div>",
            unsafe_allow_html=True
        )
        # Valor con estilo h3, centrado y color definido
        st.markdown(
            f"<h3 style='color:#262C60; text-align:center;'>{project_data[ind['column']]}</h3>",
            unsafe_allow_html=True
        )
        st.divider()



# Iconos de estado
ICONOS_ESTADO = {
    "Sí": "assets/images/SI.svg",
    "No": "assets/images/NO.svg",
    None: "assets/images/NA.svg"
}
def icono_estado(valor):
    return ICONOS_ESTADO.get(valor, "assets/images/na.png")

REQUISITOS_PROYECTO = [
    ("Titularidad de predios", "titularidad_predios"),
    ("Norma urbana", "norma_urbana"),
    ("Servicios públicos", "servicios_publicos"),
    ("Estudios y diseños", "estudios_y_disenos"),
    ("Operador definido", "operador_definido"),
    ("Plan de mantenimiento", "plan_mantenimiento"),
    ("Consulta con comunidad", "consulta_comunidad"),
    ("Licencia de construcción", "licencia_construccion"),
    ("Licencia ambiental", "licencia_ambiental"),
    ("Ocupación de cauce", "ocupacion_cauce"),
    ("Aprovechamiento forestal", "aprovechamiento_forestal"),
    ("Plan de manejo de tránsito", "plan_manejo_transito"),
    ("Intervención espacio público", "intervencion_espacio_publico"),
    ("Fuente identificada", "fuente_identificada"),
    ("CDP", "cdp"),
]
def render_tabla_progreso(project_data):
    st.markdown(
        f"<h3 style='color:#262C60;'> Estado </h3>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([4, 1])
    col1.write("**Entidad**")
    col2.write(project_data['Entidad que impulsa'])
    for label, column in REQUISITOS_PROYECTO:
        estado = project_data[column]
        col1.write(label)
        col2.image(get_status_icon(estado), width=22)

def get_status_icon(status):
    """
    Devuelve la ruta del icono correspondiente al estado dado.

    :param status: Estado del requisito (Sí, No, None)
    :return: Ruta del icono correspondiente
    """
    return ICONOS_ESTADO.get(status, "assets/images/NA.svg")


