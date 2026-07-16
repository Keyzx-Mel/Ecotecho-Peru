import streamlit as st
import math
from fpdf import FPDF  # Importamos la librería para crear PDFs

# 1. Configuración de página ancha (Layout wide) para diseño profesional
st.set_page_config(page_title="KeyzCAD Structure", page_icon="🔑", layout="wide")

# 👁️ INYECCIÓN DE CSS: Estilos de la paleta KeyzCAD Pro y mejoras de tarjetas
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

        /* Estilo personalizado para los cuadros de información (Ficha del Entorno) */
        div.stAlert {
            background-color: rgba(31, 13, 61, 0.25) !important;
            color: #f0f0f5 !important;
            border: 1px solid #5a2bb8 !important;
            border-radius: 10px !important;
        }
        
        /* Ajustar los textos dentro de las alertas modificadas */
        div.stAlert p {
            color: #e1ccff !important;
        }

        /* --- CONTENEDOR Y ANIMACIÓN DEL TEXTO DESLIZANTE --- */
        .contenedor-animado {
            height: 50px;
            overflow: hidden;
            margin-top: 10px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
        }

        .texto-estatico {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            margin-right: 10px;
        }

        .caja-palabras {
            height: 45px;
            overflow: hidden;
        }

        .lista-palabras {
            margin: 0;
            padding: 0;
            list-style: none;
            animation: deslizar 9s infinite ease-in-out;
        }

        .lista-palabras li {
            height: 45px;
            font-size: 24px;
            font-weight: bold;
            color: #cc99ff;
            display: flex;
            align-items: center;
        }

        /* El truco de los fotogramas para mover el texto hacia arriba */
        @keyframes deslizar {
            0%, 25% { transform: translateY(0); }
            33%, 58% { transform: translateY(-45px); }
            66%, 91% { transform: translateY(-90px); }
            100% { transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN ADICIONAL: GENERADOR DE REPORTE PDF ---
def generar_pdf(ciudad, ancho, largo, info, altura, area, calaminas, costo, pendiente, angulo_grados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    
    # Encabezado con estética KeyzCAD (Fondo morado oscuro para el título)
    pdf.set_fill_color(31, 13, 61)  # Color #1f0d3d
    pdf.rect(0, 0, 210, 38, 'F')
    
    # Texto del Encabezado
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 10, "KEYZCAD STRUCTURE", ln=True, align="C")
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 5, "Reporte Tecnico de Optimizacion Bioclimatica - FENCYT 2026", ln=True, align="C")
    pdf.ln(15)
    
    # Sección 1: Detalles del Proyecto
    pdf.set_text_color(90, 43, 184) # Morado Keyz
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 8, "1. Datos Generales de la Evaluacion", ln=True)
    pdf.set_draw_color(90, 43, 184)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(4)
    
    pdf.set_text_color(50, 50, 50)
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(90, 7, f"Localidad Seleccionada: {ciudad}", ln=False)
    pdf.cell(90, 7, f"Estacion Referencial: {info['estacion']}", ln=True)
    pdf.cell(90, 7, f"Ancho de la Estructura: {ancho} m", ln=False)
    pdf.cell(90, 7, f"Largo de la Estructura: {largo} m", ln=True)
    pdf.ln(8)
    
    # Sección 2: Diseño Geométrico y Datos Climáticos
    pdf.set_text_color(90, 43, 184)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 8, "2. Analisis Estructural y Climatico", ln=True)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(4)
    
    pdf.set_text_color(50, 50, 50)
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(90, 7, f"Clima de la Zona: {info['clima']}", ln=False)
    pdf.cell(90, 7, f"Pendiente de Diseño: {pendiente}%", ln=True)
    pdf.cell(90, 7, f"Angulo Calculado: {round(angulo_grados, 2)} grados", ln=False)
    pdf.cell(90, 7, f"Altura del Caballete (Central): {round(altura, 2)} m", ln=True)
    pdf.cell(90, 7, f"Alero Minimo Recomendado: {info['alero_metros']} m", ln=False)
    pdf.cell(90, 7, f"Area Inclinada Real de Cobertura: {round(area, 2)} m2", ln=True)
    pdf.ln(8)
    
    # Sección 3: Logística, Materiales y Presupuesto
    pdf.set_text_color(90, 43, 184)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 8, "3. Logistica y Presupuesto Estimado", ln=True)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(4)
    
    pdf.set_text_color(50, 50, 50)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, f"Material Ecologico Alternativo Recomendado:\n{info['material_eco']}")
    pdf.ln(2)
    pdf.cell(90, 7, f"Cantidad de Calaminas Estandar Requeridas: {calaminas} planchas", ln=False)
    pdf.cell(90, 7, f"Presupuesto de Materiales Sugerido: S/. {round(costo, 2)} Soles", ln=True)
    pdf.ln(12)
    
    # Pie de página / Firmas de validación
    pdf.set_text_color(120, 120, 120)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "Calculos estructurales generados algoritmicamente por KeyzCAD Structure v1.0.", ln=True, align="C")
    pdf.cell(0, 5, "Basado en exigencias tecnicas de las Normas RNE E.080 y E.020.", ln=True, align="C")
    
    return bytes(pdf.output())
    
