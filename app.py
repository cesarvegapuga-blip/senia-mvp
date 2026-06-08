import streamlit as st
import pandas as pd
from datetime import datetime

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SENIA · SENVAL",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --verde:    #00FF88;
    --verde-dim:#00CC66;
    --negro:    #0A0A0A;
    --gris:     #111111;
    --gris2:    #1A1A1A;
    --gris3:    #2A2A2A;
    --blanco:   #F0F0F0;
    --texto:    #CCCCCC;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--negro) !important;
    color: var(--blanco) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] { background: var(--negro) !important; }
[data-testid="stSidebar"] { background: var(--gris) !important; }

h1, h2, h3 { font-family: 'Space Mono', monospace !important; }

.senia-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    border-bottom: 1px solid var(--gris3);
    margin-bottom: 2rem;
}

.senia-logo {
    font-family: 'Space Mono', monospace;
    font-size: 2.8rem;
    font-weight: 700;
    color: var(--verde);
    letter-spacing: 0.15em;
}

.senia-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    color: var(--texto);
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}

.senia-desc {
    font-size: 0.9rem;
    color: var(--texto);
    max-width: 600px;
    margin: 0.8rem auto 0;
    line-height: 1.6;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: var(--gris2) !important;
    color: var(--blanco) !important;
    border: 1px solid var(--gris3) !important;
    border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
}

.stMultiSelect div[data-baseweb="select"] {
    background-color: var(--gris2) !important;
    border: 1px solid var(--gris3) !important;
}

/* Slider */
.stSlider [data-testid="stThumbValue"] { color: var(--verde) !important; }
.stSlider [role="slider"] { background-color: var(--verde) !important; }

/* Botón submit */
.stFormSubmitButton button {
    background-color: var(--verde) !important;
    color: var(--negro) !important;
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.7rem 2rem !important;
    width: 100% !important;
    letter-spacing: 0.1em;
    transition: opacity 0.2s;
}
.stFormSubmitButton button:hover { opacity: 0.85; }

/* Labels */
label { color: var(--texto) !important; font-size: 0.9rem !important; }

/* Section headers */
.section-title {
    font-family: 'Space Mono', monospace;
    color: var(--verde);
    font-size: 0.75rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    border-left: 3px solid var(--verde);
    padding-left: 0.75rem;
    margin: 2rem 0 1rem;
}

/* Resultado */
.resultado-card {
    background: var(--gris2);
    border: 1px solid var(--gris3);
    border-radius: 10px;
    padding: 2rem;
    margin: 1.5rem 0;
    text-align: center;
}

.nivel-badge {
    font-family: 'Space Mono', monospace;
    font-size: 1.8rem;
    font-weight: 700;
    padding: 0.5rem 1.5rem;
    border-radius: 6px;
    display: inline-block;
    margin: 0.5rem 0 1rem;
}

