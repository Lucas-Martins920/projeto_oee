# Projeto OEE - Dashboard de Eficiência Global de Equipamentos

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Dashboard vivo e simulador de OEE (Overall Equipment Effectiveness)** para monitoramento industrial em tempo real. Calcula e exibe métricas chave de produção: Disponibilidade Operacional, Performance de Velocidade, Qualidade de Produção e Eficiência Global (OEE), com gráficos interativos, linha do tempo e registro manual.

### Visão Geral
Este projeto transforma dados de produção em um painel de controle moderno e interativo usando **Streamlit**. Ideal para fábricas, manutenção industrial ou simulações de OEE.

- **Modo Dashboard Vivo** — Monitoramento em tempo real com telemetria dos últimos registros
- **Modo Simulação** — Ative para testar cenários alterando tempos, paradas, produção e defeitos
- **Cálculo OEE** baseado no padrão mundial:  
  **OEE = Disponibilidade × Performance × Qualidade**  
  (Exemplo: 93.2% × 90.4% × 95.6% = 80.5% — valores reais do seu screenshot)

### Features Principais
- **Métricas em Cards** (alto contraste, design industrial):  
  - Disponibilidade Operacional  
  - Performance de Velocidade  
  - Qualidade de Produção  
  - Eficiência Global (OEE)
- **Linha do Tempo em Tempo Real** — Gráfico Plotly com os últimos 20 registros (atualiza dinamicamente)
- **Registro Manual** — Inputs para:  
  - Tempo de Turno (min)  
  - Tempo de Parada (min)  
  - Produção Total (peças)  
  - Peças Defeituosas  
  - Velocidade Meta (peças/min)
- **Persistência** — Dados salvos em SQLite (`oee_simulation.db`)
- **Exportação** — Geração de relatórios em PDF (usando FPDF)
- **UI Adaptável** — Tema escuro, layout wide, cards translúcidos com bordas de destaque
- **Toggle Simulação** — Ative/desative modo de teste sem afetar dados reais

### Captura de Tela
![Dashboard OEE em Tempo Real](https://via.placeholder.com/1200x700/1e1e1e/00ff9f?text=Dashboard+OEE+Exemplo)  
*(Atualize esta imagem: tire um print do seu app rodando e suba como `screenshot.png` no repo)*

### Tecnologias Utilizadas
- **Frontend/Backend**: Streamlit (rápido e interativo)
- **Dados**: Pandas (manipulação), SQLite3 (persistência local)
- **Visualizações**: Plotly Express (gráficos interativos)
- **Exportação**: FPDF (relatórios PDF)
- **Outros**: datetime, time, random (para simulações)

### Como Instalar e Rodar Localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/Lucas-Martins920/projeto_oee.git
   cd projeto_oee
2. Crie e ative um ambiente virtual (recomendado):
  python -m venv venv
source venv/bin/activate   # Linux/Mac
# ou venv\Scripts\activate   # Windows

3. Instale as dependências:
   pip install -r requirements.txt
(Se não tiver o arquivo, crie com: pip freeze > requirements.txt após instalar manualmente: streamlit pandas plotly fpdf)

4. Rode o app:
   streamlit run app.py


Como Contribuir

+ Fork o repo
+ Crie uma branch: git checkout -b feature/nova-metrica
+ Commit suas mudanças: git commit -m "Add nova métrica X"
+ Push: git push origin feature/nova-metrica
+ Abra um Pull Request


5. Roadmap / Ideias Futuras

+ Integração com CSV/Excel para upload de dados reais
+ Autenticação simples (para multi-usuários)
+ Alertas visuais quando OEE < meta
+ Histórico completo com filtros por data/turno
+ Deploy no Streamlit Community Cloud ou Railway
+ Exportação para Excel + email automático