# Base de datos adaptada a las pendientes mínimas requeridas por normativa
datos_peru = {
    "Nueva Cajamarca": {
        "estacion": "Estación Naranjillo (Rioja)", "clima": "Selva Alta / Lluvias Torrenciales",
        "pendiente_porcentaje": 30, "alero_metros": 1.2, "costo_m2_soles": 48,
        "material_eco": "Madera local, caña brava con barro o tejas artesanales"
    },
    "Tarapoto": {
        "estacion": "Estación El Porvenir (San Martín)", "clima": "Selva Alta / Cálido y Lluvioso",
        "pendiente_porcentaje": 30, "alero_metros": 1.3, "costo_m2_soles": 45,
        "material_eco": "Palma de irapay trenzada o bambú local estructurado"
    },
    "Iquitos": {
        "estacion": "Estación Punchana (Loreto)", "clima": "Selva Baja / Lluvias Constantes Todo el Año",
        "pendiente_porcentaje": 30, "alero_metros": 1.5, "costo_m2_soles": 50,
        "material_eco": "Hojas de palma tejidas y columnas de madera Copaiba certificada"
    },
    "Piura": {
        "estacion": "Estación Miraflores (Piura)", "clima": "Costa Desértica / Estacional (Fenómeno El Niño)",
        "pendiente_porcentaje": 15, "alero_metros": 1.0, "costo_m2_soles": 55,
        "material_eco": "Paneles de quincha mejorada o bloques de tierra comprimida (BTC)"
    }
}

# --- IMAGEN DE LOGO EN LA BARRA LATERAL ---
URL_DEL_LOGO = "logo_keyz.png"

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
    
    st.markdown("""
        <div class="contenedor-animado">
            <span class="texto-estatico">Especializado en</span>
            <div class="caja-palabras">
                <ul class="lista-palabras">
                    <li>🌧️ Lluvias Torrenciales</li>
                    <li>🛡️ Prevención de Riesgos</li>
                    <li>💰 Ahorro de Materiales</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
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
        st.info("**🔧 Desarrollo:** Python 3\n\n**📦 Framework:** Streamlit Web\n\n**🧬 Área:** Tecnología e Innovación")

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
    pendiente = info["pendiente_porcentaje"]

    # --- NUEVOS CÁLCULOS MATEMÁTICOS DINÁMICOS ---
    # 1. Distancia horizontal (mitad del ancho para techo a dos aguas)
    distancia_horizontal = ancho / 2
    
    # 2. Altura del Caballete (h) calculada dinámicamente mediante la pendiente en %
    altura_centro = (pendiente * distancia_horizontal) / 100
    
    # 3. Conversión de pendiente a ángulo en radianes y luego a grados sexagesimales
    angulo_rad = math.atan(pendiente / 100)
    angulo_grados = math.degrees(angulo_rad)
    
    # 4. Cálculo del Largo de la Caída (Hipotenusa) usando Pitágoras
    # (Se le suma el alero a la distancia horizontal para una proyección de cobertura real completa)
    dist_con_alero = distancia_horizontal + info["alero_metros"]
    altura_con_alero = (pendiente * dist_con_alero) / 100
    largo_caida = math.sqrt(altura_con_alero**2 + dist_con_alero**2)
    
    # 5. Área Real del Techo multiplicada por las 2 caídas y extendida por los aleros frontales
    area_inclinada = (largo_caida * 2) * (largo + (2 * info["alero_metros"]))
    
    # 6. Presupuesto y materiales basados en el área real
    cantidad_calaminas = math.ceil(area_inclinada / 1.44)
    costo_total = area_inclinada * info["costo_m2_soles"]

    st.markdown(f"### 📍 Localidad Activa: {ciudad} | `Datos: {info['estacion']}`")
    st.markdown(f"**Clasificación de Entorno:** *{info['clima']}*")
    st.write("---")

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric(label="📐 Ángulo Real Calculado", value=f"{round(angulo_grados, 2)}°")
    with col_m2:
        st.metric(label="⬆️ Altura Central (Caballete)", value=f"{round(altura_centro, 2)} m")
    with col_m3:
        st.metric(label="↔️ Alero Mínimo Protector", value=f"{info['alero_metros']} m")
    with col_m4:
        st.metric(label="📐 Área Real de Cobertura", value=f"{round(area_inclinada, 2)} m²")

    st.write("---")

    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.subheader("🌱 Material Ecológico Sugerido")
        st.info(info["material_eco"])
        
    with col_inf2:
        st.subheader("💰 Presupuesto Estimado y Logística")
        st.success(f"**Costo Estimado Materiales:** S/. {round(costo_total, 2)} Soles")
        st.warning(f"**Volumen Comercial:** Requiere aprox. **{cantidad_calaminas}** planchas de calamina estándar.")

    # --- BOTÓN PARA GENERAR Y DESCARGAR EL PDF CON LOS NUEVOS PARÁMETROS ---
    st.write("---")
    st.subheader("📋 Documentación de Ingeniería")
    
    pdf_data = generar_pdf(
        ciudad=ciudad, 
        ancho=ancho, 
        largo=largo, 
        info=info, 
        altura=altura_centro, 
        area=area_inclinada, 
        calaminas=cantidad_calaminas, 
        costo=costo_total,
        pendiente=pendiente,
        angulo_grados=angulo_grados
    )
    
    st.download_button(
        label="📥 Descargar Reporte Técnico (PDF)",
        data=pdf_data,
        file_name=f"Reporte_KeyzCAD_{ciudad.replace(' ', '_')}.pdf",
        mime="application/pdf"
    )

# -------------------------------------------------------------------
# SECCIÓN 3: SUSTENTO (Tus escudos de defensa científica)
# -------------------------------------------------------------------
elif seccion_activa == "Sustento Científico y Normas":
    st.title("📚 Sustento Técnico y Marco Normativo")
    
    st.markdown("### 🏢 1. Reglamento Nacional de Edificaciones (RNE)")
    st.write(
        "Los ángulos de inclinación asignados en el diccionario de datos responden a las exigencias de la **Norma Técnica E.080**..."
    )