.nivel-bajo       { color: #00FF88; border: 2px solid #00FF88; }
.nivel-moderado   { color: #FFD700; border: 2px solid #FFD700; }
.nivel-alto       { color: #FF8C00; border: 2px solid #FF8C00; }
.nivel-critico    { color: #FF3333; border: 2px solid #FF3333; }
.nivel-catastrofe { color: #FF0000; border: 2px solid #FF0000; background: rgba(255,0,0,0.08); box-shadow: 0 0 20px rgba(255,0,0,0.3); }

.rec-box {
    background: var(--gris3);
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
    font-size: 0.9rem;
    line-height: 1.7;
    color: var(--texto);
    text-align: left;
}

/* Download btn */
.stDownloadButton button {
    background: transparent !important;
    color: var(--verde) !important;
    border: 1px solid var(--verde) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    border-radius: 6px !important;
    padding: 0.5rem 1.2rem !important;
}

/* Divider */
hr { border-color: var(--gris3) !important; }

/* Metrics */
[data-testid="metric-container"] {
    background: var(--gris2) !important;
    border: 1px solid var(--gris3) !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.viewerBadge_container__1QSob { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ─── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="senia-header">
    <div class="senia-logo">SENIA</div>
    <div class="senia-sub">SENVAL · Motor de Evaluación de Riesgo Ocupacional</div>
    <div class="senia-desc">
        Evaluación preliminar de salud mental, ergonomía, riesgos psicosociales
        y seguridad y salud en el trabajo.
    </div>
</div>
""", unsafe_allow_html=True)

# ─── FORMULARIO ─────────────────────────────────────────────────────────────────
with st.form("senval_form"):

    st.markdown('<div class="section-title">01 · Datos del evaluado</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre completo")
        edad   = st.number_input("Edad", min_value=16, max_value=80, value=30)
        sexo   = st.selectbox("Sexo biológico", ["Prefiero no indicar", "Femenino", "Masculino", "Otro"])
    with col2:
        puesto  = st.text_input("Puesto / actividad")
        empresa = st.text_input("Empresa / institución")
        motivo  = st.text_area("Motivo de evaluación", height=108)

    st.markdown('<div class="section-title">02 · Estado actual</div>', unsafe_allow_html=True)
    col3, col4 = st.columns([1, 1])
    with col3:
        malestar = st.slider("Nivel general de malestar (0 = ninguno · 10 = máximo)", 0, 10, 0)
    with col4:
        zona = st.multiselect(
            "Zona(s) de dolor o malestar",
            ["Cabeza / migraña", "Cuello", "Hombros", "Espalda alta",
             "Espalda baja / lumbar", "Muñecas / manos", "Caderas",
             "Rodillas", "Pies / tobillos", "Emocional / mental", "Otra"]
        )

    st.markdown('<div class="section-title">03 · Tipo de evaluación</div>', unsafe_allow_html=True)
    tipo = st.selectbox(
        "Enfoque principal",
        ["Mixta (recomendada)", "Salud mental", "Ergonomía",
         "Riesgo psicosocial laboral", "SST / Seguridad", "Wellness / Bienestar"]
    )

    st.markdown('<div class="section-title">04 · Instrumentos a aplicar</div>', unsafe_allow_html=True)
    col5, col6, col7 = st.columns(3)
    with col5:
        st.caption("**Salud mental / psicosocial**")
        inst_mental = st.multiselect("", [
            "GAD-7", "PHQ-9", "AUDIT", "GHQ-12", "MBI", "ERI", "MBTI orientativo"
        ], label_visibility="collapsed")
    with col6:
        st.caption("**Ergonomía**")
        inst_ergo = st.multiselect("", [
            "RULA", "REBA", "ROSA", "OWAS",
            "NIOSH", "Snook & Ciriello", "MAPO"
        ], label_visibility="collapsed")
    with col7:
        st.caption("**Psicosocial laboral / higiene**")
        inst_psico = st.multiselect("", [
            "FPSICO 4.1", "CoPsoQ / ISTAS21",
            "Checklist puesto de trabajo",
            "Registro fotográfico",
            "Observación de instalaciones"
        ], label_visibility="collapsed")

    submitted = st.form_submit_button("⟶ GENERAR EVALUACIÓN SENVAL")

# ─── RESULTADO ──────────────────────────────────────────────────────────────────
if submitted:
    instrumentos = inst_mental + inst_ergo + inst_psico

    # Escala SENVAL de 5 niveles (0–10 → 0–100)
    score = malestar * 10

    if score <= 39:
        nivel = "Bajo"
        clase = "nivel-bajo"
        score_label = f"{score}/100"
        rec = (
            "No se identifican señales de alerta inmediatas. "
            "Se recomienda mantener seguimiento preventivo, registrar periódicamente el estado de salud "
            "y fortalecer hábitos de bienestar. Aplicar instrumentos de tamizaje de forma semestral."
        )
    elif score <= 59:
        nivel = "Moderado"
        clase = "nivel-moderado"
        score_label = f"{score}/100"
        rec = (
            "Existen indicadores que requieren atención. "
            "Aplicar los instrumentos seleccionados para caracterizar el riesgo con mayor precisión. "
            "Revisar condiciones de trabajo, pausas activas y carga mental. "
            "Seguimiento en 30 días."
        )
    elif score <= 74:
        nivel = "Alto"
        clase = "nivel-alto"
        score_label = f"{score}/100"
        rec = (
            "Nivel de riesgo elevado. Se recomienda aplicación inmediata de instrumentos clínicos validados, "
            "revisión ergonómica del puesto y evaluación psicosocial profunda. "
            "Considerar derivación a profesional de salud ocupacional o psicólogo laboral."
        )
    elif score <= 89:
        nivel = "Crítico"
        clase = "nivel-critico"
        score_label = f"{score}/100"
        rec = (
            "Situación crítica que requiere intervención prioritaria. "
            "Suspender exposición al factor de riesgo si es posible. "
            "Derivación inmediata a médico ocupacional, psicólogo o especialista según área afectada. "
            "Notificar a RRHH y registrar en sistema de vigilancia de salud."
        )
    else:
        nivel = "CATÁSTROFE"
        clase = "nivel-catastrofe"
        score_label = f"{score}/100"
        rec = (
            "⚠ ALERTA MÁXIMA. Intervención de emergencia requerida. "
            "Activar protocolo de crisis si aplica. "
            "Derivación inmediata y urgente a profesional de salud. "
            "Documentar el caso, notificar a responsables de SST y seguimiento diario."
        )

    # Card de resultado
    st.markdown(f"""
    <div class="resultado-card">
        <div style="font-family:'Space Mono',monospace; font-size:0.7rem; letter-spacing:0.2em; 
                    color:#666; text-transform:uppercase; margin-bottom:0.5rem;">
            Resultado SENVAL
        </div>
        <div class="nivel-badge {clase}">{nivel}</div>
        <div style="font-size:0.85rem; color:#666; margin-bottom:1rem;">
            Score estimado: {score_label}
        </div>
        <div style="font-size:0.9rem; color:#aaa;">
            Tipo de evaluación: <strong style="color:#eee;">{tipo}</strong> &nbsp;·&nbsp;
            Instrumentos: <strong style="color:#eee;">{len(instrumentos)}</strong>
        </div>
        <div class="rec-box">{rec}</div>
    </div>
    """, unsafe_allow_html=True)

    # Métricas rápidas
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Score SENVAL", f"{score}/100")
    col_m2.metric("Instrumentos seleccionados", len(instrumentos))
    col_m3.metric("Zonas afectadas", len(zona) if zona else 0)

    if instrumentos:
        st.markdown('<div class="section-title">Instrumentos para aplicar</div>', unsafe_allow_html=True)
        for i in instrumentos:
            st.markdown(f"&nbsp;&nbsp;`→` {i}")

    # Export CSV
    st.markdown('<div class="section-title">Exportar resultado</div>', unsafe_allow_html=True)
    data = {
        "fecha":        datetime.now().strftime("%Y-%m-%d %H:%M"),
        "nombre":       nombre,
        "edad":         edad,
        "sexo":         sexo,
        "puesto":       puesto,
        "empresa":      empresa,
        "motivo":       motivo,
        "malestar_0_10": malestar,
        "score_senval": score,
        "nivel_senval": nivel,
        "zona_dolor":   ", ".join(zona) if zona else "—",
        "tipo_eval":    tipo,
        "instrumentos": ", ".join(instrumentos) if instrumentos else "—",
    }
    df  = pd.DataFrame([data])
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("↓ Descargar resultado CSV", csv, "senval_resultado.csv", "text/csv")

    st.markdown("""
    <div style="text-align:center; margin-top:3rem; font-family:'Space Mono',monospace; 
                font-size:0.65rem; color:#333; letter-spacing:0.2em;">
        SENIA · BIOCENTRIC · SENVAL ENGINE v1.0
    </div>
    """, unsafe_allow_html=True)
