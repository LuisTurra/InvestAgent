# 📊 InvestAgent

Sistema híbrido de análise de ativos financeiros que combina análise quantitativa baseada em indicadores técnicos com interpretação contextual através de Large Language Models (LLMs).

O projeto foi desenvolvido para demonstrar uma arquitetura moderna onde o Python é responsável pelos cálculos matemáticos e estatísticos, enquanto o modelo de linguagem atua exclusivamente na interpretação dos resultados e geração de explicações em linguagem natural.

---
Projeto(DEMO)[https://luisturra-investagent-streamlit-app-6ughqf.streamlit.app/]
---

## 🚀 Principais Funcionalidades

* Coleta automática de dados de mercado via Yahoo Finance
* Cálculo de indicadores técnicos
* Detecção de regime de mercado
* Sistema de scoring quantitativo
* Avaliação de risco
* Integração com LLM via Groq
* Dashboard interativo desenvolvido em Streamlit
* Explicações em linguagem natural em português
* Tratamento de erros e validações de dados
* Interface inspirada em terminais financeiros

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura híbrida:

```text
Dados de Mercado
       ↓
Indicadores Técnicos
       ↓
Detecção de Regime
       ↓
Sistema de Scores
       ↓
Resumo Estruturado
       ↓
LLM (Groq)
       ↓
Recomendação e Explicação
       ↓
Dashboard Streamlit
```

### Responsabilidades

**Python**

* Coleta de dados
* Limpeza de dados
* Cálculo de indicadores
* Cálculo de scores
* Avaliação de risco
* Detecção de regime

**LLM**

* Interpretação dos resultados
* Identificação de conflitos entre sinais
* Geração de justificativas
* Recomendação BUY / HOLD / SELL

---

## 📈 Indicadores Utilizados

### RSI (Relative Strength Index)

Mede a força relativa dos movimentos de alta e baixa.

### MACD (Moving Average Convergence Divergence)

Avalia momentum e possíveis mudanças de tendência.

### EMA20 e EMA50

Médias móveis exponenciais utilizadas para identificação de tendência.

### Volatilidade

Mede o nível de risco e instabilidade dos preços.

---

## 📊 Scores Quantitativos

### Technical Score

Avalia a qualidade técnica do ativo.

### Trend Score

Avalia a força da tendência predominante.

### Momentum Score

Mede a aceleração ou desaceleração dos movimentos de preço.

### Risk Score

Avalia o nível de risco baseado na volatilidade e comportamento recente do ativo.

---

## 🤖 Integração com IA

O projeto utiliza a API da Groq para executar modelos de linguagem.

O LLM não realiza cálculos financeiros.

Ele recebe apenas um resumo estruturado contendo:

```json
{
  "ticker": "AAPL",
  "regime": "SIDEWAYS",
  "technical_score": 10,
  "trend_score": 55,
  "momentum_score": 25,
  "risk_score": 29
}
```

Com base nesses dados, gera:

* Recomendação
* Nível de risco
* Confiança
* Justificativa

---

## 🛠️ Tecnologias Utilizadas

### Linguagem

* Python

### Dashboard

* Streamlit

### Inteligência Artificial

* Groq API
* Llama 3.3 70B Versatile

### Dados Financeiros

* Yahoo Finance (yfinance)

### Manipulação de Dados

* Pandas
* NumPy

### Configuração

* python-dotenv

### Controle de Versão

* Git
* GitHub


---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd InvestAgent
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuração

Crie um arquivo `.env`:

```env
GROQ_API_KEY=sua_chave_groq
MODEL_NAME=llama-3.3-70b-versatile
```

---

## ▶️ Executando o Projeto

```bash
streamlit run app.py
```

---

## 📋 Exemplo de Resultado

### Quant Summary

```text
Ticker: AAPL
Regime: SIDEWAYS
Technical Score: 10
Trend Score: 54.8
Momentum Score: 25
Risk Score: 29.4
```

### AI Decision

```text
Recomendação: HOLD
Risco: BAIXO
Confiança: 60%

Justificativa:
O ativo apresenta regime lateral com momentum fraco e baixo risco.
Os indicadores técnicos não demonstram um setup claro para compra
ou venda neste momento.
```

---

## ⚠️ Aviso

Este projeto possui finalidade educacional e demonstrativa.

As análises geradas não constituem recomendação de investimento e não devem ser utilizadas como única base para decisões financeiras.

---

## 👨‍💻 Autor

**Luis Henrique Turra Ramos**

Projeto desenvolvido para demonstrar competências em:

* Data Science
* Python
* Engenharia de Dados
* IA Generativa
* Análise Quantitativa
* Desenvolvimento de Dashboards
* Integração de APIs
* Sistemas de Suporte à Decisão
