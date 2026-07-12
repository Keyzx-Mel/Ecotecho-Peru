import streamlit as st
import math

# Base de datos cargada en la aplicación web
datos_peru = {
    "Nueva Cajamarca": {
        "estacion": "Estación Naranjillo (Rioja)", "clima": "Selva Alta / Lluvias Torrenciales",
        "angulo_ideal": 35, "alero_metros": 1.2, "costo_m2_soles": 48,
        "material_eco": "Madera local, caña brava con barro o tejas artesanales"
    },
    "Tarapoto": {
        "estacion": "Estación El Porvenir (San Martín)", "clima": "Selva Alta / Cálido y Lluvioso",
        "angulo_ideal": 40, "alero_metros": 1.3, "costo_m2_soles": 45,
        "material_eco": "Palma de irapay trenzada o bambú local estructurado"
    },
    "Iquitos": {
        "estacion": "Estación Punchana (Loreto)", "clima": "Selva Baja / Lluvias Constantes Todo el Año",
        "angulo_ideal": 45, "alero_metros": 1.5, "costo_m2_soles": 50,
        "material_eco": "Hojas de palma tejidas y columnas de madera Copaiba certificada"
    },
    "Piura": {
        "estacion": "Estación Miraflores (Piura)", "clima": "Costa Desértica / Estacional (Fenómeno El Niño)",
        "angulo_ideal": 25, "alero_metros": 1.0, "costo_m2_soles": 55,
        "material_eco": "Paneles de quincha mejorada o bloques de tierra comprimida (BTC)"
    }
}

# Diseño de la Interfaz Gráfica de la Página Web
st.set_page_config(page_title="EcoTecho Perú", page_icon="🏠", layout="centered")

st.title("🏠 EcoTecho Perú")
st.subheader("Optimización de Techos Bioclimáticos - FENECIT")
st.markdown("Herramienta tecnológica para el diseño sostenible y prevención de riesgos climáticos.")

st.sidebar.header("⚙️ Configuración de la Vivienda")

# 1. Menú desplegable para elegir la ciudad
ciudad = st.sidebar.selectbox("Selecciona la localidad:", list(datos_peru.keys()))

# 2. Barras deslizantes para las dimensiones de la casa
ancho = st.sidebar.slider("Ancho de la casa (metros):", 3.0, 15.0, 6.0, 0.5)
largo = st.sidebar.slider("Largo de la casa (metros):", 4.0, 20.0, 8.0, 0.5)

info = datos_peru[ciudad]

# Cálculos estructurales en tiempo real
mitad_ancho = ancho / 2
angulo_rad = math.radians(info["angulo_ideal"])
altura_centro = mitad_ancho * math.tan(angulo_rad)
area_inclinada = (ancho * largo) / math.cos(angulo_rad)
cantidad_calaminas = math.ceil(area_inclinada / 1.44)
costo_total = area_inclinada * info["costo_m2_soles"]

# Mostrar los resultados organizados en la pantalla principal
st.info(f"📍 *Localidad Activa:* {ciudad} | *Datos:* {info['estacion']}")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="📐 Ángulo del Techo", value=f"{info['angulo_ideal']}°")
    st.metric(label="⬆️ Altura Central (Caballete)", value=f"{round(altura_centro, 2)} m")
with col2:
    st.metric(label="↔️ Alero Protector", value=f"{info['alero_metros']} m")
    st.metric(label="📐 Área del Techo", value=f"{round(area_inclinada, 2)} m²")

st.subheader("🌱 Material Ecológico Recomendado")
st.write(info["material_eco"])

st.subheader("💰 Presupuesto Estimado de la Estructura")
st.success(f"*Costo Materiales Locales:* S/. {round(costo_total, 2)} Soles")
st.warning(f"*Material Comercial:* Se requieren aprox. {cantidad_calaminas} planchas de calamina estándar.")
