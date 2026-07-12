import streamlit as st
import math

# 1. Configuración de página ancha (Layout wide) para diseño profesional
st.set_page_config(page_title="KeyzCAD Structure", page_icon="🔑", layout="wide")

# 👁️ INYECCIÓN DE CSS: Mantenemos la paleta KeyzCAD Pro
st.markdown("""
    <style>
        /* Fondo de la app principal (Oscuro profundo) */
        .stApp {
            background-color: #0d0d11;
            color: #f0f0f5;
        }
        
        /* Fondo del menú lateral (Degradado morado Keyz) */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1f0d3d 0%, #0a0414 100%);
            border-right: 1px solid #3d1f75;
        }
        
        /* Estilo para los títulos principales */
        h1, h2, h3 {
            color: #b380ff !important;
            font-family: 'sans-serif';
        }
        
        /* Estilo para las etiquetas de los botones de navegación */
        .stRadio label {
            color: #d1b3ff !important;
            font-size: 16px !important;
        }
    </style>
""", unsafe_allow_html=True)

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

# --- NUEVO: IMAGEN DE LOGO EN LA BARRA LATERAL ---
# Puse un icono técnico de una casa/llave temporal. Cuando tengas tu logo, pones su nombre de archivo aquí (ej: "mi_logo.png")
URL_DEL_LOGO = "https://cdn-icons-png.flaticon.com/512/609/609803.png"

st.sidebar.image(URL_DEL_LOGO, use_container_width=True)
st.sidebar.markdown("<h2 style='text-align: center; color: #cc99ff; font-size: 26px; margin-top: 5px; margin-bottom: 0px;'>KeyzCAD Pro</h2>", unsafe_allow_html=True)
st.sidebar.write("---")

# 2. Menú de Navegación en la Barra Lateral
seccion_activa = st.sidebar.radio(
    "🧭 Navegación:",
    ["Inicio", "KeyzCAD Simulador", "Sustento Científico y Normas"]
)

# -------------------------------------------------------------------
# SECCIÓN 1: INICIO (El Problema, Objetivos y Qué es el Software)
# -------------------------------------------------------------------
if seccion_activa == "Inicio":
    st.title("🔑 KeyzCAD Structure")
    st.subheader("Optimización de Techos Bioclimáticos - FENCYT 2026")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### ❓ ¿Cuál es el problema?")
        st.info(
            "En regiones amazónico-andinas y pluviales del Perú, la autoconstrucción informal "
            "diseña techos basados en aproximaciones empíricas ('al ojo'). Ante el cambio climático, "
            "las lluvias torrenciales atípicas superan los límites tradicionales, provocando fallas "
            "estructurales, filtraciones severas e inundaciones por pendientes insuficientes o aleros muy cortos."
        )
        
        st.markdown("### 🎯 ¿Qué buscamos solucionar?")
        st.write(
            "Buscamos **democratizar el acceso al diseño técnico preventivo**. Esta herramienta automatiza "
            "los cálculos geométricos y estructurales que un constructor local necesita, garantizando que cada "
            "techo responda con precisión matemática a los factores de riesgo meteorológico reales de su entorno."
        )
        
        st.markdown("### 💻 ¿De qué trata el software?")
        st.write(
            "**KeyzCAD Structure** es un entorno informático de simulación que procesa las dimensiones espaciales "
            "deseadas para una vivienda y las contrasta con una base de datos climática geo-referenciada. El sistema "
            "determina al instante alturas críticas, áreas inclinadas exactas, presupuestos aproximados y "
            "materiales alternativos eco-amigables de bajo impacto térmico."
        )
    
    with col2:
        st.markdown("### 🛠️ Ficha del Entorno")
        st.success("**Desarrollo:** Python 3\n\n**Framework:** Streamlit Web\n\n**Área:** Tecnología e Innovación")

# -------------------------------------------------------------------
# SECCIÓN 2: SIMULADOR (Tus cálculos y panel interactivo)
# -------------------------------------------------------------------
elif seccion_activa == "KeyzCAD Simulador":
    st.title("📊 Panel de Simulación y Modelamiento Estructural")
    
    st.sidebar.write("---")
    st.sidebar.header("⚙️ Configuración")
    ciudad = st.sidebar.selectbox("Selecciona la localidad:", list(datos_peru.keys()))
    ancho = st.sidebar.slider("Ancho de la casa (metros):", 3.0, 15.0, 6.0, 0.5)
    largo = st.sidebar.slider("Largo de la casa (metros):", 4.0, 20.0, 8.0, 0.5)

    info = datos_peru[ciudad]

    mitad_ancho = ancho / 2
    angulo_rad = math.radians(info["angulo_ideal"])
    altura_centro = mitad_ancho * math.tan(angulo_rad)
    area_inclinada = (ancho * largo) / math.cos(angulo_rad)
    cantidad_calaminas = math.ceil(area_inclinada / 1.44)
    costo_total = area_inclinada * info["costo_m2_soles"]

    st.markdown(f"### 📍 Localidad Activa: {ciudad} | `Datos: {info['estacion']}`")
    st.markdown(f"**Clasificación de Entorno:** *{info['clima']}*")
    st.write("---")

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric(label="📐 Ángulo Recomendado", value=f"{info['angulo_ideal']}°")
    with col_m2:
        st.metric(label="⬆️ Altura Central (Caballete)", value=f"{round(altura_centro, 2)} m")
    with col_m3:
        st.metric(label="↔️ Alero Mínimo Protector", value=f"{info['alero_metros']} m")
    with col_m4:
        st.metric(label="📐 Área Real del Techo", value=f"{round(area_inclinada, 2)} m²")

    st.write("---")

    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.subheader("🌱 Material Ecológico Sugerido")
        st.info(info["material_eco"])
        
    with col_inf2:
        st.subheader("💰 Presupuesto Estimado y Logística")
        st.success(f"**Costo Estimado Materiales:** S/. {round(costo_total, 2)} Soles")
        st.warning(f"**Volumen Comercial:** Requiere aprox. **{cantidad_calaminas}** planchas de calamina estándar.")

# -------------------------------------------------------------------
# SECCIÓN 3: SUSTENTO (Tus escudos de defensa científica)
# -------------------------------------------------------------------
elif seccion_activa == "Sustento Científico y Normas":
    st.title("📚 Sustento Técnico y Marco Normativo")
    
    st.markdown("### 🏢 1. Reglamento Nacional de Edificaciones (RNE)")
    st.write(
        "Los ángulos de inclinación asignados en el diccionario de datos responden a las exigencias de la **Norma Técnica E.080**..."
    )
