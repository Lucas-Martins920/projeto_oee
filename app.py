import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime
import io
import time
import random
from fpdf import FPDF

# --- CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="OEE Matrix Simulation", layout="wide")

# --- CSS ADAPTÁVEL (ALTO CONTRASTE) ---
st.markdown("""
<style>
    /* Estilo dos Cards - Translúcido com borda de destaque */
    div[data-testid="stMetric"] {
        background-color: rgba(28, 131, 225, 0.1) !important;
        border: 2px solid #1e3d59 !important; 
        border-radius: 12px;
        padding: 15px;
    }
    
    /* Ajuste de borda para destacar no modo escuro */
    @media (prefers-color-scheme: dark) {
        div[data-testid="stMetric"] { border: 2px solid #00d488 !important; }
    }

    [data-testid="stMetricValue"] { color: #00d488 !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] { font-weight: bold; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE SISTEMA ---
def init_db():
    conn = sqlite3.connect('oee_simulation.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (data_hora TEXT, disponibilidade REAL, performance REAL, qualidade REAL, oee REAL, motivo TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- SIDEBAR: MODO SIMULAÇÃO ---
with st.sidebar:
    st.title("🎮 PAINEL DE CONTROLE")
    simulacao_ativa = st.toggle("⚡ ATIVAR MODO SIMULAÇÃO", help="Gera dados automáticos a cada 3 segundos")
    st.divider()
    
    if not simulacao_ativa:
        st.subheader("Registro Manual")
        with st.form("manual_form"):
            t_total = st.number_input("Tempo de Turno (min)", 480)
            t_parada = st.number_input("Tempo Parada (min)", 30)
            p_total = st.number_input("Produção Total", 1000)
            p_ruins = st.number_input("Peças Defeituosas", 15)
            v_meta = st.number_input("Velocidade Meta (pç/min)", 2.5)
            motivo = st.selectbox("Motivo da Parada", ["Normal", "Manutenção", "Setup", "Falta Material"])
            if st.form_submit_button("SALVAR REGISTRO"):
                # Cálculos rápidos
                d = (t_total - t_parada) / t_total
                p = p_total / ((t_total - t_parada) * v_meta)
                q = (p_total - p_ruins) / p_total
                oee = d * p * q
                conn = sqlite3.connect('oee_simulation.db')
                c = conn.cursor()
                c.execute("INSERT INTO logs VALUES (?,?,?,?,?,?)", 
                          (datetime.now().strftime("%H:%M:%S"), d, p, q, oee, motivo))
                conn.commit()
                conn.close()
                st.rerun()

# --- LÓGICA DE SIMULAÇÃO (AUTO-GENERATE) ---
if simulacao_ativa:
    # Gera números aleatórios mas realistas
    d_sim = random.uniform(0.7, 0.95)
    p_sim = random.uniform(0.8, 0.98)
    q_sim = random.uniform(0.9, 1.0)
    oee_sim = d_sim * p_sim * q_sim
    
    conn = sqlite3.connect('oee_simulation.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?,?,?,?,?,?)", 
              (datetime.now().strftime("%H:%M:%S"), d_sim, p_sim, q_sim, oee_sim, "Simulação IoT"))
    conn.commit()
    conn.close()
    time.sleep(3) # Aguarda 3 segundos
    st.rerun()

# --- INTERFACE POR ABAS ---
tab1, tab2, tab3, tab4 = st.tabs(["DASHBOARD VIVO", "HISTÓRICO COMPLETO", "ANÁLISE TÉCNICA", "EXPORTAR DADOS"])

# Carregamento de dados
conn = sqlite3.connect('oee_simulation.db')
df = pd.read_sql_query("SELECT * FROM logs", conn)
conn.close()

# ABA 1: DASHBOARD
with tab1:
    if not df.empty:
        ultimo = df.iloc[-1]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Disponibilidade Operacional", f"{ultimo['disponibilidade']:.1%}")
        c2.metric("Performance de Velocidade", f"{ultimo['performance']:.1%}")
        c3.metric("Qualidade de Produção", f"{ultimo['qualidade']:.1%}")
        c4.metric("Eficiência Global (OEE)", f"{ultimo['oee']:.1%}")
        
        st.subheader("Linha do Tempo em Tempo Real")
        fig = px.line(df.tail(20), x='data_hora', y='oee', markers=True, title="Telemetria dos últimos 20 registros")
        fig.update_layout(yaxis_range=[0, 1])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Ligue a Simulação ou registre dados para ver o Dashboard.")

# ABA 2: HISTÓRICO (SEM ABREVIAÇÕES)
with tab2:
    st.subheader("Log de Auditoria Industrial")
    if not df.empty:
        # Renomeando para exibição clara
        df_visual = df.rename(columns={
            'data_hora': 'Horário do Registro',
            'disponibilidade': 'Disponibilidade Operacional',
            'performance': 'Performance de Velocidade',
            'qualidade': 'Qualidade de Produção',
            'oee': 'Eficiência Global OEE',
            'motivo': 'Motivo da Parada'
        })
        st.dataframe(df_visual.tail(50).style.format({
            'Disponibilidade Operacional': '{:.2%}',
            'Performance de Velocidade': '{:.2%}',
            'Qualidade de Produção': '{:.2%}',
            'Eficiência Global OEE': '{:.2%}'
        }), use_container_width=True)

# ABA 3: ANÁLISE TÉCNICA
with tab3:
    if not df.empty:
        st.subheader("Análise Comparativa de Pilares")
        fig_bar = px.bar(df.tail(1), y=['disponibilidade', 'performance', 'qualidade'], barmode='group')
        st.plotly_chart(fig_bar, use_container_width=True)

# ABA 4: EXPORTAÇÃO (EXCEL E PDF)
with tab4:
    if not df.empty:
        st.subheader("Baixar Documentos Oficiais")
        # EXCEL
        buffer_ex = io.BytesIO()
        df.to_excel(buffer_ex, index=False)
        st.download_button("Baixar Planilha Excel (.xlsx)", buffer_ex.getvalue(), "relatorio_oee.xlsx", use_container_width=True)
        
        # PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, "RELATORIO OEE ENTERPRISE", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        for i, r in df.tail(10).iterrows():
            pdf.cell(200, 10, f"Hora: {r['data_hora']} | OEE: {r['oee']:.2%}", ln=True)
        st.download_button("Baixar Relatório PDF", pdf.output(dest="S").encode("latin-1"), "auditoria.pdf", use_container_width=True)