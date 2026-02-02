import os
ICONOS_ESTADO = {
    "Sí": "assets/images/SI.svg",
    "No": "assets/images/NO.svg",
    None: "assets/images/NA.svg"
}

def icono_estado(valor):
    return ICONOS_ESTADO.get(valor, "assets/images/na.png")


def imagen(project_id: int) -> str:
    """
    Devuelve la ruta de la imagen asociada a un proyecto dado su ID.
    Si no existe una imagen específica para el proyecto, devuelve la ruta de una imagen por defecto.

    :param project_id: ID del proyecto
    :return: Ruta de la imagen del proyecto
    """
    ruta_base = "assets/images/proyects/"
    ruta_imagen = f"{ruta_base}{project_id}.jpg"
    ruta_default = f"{ruta_base}default.jpeg"

    if os.path.exists(ruta_imagen):
        return ruta_imagen
    else:
        return ruta_default
    

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
    import streamlit as st

    st.markdown("### Estado del proyecto")

    for label, column in REQUISITOS_PROYECTO:
        estado = project_data[column]

        col1, col2 = st.columns([4, 1])
        col1.write(label)
        col2.image(get_status_icon(estado), width=22)

def get_status_icon(status):
    """
    Devuelve la ruta del icono correspondiente al estado dado.

    :param status: Estado del requisito (Sí, No, None)
    :return: Ruta del icono correspondiente
    """
    return ICONOS_ESTADO.get(status, "assets/images/NA.svg")


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
    import streamlit as st

    for ind in INDICADORES:
        st.image(ind["icon"], width=50)
        st.markdown(f"**{ind['label']}**")
        st.markdown(f"### {project_data[ind['column']]}")
        st.divider()
