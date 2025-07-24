import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Índice Bovespa (2010 - 2023)")
st.text("Histórico de cotações do Índice Bovespa (IBOV) registrados entre o dia 04 de janeiro de 2010 até o dia 02 de fevereiro de 2023.")

df_indiceBovespa = pd.read_csv(r"app_ibovespa\bvsp.csv")

preco_max = df_indiceBovespa["Último"].max()
preco_min = df_indiceBovespa["Último"].min()

fechamento = st.sidebar.slider("Preço de fechamento", preco_min, preco_max, preco_max)
df_ibovespa = df_indiceBovespa[df_indiceBovespa["Último"] <= fechamento]
df_ibovespa

fig1 = px.line(df_ibovespa, x="Data", y="Último", title="Variação do preço")
fig2 = px.bar(df_ibovespa, x="Data", y="Vol.", title="Volume 24h")

col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)