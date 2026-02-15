import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- CONFIGURACIÓN ---
# Cambiamos a "wide" para que la galaxia ocupe más pantalla
st.set_page_config(page_title="Para May 💜", page_icon="✨", layout="wide")

# Estilos para fondo oscuro como el espacio profundo
st.markdown("""
    <style>
    .stApp { background-color: #030008; color: white; }
    h1, h2, p { text-align: center; font-family: 'Helvetica', sans-serif; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color: #E0B0FF; text-shadow: 0px 0px 15px #9B59B6;'>✨ El Universo de May ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #D8BFD8; font-size: 16px;'>Navega por nuestra galaxia. Haz zoom y gira para descubrir todo lo que siento por ti 💜</p>", unsafe_allow_html=True)

# --- 1. MATEMÁTICAS PARA LA GALAXIA ---
num_stars = 4000
np.random.seed(150125) # ¡La semilla matemática es su fecha!
theta = np.random.uniform(0, 8 * np.pi, num_stars)
r = np.random.uniform(0, 100, num_stars)

x = r * np.cos(theta + r*0.1)
y = r * np.sin(theta + r*0.1)
z = np.random.normal(0, 4, num_stars) * (100 - r) / 100 

fig = go.Figure()

# Capa 1: Nube de estrellas moradas (el polvo estelar)
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(size=1.5, color=r, colorscale='Purples', opacity=0.4),
    hoverinfo='none',
    showlegend=False
))

# Capa 2: Estrellas blancas brillantes
num_bright = 400
fig.add_trace(go.Scatter3d(
    x=x[:num_bright], y=y[:num_bright], z=z[:num_bright] + np.random.normal(0, 3, num_bright),
    mode='markers',
    marker=dict(size=2.5, color='white', opacity=0.9),
    hoverinfo='none',
    showlegend=False
))

# --- 2. LOS MENSAJES DE AMOR (ESTRELLAS GIGANTES) ---
frases = [
    "💜 <b>15-01-25</b> 💜<br>Donde todo empezó...",
    "💌 <b>Lara Jean:</b><br><i>Te miro y te vuelves más real</i>",
    "🌧️ <b>El Diario de una Pasión:</b><br><i>Quiero hacerlo porque te quiero a ti</i>",
    "👣 <b>A Dos Metros de Ti:</b><br><i>Solo quiero que estés a salvo</i>",
    "✨ Eres mi estrella favorita<br>en toda la galaxia, May.",
    "💌 <b>Lara Jean:</b><br><i>Tú eres a quien quiero. A ti.</i>",
    "🌧️ <b>El Diario de una Pasión:</b><br><i>El mejor tipo de amor<br>es el que despierta el alma</i>",
    "💫 En este y en todos los universos,<br>te elegiría a ti siempre.",
    "💜 Gracias por pintar<br>mi mundo de color morado.",
    "✨ Eres mi casualidad más bonita.",
    "👣 <b>A Dos Metros de Ti:</b><br><i>Si esto es todo lo que tenemos,<br>entonces quiero vivirlo al máximo.</i>",
    "🌌 Eres la luz que ilumina<br>mi sistema solar entero."
]

# Distribuir las frases alrededor de la galaxia
num_frases = len(frases)
theta_f = np.linspace(0, 6 * np.pi, num_frases)
r_f = np.linspace(15, 85, num_frases) 
np.random.shuffle(r_f) # Desordenar distancias para que sea sorpresa

fx = r_f * np.cos(theta_f + r_f*0.1)
fy = r_f * np.sin(theta_f + r_f*0.1)
fz = np.random.normal(0, 20, num_frases) # Esparcirlas verticalmente para usar el 3D

# Añadir los textos al modelo
fig.add_trace(go.Scatter3d(
    x=fx, y=fy, z=fz,
    mode='markers+text',
    text=frases,
    textposition="top center",
    textfont=dict(color='#F8E0F7', size=12), # Letra rosa/morada muy clarita
    marker=dict(
        size=8, 
        color='#DDA0DD', 
        symbol='diamond', 
        opacity=1,
        line=dict(color='white', width=1.5)
    ),
    hoverinfo='none',
    showlegend=False
))

# --- 3. DISEÑO DEL ESPACIO ---
fig.update_layout(
    scene=dict(
        xaxis=dict(showbackground=False, visible=False),
        yaxis=dict(showbackground=False, visible=False),
        zaxis=dict(showbackground=False, visible=False),
        bgcolor='#030008'
    ),
    paper_bgcolor='#030008',
    margin=dict(l=0, r=0, b=0, t=0),
    height=750 # Mucho más alto para que parezca inmersivo en celular o PC
)

# Mostrar el gráfico
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.markdown("<p style='color: #9B59B6; font-size: 18px;'><b>Para mi persona favorita en el universo.</b></p>", unsafe_allow_html=True)