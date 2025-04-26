
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Visualizador de CSV", layout="wide")
st.title("📄 Visualizador de Arquivo CSV")

caminho_arquivo = "CARTEIRA_DI_GASPI_24.04.csv"

if os.path.exists(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')
        st.subheader("📋 Tabela de Dados")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
else:
    st.error("❌ Arquivo não encontrado. Verifique se o nome e o caminho estão corretos.")
