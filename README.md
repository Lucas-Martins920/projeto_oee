#  OEE Matrix Intelligence - Sistema de Monitoramento Industrial v6.0

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red.svg)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

##  Sobre o Projeto
O **OEE Matrix Intelligence** é uma solução de Business Intelligence focada em **Indústria 4.0**. O sistema automatiza o cálculo do Índice de Eficiência Global (OEE), transformando dados operacionais em insights estratégicos para tomada de decisão no chão de fábrica.

Diferente de planilhas convencionais, este projeto integra **persistência de dados**, **análise de impacto financeiro** e um **simulador de telemetria IoT** para monitoramento contínuo.



---

##  Funcionalidades Principais

* **⚡ Modo Simulação IoT:** Motor de simulação em tempo real que mimetiza sensores de máquinas, gerando dados automáticos para testes de telemetria.
* ** Dashboard Dinâmico:** Visualização interativa dos 3 pilares:
    * **Disponibilidade Operacional:** Tempo de máquina ativa vs. paradas planejadas.
    * **Performance de Velocidade:** Ritmo de produção vs. capacidade máxima.
    * **Qualidade de Produção:** Índice de peças conformes vs. refugo.
* ** Gestão de Perdas Financeiras:** Conversão automática de tempo de parada em prejuízo financeiro (R$).
* ** Registro de Causa Raiz:** Categorização de paradas (Manutenção, Setup, Falta de Material) para análise de Pareto.
* ** Central de Exportação:**
    * **Excel (.xlsx):** Relatório completo formatado para análise de dados.
    * **PDF:** Relatório de auditoria profissional formatado para diretoria.

---

##  Estrutura do Sistema (Abas)

O sistema foi organizado em abas para garantir uma experiência de usuário (UX) limpa e profissional:

1.  ** Dashboard Vivo:** Monitoramento instantâneo com gráficos de linha e gauges (velocímetros).
2.  ** Consulta de Histórico:** Tabela detalhada sem abreviações, com formatação condicional.
3.  ** Análise Técnica:** Comparativo visual de desempenho entre os turnos.
4.  ** Central de Exportação:** Área dedicada para download de relatórios.



---

##  Tecnologias Utilizadas

* **Linguagem:** Python 3.9+
* **Interface:** Streamlit
* **Banco de Dados:** SQLite3 (Persistência de logs)
* **Gráficos:** Plotly Express & Graph Objects
* **Exportação:** FPDF (PDF) & XlsxWriter (Excel)

---

##  Como Instalar e Rodar

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/Lucas-Martins920/projeto_oee.git](https://github.com/Lucas-Martins920/projeto_oee.git)
   cd projeto_oee

   Crie um ambiente virtual (Recomendado):

2. Crie um ambiente virtual (Recomendado):
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

3. Instale as dependências:
  pip install -r requirements.txt

4. Execute a aplicação:
   streamlit run app.py

Lógica de Negócio (OEE) O sistema segue o padrão mundial de produtividade:$OEE = \text{Disponibilidade} \times \text{Performance} \times \text{Qualidade}$A interface foi desenhada com um estilo "Glassmorphism Industrial", garantindo alto contraste tanto em Modo Claro quanto em Modo Escuro, facilitando a leitura em diferentes dispositivos de fábrica.
