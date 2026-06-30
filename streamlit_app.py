import streamlit as st
import re

from data.market import get_stock_data
from indicators.technicals import calculate_indicators

from scoring.scores import (
    detect_market_regime,
    technical_score_v2,
    trend_score_v2,
    momentum_score_v2,
    risk_score_v2
)

from llm.groq_agent import analyze
from utils.formatters import format_financial
from config import GROQ_API_KEY, MODEL_NAME

st.set_page_config(
    page_title="InvestAgent Terminal",
    layout="wide",
    page_icon="assets/logo.png",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #e6edf3;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    h1, h2, h3 {
        color: #00ff88;
    }

    div[data-testid="metric-container"] {
        background-color: #161b22;
        border: 1px solid #2a2f3a;
        border-radius: 10px;
        padding: 12px;
    }

    .stButton>button {
        background-color: #00ff88;
        color: black;
        font-weight: bold;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


st.title("📊 INVEST AGENT TERMINAL")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in environment or Streamlit secrets")

ticker = st.text_input("TICKER", "AAPL").upper().strip()
if not re.match(r"^[A-Z]{1,6}$", ticker):
    st.error("Ticker inválido (use apenas letras, ex: AAPL)")
    st.stop()

def color_score(v):
    if v >= 70:
        return "🟢"
    elif v >= 40:
        return "🟡"
    return "🔴"

if st.button("ANALISAR MERCADO"):

    st.info("⏳ O sistema está coletando dados de mercado e executando análise quantitativa...")

    try:
        df = get_stock_data(ticker)
    except Exception as e:
        st.error("⚠️ ERRO AO ACESSAR DADOS DE MERCADO")
        st.warning(str(e))
        st.stop()

    ind = calculate_indicators(df)
    regime = detect_market_regime(ind)

    summary = {
        "ticker": ticker,
        "price": ind["price"],
        "regime": regime,

        "technical_score": technical_score_v2(ind, regime),
        "trend_score": trend_score_v2(ind, regime),
        "momentum_score": momentum_score_v2(ind, regime),
        "risk_score": risk_score_v2(ind, regime),

        "facts": {
            "rsi": ind["rsi"],
            "macd": ind["macd"],
            "signal": ind["signal"],
            "ema20": ind["ema20"],
            "ema50": ind["ema50"],
            "volatility": ind["volatility"],
        }
    }

    result = analyze(summary)

    st.subheader(f"📌 VISÃO GERAL - {ticker}")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("PREÇO", format_financial(ind["price"]))
    c2.metric("REGIME", regime)
    c3.metric("RISCO", result["risk"])
    c4.metric("CONFIANÇA", f"{result['confidence']}%")

    st.divider()

    st.subheader("📈 EVOLUÇÃO DO PREÇO")

    chart_data = df["Close"].copy()
    st.line_chart(chart_data)

    st.divider()

    st.subheader("📊 MOTOR QUANTITATIVO")

    tech = summary["technical_score"]
    trend = summary["trend_score"]
    mom = summary["momentum_score"]
    risk = summary["risk_score"]

    q1, q2, q3, q4 = st.columns(4)

    q1.metric("TÉCNICO", f"{format_financial(tech)} {color_score(tech)}")
    q2.metric("TENDÊNCIA", f"{format_financial(trend)} {color_score(trend)}")
    q3.metric("MOMENTUM", f"{format_financial(mom)} {color_score(mom)}")
    q4.metric("RISCO", f"{format_financial(risk)} {color_score(100 - risk)}")

    st.divider()

    st.subheader("🧠 ANÁLISE DA IA")

    colA, colB = st.columns([1, 2])

    with colA:
        st.success(result["recommendation"])

    with colB:
        st.write(result["reasoning"])

    st.divider()

    st.subheader("📌 DADOS TÉCNICOS")

    f = summary["facts"]

    f1, f2, f3 = st.columns(3)

    f1.write(f"RSI: {format_financial(f['rsi'])}")
    f1.write(f"MACD: {format_financial(f['macd'])}")

    f2.write(f"EMA20: {format_financial(f['ema20'])}")
    f2.write(f"EMA50: {format_financial(f['ema50'])}")

    f3.write(f"VOLATILIDADE: {format_financial(f['volatility'])}")
    f3.write(f"SINAL: {format_financial(f['signal'])}")