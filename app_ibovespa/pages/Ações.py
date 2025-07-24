import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit import plotly_chart

st.set_page_config(layout="wide")

st.title("Ações do IBovespa")
st.text("Empresas que compõem o índice, com tipo e participação relativa de cada papel.")

df_acoesIbovespa = pd.read_csv(r"app_ibovespa\ibovespa.csv")
df_acoesIbovespa

fig = px.pie(df_acoesIbovespa, values="participacao_relativa", names="acao", title="Participação das empresas", color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label')
plotly_chart(fig)