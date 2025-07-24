import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_indiceBovespa = pd.read_csv(r"app_ibovespa\bvsp.csv")

dias = df_indiceBovespa["Data"].unique()
dia = st.sidebar.selectbox("Dias", dias)

df_dias = df_indiceBovespa[df_indiceBovespa["Data"] == dia]

dia_data = df_dias["Data"].iloc[0]
dia_fechamento = f"{df_dias['Último'].iloc[0]} pontos"
dia_abertura = f"{df_dias['Abertura'].iloc[0]} pontos"
dia_maxima = f"{df_dias['Máxima'].iloc[0]} pontos"
dia_minima = f"{df_dias['Mínima'].iloc[0]} pontos"
dia_volume = df_dias["Vol."].iloc[0]
dia_var = df_dias["Var%"].iloc[0]

st.title("Análise diária do IBoversa (2010-2023)")
st.header(f"Dia {dia_data}")
st.subheader(f"Volume: {dia_volume}")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Abertura", dia_abertura)
col2.metric("Mínima", dia_minima)
col3.metric("Máxima", dia_maxima)
col4.metric("Fechamento", dia_fechamento, dia_var)