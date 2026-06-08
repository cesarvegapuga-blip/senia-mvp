import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="SENIA · Ecosistema",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');
:root {
    --verde:#00FF88; --verde-dim:#00CC66; --negro:#0A0A0A;
    --gris:#111111; --gris2:#1A1A1A; --gris3:#2A2A2A;
    --blanco:#F0F0F0; --texto:#CCCCCC;
}
html,body,[data-testid="stAppViewContainer"]{background-color:var(--negro)!important;color:var(--blanco)!important;font-family:'DM Sans',sans-serif;}
[data-testid="stHeader"]{background:var(--negro)!important;}
[data-testid="stSidebar"]{background:var(--gris)!important;border-right:1px solid var(--gris3)!important;}
h1,h2,h3{font-family:'Space Mono',monospace!important;}
.sidebar-logo{font-family:'Space Mono',monospace;font-size:1.6rem;font-weight:700;color:var(--verde);letter-spacing:0.15em;padding:1.2rem 0 0.2rem;text-align:center;}
.sidebar-tagline{font-size:0.65rem;color:#555;letter-spacing:0.2em;text-transform:uppercase;text-align:center;margin-bottom:1.5rem;}
.sidebar-divider{border:none;border-top:1px solid var(--gris3);margin:0.8rem 0;}
.senia-header{text-align:center;padding:2rem 1rem 1.5rem;border-bottom:1px solid var(--gris3);margin-bottom:2rem;}
.senia-logo{font-family:'Space Mono',monospace;font-size:2.4rem;font-weight:700;color:var(--verde);letter-spacing:0.15em;}
.senia-sub{font-size:0.8rem;color:var(--texto);letter-spacing:0.3em;text-transform:uppercase;margin-top:0.3rem;}
.senia-desc{font-size:0.9rem;color:var(--texto);max-width:600px;margin:0.6rem auto 0;line-height:1.6;}
.section-title{font-family:'Space Mono',monospace;color:var(--verde);font-size:0.72rem;letter-spacing:0.25em;text-transform:uppercase;border-left:3px solid var(--verde);padding-left:0.75rem;margin:2rem 0 1rem;}
.stTextInput input,.stTextArea textarea,.stNumberInput input,.stSelectbox div[data-baseweb="select"]{background-color:var(--gris2)!important;color:var(--blanco)!important;border:1px solid var(--gris3)!important;border-radius:6px!important;font-family:'DM Sans',sans-serif!important;}
.stMultiSelect div[data-baseweb="select"]{background-color:var(--gris2)!important;border:1px solid var(--gris3)!important;}
.stSlider [data-testid="stThumbValue"]{color:var(--verde)!important;}
.stSlider [role="slider"]{background-color:var(--verde)!important;}
.stFormSubmitButton button,.stButton button{background-color:var(--verde)!important;color:var(--negro)!important;font-family:'Space Mono',monospace!important;font-weight:700!important;font-size:0.9rem!important;border:none!important;border-radius:6px!important;padding:0.6rem 1.5rem!important;width:100%!important;letter-spacing:0.08em;transition:opacity 0.2s;}
.stFormSubmitButton button:hover,.stButton button:hover{opacity:0.82;}
label{color:var(--texto)!important;font-size:0.88rem!important;}
.resultado-card{background:var(--gris2);border:1px solid var(--gris3);border-radius:10px;padding:2rem;margin:1.5rem 0;text-align:center;}
.nivel-badge{font-family:'Space Mono',monospace;font-size:1.7rem;font-weight:700;padding:0.5rem 1.5rem;border-radius:6px;display:inline-block;margin:0.5rem 0 1rem;}
.nivel-bajo{color:#00FF88;border:2px solid #00FF88;}
.nivel-moderado{color:#FFD700;border:2px solid #FFD700;}
.nivel-alto{color:#FF8C00;border:2px solid #FF8C00;}
.nivel-critico{color:#FF3333;border:2px solid #FF3333;}
.nivel-catastrofe{color:#FF0000;border:2px solid #FF0000;background:rgba(255,0,0,0.08);box-shadow:0 0 20px rgba(255,0,0,0.3);}
.rec-box{background:var(--gris3);border-radius:8px;padding:1.2rem 1.5rem;margin-top:1rem;font-size:0.9rem;line-height:1.7;color:var(--texto);text-align:left;}
.hab-card{background:var(--gris2);border:1px solid var(--gris3);border-radius:10px;padding:1.5rem;margin-bottom:1rem;text-align:center;}
.hab-nombre{font-family:'Space Mono',monospace;font-size:1.2rem;font-weight:700;color:var(--verde);margin-bottom:0.3rem;}
.hab-precio{font-size:1.6rem;font-weight:600;color:var(--blanco);margin:0.4rem 0;}
.hab-libre{color:#00FF88;font-size:0.8rem;font-weight:600;letter-spacing:0.1em;}
.hab-ocupada{color:#FF5555;font-size:0.8rem;font-weight:600;letter-spacing:0.1em;}
.store-card{background:var(--gris2);border:1px solid var(--gris3);border-radius:10px;padding:1.2rem 1.5rem;margin-bottom:0.8rem;}
[data-testid="metric-container"]{background:var(--gris2)!important;border:1px solid var(--gris3)!important;border-radius:8px!important;padding:1rem!important;}
.stDownloadButton button{background:transparent!important;color:var(--verde)!important;border:1px solid var(--verde)!important;font-size:0.8rem!important;}
hr{border-color:var(--gris3)!important;}
#MainMenu,footer,header{visibility:hidden;}
.viewerBadge_container__1QSob{display:none!important;}
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">SENIA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">BIOCENTRIC · Ecosistema SST</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    modulo = st.radio("Nav", ["🧠 SENVAL","🏠 Habitaciones","🛒 SenStore","🔬 SenSearch","📊 Dashboard"], label_visibility="collapsed")
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.65rem;color:#444;text-align:center;letter-spacing:0.1em;">v1.1 · SENVAL ENGINE<br>BIOCENTRIC © 2026</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════
# SENVAL
# ════════════════════════════════════════════════════════
if modulo == "🧠 SENVAL":
    st.markdown("""
    <div class="senia-header">
        <div class="senia-logo">SENVAL</div>
        <div class="senia-sub">Motor de Evaluación de Riesgo Ocupacional</div>
        <div class="senia-desc">Evaluación preliminar de salud mental, ergonomía, riesgos psicosociales y SST.</div>
    </div>""", unsafe_allow_html=True)

    with st.form("senval_form"):
        st.markdown('<div class="section-title">01 · Datos del evaluado</div>', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            nombre  = st.text_input("Nombre completo")
            edad    = st.number_input("Edad", min_value=16, max_value=80, value=30)
            sexo    = st.selectbox("Sexo biológico", ["Prefiero no indicar","Femenino","Masculino","Otro"])
        with c2:
            puesto  = st.text_input("Puesto / actividad")
            empresa = st.text_input("Empresa / institución")
            motivo  = st.text_area("Motivo de evaluación", height=108)

        st.markdown('<div class="section-title">02 · Estado actual</div>', unsafe_allow_html=True)
        c3,c4 = st.columns(2)
        with c3:
            malestar = st.slider("Nivel de malestar (0 = ninguno · 10 = máximo)", 0, 10, 0)
        with c4:
            zona = st.multiselect("Zona(s) de dolor o malestar",
                ["Cabeza / migraña","Cuello","Hombros","Espalda alta","Espalda baja / lumbar",
                 "Muñecas / manos","Caderas","Rodillas","Pies / tobillos","Emocional / mental","Otra"])

        st.markdown('<div class="section-title">03 · Tipo de evaluación</div>', unsafe_allow_html=True)
        tipo = st.selectbox("Enfoque principal",
            ["Mixta (recomendada)","Salud mental","Ergonomía","Riesgo psicosocial laboral","SST / Seguridad","Wellness"])

        st.markdown('<div class="section-title">04 · Instrumentos</div>', unsafe_allow_html=True)
        c5,c6,c7 = st.columns(3)
        with c5:
            st.caption("**Salud mental**")
            inst_mental = st.multiselect("m", ["GAD-7","PHQ-9","AUDIT","GHQ-12","MBI","ERI","MBTI orientativo"], label_visibility="collapsed")
        with c6:
            st.caption("**Ergonomía**")
            inst_ergo = st.multiselect("e", ["RULA","REBA","ROSA","OWAS","NIOSH","Snook & Ciriello","MAPO"], label_visibility="collapsed")
        with c7:
            st.caption("**Psicosocial / higiene**")
            inst_psico = st.multiselect("p", ["FPSICO 4.1","CoPsoQ / ISTAS21","Checklist puesto","Registro fotográfico","Observación instalaciones"], label_visibility="collapsed")

        submitted = st.form_submit_button("⟶ GENERAR EVALUACIÓN SENVAL")

    if submitted:
        instrumentos = inst_mental + inst_ergo + inst_psico
        score = malestar * 10
        if score <= 39:
            nivel,clase = "Bajo","nivel-bajo"
            rec = "No se identifican señales de alerta. Mantener seguimiento preventivo y hábitos saludables. Tamizaje semestral."
        elif score <= 59:
            nivel,clase = "Moderado","nivel-moderado"
            rec = "Indicadores que requieren atención. Aplicar instrumentos seleccionados y revisar condiciones laborales. Seguimiento en 30 días."
        elif score <= 74:
            nivel,clase = "Alto","nivel-alto"
            rec = "Riesgo elevado. Aplicación inmediata de instrumentos clínicos. Considerar derivación a salud ocupacional."
        elif score <= 89:
            nivel,clase = "Crítico","nivel-critico"
            rec = "Intervención prioritaria. Derivación inmediata a médico ocupacional. Notificar a RRHH y registrar en vigilancia de salud."
        else:
            nivel,clase = "CATÁSTROFE","nivel-catastrofe"
            rec = "⚠ ALERTA MÁXIMA. Intervención de emergencia. Activar protocolo de crisis. Derivación urgente a profesional de salud."

        st.markdown(f"""
        <div class="resultado-card">
            <div style="font-family:'Space Mono',monospace;font-size:0.7rem;letter-spacing:0.2em;color:#666;text-transform:uppercase;margin-bottom:0.5rem;">Resultado SENVAL</div>
            <div class="nivel-badge {clase}">{nivel}</div>
            <div style="font-size:0.85rem;color:#666;margin-bottom:1rem;">Score estimado: {score}/100</div>
            <div style="font-size:0.9rem;color:#aaa;">Tipo: <strong style="color:#eee;">{tipo}</strong> &nbsp;·&nbsp; Instrumentos: <strong style="color:#eee;">{len(instrumentos)}</strong></div>
            <div class="rec-box">{rec}</div>
        </div>""", unsafe_allow_html=True)

        m1,m2,m3 = st.columns(3)
        m1.metric("Score SENVAL", f"{score}/100")
        m2.metric("Instrumentos", len(instrumentos))
        m3.metric("Zonas afectadas", len(zona) if zona else 0)

        if instrumentos:
            st.markdown('<div class="section-title">Instrumentos seleccionados</div>', unsafe_allow_html=True)
            for i in instrumentos:
                st.markdown(f"&nbsp;&nbsp;`→` {i}")

        st.markdown('<div class="section-title">Exportar</div>', unsafe_allow_html=True)
        data = {"fecha":datetime.now().strftime("%Y-%m-%d %H:%M"),"nombre":nombre,"edad":edad,"sexo":sexo,
                "puesto":puesto,"empresa":empresa,"motivo":motivo,"malestar_0_10":malestar,
                "score_senval":score,"nivel_senval":nivel,"zona_dolor":", ".join(zona) if zona else "—",
                "tipo_eval":tipo,"instrumentos":", ".join(instrumentos) if instrumentos else "—"}
        df = pd.DataFrame([data])
        st.download_button("↓ Descargar resultado CSV", df.to_csv(index=False).encode("utf-8"), "senval_resultado.csv","text/csv")

# ════════════════════════════════════════════════════════
# HABITACIONES
# ════════════════════════════════════════════════════════
elif modulo == "🏠 Habitaciones":
    st.markdown("""
    <div class="senia-header">
        <div class="senia-logo">SenHouse</div>
        <div class="senia-sub">Coliving · Cumbayá, Ecuador</div>
        <div class="senia-desc">Comunidad de mujeres emprendedoras. Bienestar, networking y experiencias.</div>
    </div>""", unsafe_allow_html=True)

    habs = [
        {"nombre":"AQUA","sub":"Suite Master","precio":"$350 / mes","cap":"Hasta 3 personas","libre":True,"desc":"Suite principal con baño privado, mayor amplitud y vista al jardín."},
        {"nombre":"TERRA","sub":"Habitación estándar","precio":"$250 / mes","cap":"1 persona","libre":False,"desc":"Habitación acogedora con escritorio de trabajo y ventilación natural."},
        {"nombre":"IGNIS","sub":"Habitación estándar","precio":"$250 / mes","cap":"1 persona","libre":False,"desc":"Ambiente cálido con acceso directo a áreas comunes y terraza."},
    ]
    for h in habs:
        est_clase = "hab-libre" if h["libre"] else "hab-ocupada"
        est_txt   = "● Disponible" if h["libre"] else "● Ocupada"
        st.markdown(f"""
        <div class="hab-card">
            <div class="hab-nombre">{h['nombre']}</div>
            <div style="font-size:0.75rem;color:#666;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:0.5rem;">{h['sub']}</div>
            <div class="hab-precio">{h['precio']}</div>
            <div style="font-size:0.82rem;color:#888;margin:0.3rem 0 0.6rem;">{h['cap']}</div>
            <div class="{est_clase}">{est_txt}</div>
            <div style="font-size:0.85rem;color:#888;margin-top:0.8rem;">{h['desc']}</div>
        </div>""", unsafe_allow_html=True)
        if h["libre"]:
            if st.button(f"Reservar {h['nombre']}", key=f"hab_{h['nombre']}"):
                st.success(f"Solicitud para {h['nombre']} enviada. Nos contactamos en breve.")
        else:
            st.markdown('<div style="text-align:center;color:#444;font-size:0.8rem;padding:0.3rem 0 1rem;">No disponible actualmente</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Servicios incluidos</div>', unsafe_allow_html=True)
    inc = ["WiFi alta velocidad","Áreas comunes","Cocina equipada","Lavandería","Seguridad 24h","Actividades de bienestar"]
    cols = st.columns(3)
    for i,s in enumerate(inc):
        cols[i%3].markdown(f"✦ {s}")

# ════════════════════════════════════════════════════════
# SENSTORE
# ════════════════════════════════════════════════════════
elif modulo == "🛒 SenStore":
    st.markdown("""
    <div class="senia-header">
        <div class="senia-logo">SenStore</div>
        <div class="senia-sub">Servicios · Wellness · SST</div>
        <div class="senia-desc">Reserva servicios de bienestar, evaluaciones y capacitaciones profesionales.</div>
    </div>""", unsafe_allow_html=True)

    servicios = [
        {"nombre":"Evaluación SENVAL","desc":"Evaluación completa de riesgo ocupacional con reporte PDF.","precio":"$80","emoji":"🧠"},
        {"nombre":"Jacuzzi","desc":"Sesión de hidroterapia y relajación muscular profunda.","precio":"$25","emoji":"💧"},
        {"nombre":"Masaje terapéutico","desc":"Sesión de 60 min enfocada en tensión laboral.","precio":"$35","emoji":"🤲"},
        {"nombre":"Mentoría SST","desc":"Sesión 1:1 con especialista en seguridad y salud ocupacional.","precio":"$60","emoji":"🎯"},
        {"nombre":"Capacitación SST grupal","desc":"Taller certificado, hasta 20 personas, 4 horas.","precio":"$200","emoji":"📋"},
    ]
    st.markdown('<div class="section-title">Servicios disponibles</div>', unsafe_allow_html=True)
    for s in servicios:
        ca,cb = st.columns([4,1])
        with ca:
            st.markdown(f"""
            <div class="store-card">
                <div style="font-size:1.3rem;margin-bottom:0.3rem;">{s['emoji']}</div>
                <div style="font-weight:600;color:var(--blanco);font-size:1rem;">{s['nombre']}</div>
                <div style="font-size:0.82rem;color:#777;margin-top:0.2rem;">{s['desc']}</div>
                <div style="font-family:'Space Mono',monospace;color:var(--verde);font-size:1.1rem;margin-top:0.5rem;">{s['precio']}</div>
            </div>""", unsafe_allow_html=True)
        with cb:
            st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)
            if st.button("Reservar", key=f"store_{s['nombre']}"):
                st.success(f"✓ Solicitud '{s['nombre']}' recibida.")

# ════════════════════════════════════════════════════════
# SENSEARCH
# ════════════════════════════════════════════════════════
elif modulo == "🔬 SenSearch":
    st.markdown("""
    <div class="senia-header">
        <div class="senia-logo">SenSearch</div>
        <div class="senia-sub">Investigación Científica · APA 7</div>
        <div class="senia-desc">Búsqueda automática en PubMed, Scopus, ScienceDirect y SciELO con niveles de evidencia CEBM.</div>
    </div>""", unsafe_allow_html=True)

    with st.form("sensearch_form"):
        query = st.text_input("Término de búsqueda", placeholder="ej. burnout petroleum workers Latin America")
        sa,sb,sc = st.columns(3)
        with sa:
            fuentes = st.multiselect("Fuentes",["PubMed","Scopus","ScienceDirect","SciELO","OpenAlex"],default=["PubMed","Scopus"])
        with sb:
            anio = st.number_input("Desde año", min_value=2015, max_value=2026, value=2021)
        with sc:
            max_res = st.selectbox("Resultados",[5,10,20])
        search_sub = st.form_submit_button("⟶ BUSCAR")

    if search_sub and query:
        st.markdown('<div class="section-title">Resultados — próxima versión conectará APIs reales</div>', unsafe_allow_html=True)
        ejemplos = [
            {"titulo":"Occupational stress and mental health in industrial workers: a systematic review","autores":"García, M., López, R., & Torres, J.","año":2023,"fuente":"Occupational Medicine","doi":"10.1093/occmed/mqad001","ev":"II"},
            {"titulo":"Psychosocial risk factors in the petroleum industry: prevalence and intervention","autores":"Ramírez, C., Vega, A., & Suárez, L.","año":2022,"fuente":"Safety and Health at Work","doi":"10.1016/j.shaw.2022.03.004","ev":"III"},
            {"titulo":"GAD-7 and PHQ-9 validity in Latin American occupational settings","autores":"Mendoza, P., & Herrera, K.","año":2024,"fuente":"Int. Journal of Environmental Research and Public Health","doi":"10.3390/ijerph21010088","ev":"II"},
        ]
        for r in ejemplos[:max_res]:
            st.markdown(f"""
            <div style="background:var(--gris2);border:1px solid var(--gris3);border-radius:8px;padding:1.2rem;margin-bottom:0.8rem;">
                <div style="font-size:0.95rem;font-weight:600;color:var(--blanco);margin-bottom:0.3rem;">{r['titulo']}</div>
                <div style="font-size:0.8rem;color:#888;">{r['autores']} ({r['año']}). <em>{r['fuente']}</em>.</div>
                <div style="font-size:0.8rem;color:#555;margin-top:0.2rem;">https://doi.org/{r['doi']}</div>
                <div style="margin-top:0.5rem;">
                    <span style="font-size:0.7rem;background:var(--gris3);color:var(--verde);padding:0.2rem 0.5rem;border-radius:4px;letter-spacing:0.1em;">CEBM Nivel {r['ev']}</span>
                </div>
                <div style="font-size:0.75rem;color:#666;margin-top:0.5rem;font-family:'Space Mono',monospace;">
                    APA 7: {r['autores']} ({r['año']}). {r['titulo']}. <em>{r['fuente']}</em>. https://doi.org/{r['doi']}
                </div>
            </div>""", unsafe_allow_html=True)
        st.info("⚡ SenSearch v2 conectará APIs reales de PubMed y Scopus con verificación DOI automática.")

# ════════════════════════════════════════════════════════
# DASHBOARD
# ════════════════════════════════════════════════════════
elif modulo == "📊 Dashboard":
    st.markdown("""
    <div class="senia-header">
        <div class="senia-logo">Dashboard</div>
        <div class="senia-sub">SENIA · Vista administrativa</div>
        <div class="senia-desc">Métricas del ecosistema SENIA.</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Métricas generales</div>', unsafe_allow_html=True)
    d1,d2,d3,d4 = st.columns(4)
    d1.metric("Evaluaciones SENVAL","47","+8 este mes")
    d2.metric("Ingresos estimados","$2.340","+$480 este mes")
    d3.metric("Habitaciones ocupadas","2 / 3","1 disponible")
    d4.metric("Papers guardados","126","+14 esta semana")

    st.markdown('<div class="section-title">Estado de módulos</div>', unsafe_allow_html=True)
    mods = {"SENVAL":"✅ Activo","SenHouse":"✅ Activo","SenStore":"🟡 En configuración","SenSearch":"🟡 APIs pendientes","Reporte PDF":"🔴 Próximamente","WhatsApp Bot":"🔴 Próximamente"}
    e1,e2 = st.columns(2)
    for i,(m,s) in enumerate(mods.items()):
        col = e1 if i%2==0 else e2
        col.markdown(f"""
        <div style="background:var(--gris2);border:1px solid var(--gris3);border-radius:8px;padding:0.8rem 1rem;margin-bottom:0.5rem;display:flex;justify-content:space-between;">
            <span style="font-weight:600;color:var(--blanco);">{m}</span>
            <span style="font-size:0.85rem;">{s}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Actividad reciente</div>', unsafe_allow_html=True)
    act = [
        ("2026-06-08 21:30","SENVAL","Evaluación completada","Moderado"),
        ("2026-06-08 19:15","SenHouse","Consulta habitación Aqua","—"),
        ("2026-06-07 14:00","SenStore","Reserva Mentoría SST","$60"),
        ("2026-06-06 10:30","SenSearch","Búsqueda: burnout petroleum","3 papers"),
    ]
    st.dataframe(pd.DataFrame(act, columns=["Fecha","Módulo","Evento","Resultado"]), use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">Estado del MVP</div>', unsafe_allow_html=True)
    st.success("SENIA MVP v1.1 activo: SENVAL + Habitaciones + SenStore + SenSearch + Dashboard visual.")
    st.markdown("""
    <div class="rec-box">
        <strong>Próximos pasos:</strong><br>
        1. Agregar SQLite para guardar evaluaciones y reservas.<br>
        2. Generar PDF automático de SENVAL.<br>
        3. Conectar WhatsApp para reservas.<br>
        4. Convertir SenSearch en biblioteca real con DOI y APA 7.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; margin-top:3rem; font-family:'Space Mono',monospace;
                font-size:0.65rem; color:#333; letter-spacing:0.2em;">
        SENIA · BIOCENTRIC · ECOSYSTEM v1.1
    </div>
    """, unsafe_allow_html=True)
