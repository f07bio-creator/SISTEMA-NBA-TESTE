# app_simplificado.py - VERSÃO QUE FUNCIONA
import streamlit as st
import pandas as pd
import numpy as np

# Testar plotly de forma segura
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.error("⚠️ Plotly não está instalado. Usando gráficos alternativos.")

st.set_page_config(page_title="NBA Analytics", layout="wide")
st.title("🏀 NBA ULTIMATE ANALYTICS 2025-26")

# Interface básica
st.sidebar.header("Configuração")
team1 = st.sidebar.selectbox("Time da Casa", ["Boston Celtics", "LA Lakers", "Golden State Warriors"])
team2 = st.sidebar.selectbox("Time Visitante", ["Miami Heat", "Chicago Bulls", "Denver Nuggets"])

# Dados simulados
data = pd.DataFrame({
    "Time": [team1, team2],
    "Pontos": [112, 108],
    "Rebotes": [45, 42],
    "Assistências": [25, 23]
})

st.subheader(f"Análise: {team1} vs {team2}")
st.dataframe(data)

# Gráfico (com fallback)
if PLOTLY_AVAILABLE:
    fig = px.bar(data, x='Time', y='Pontos', title='Pontuação por Time')
    st.plotly_chart(fig)
else:
    st.bar_chart(data.set_index('Time')['Pontos'])
    st.warning("Usando gráfico nativo do Streamlit (plotly não disponível)")

st.success("✅ Sistema funcionando!")
