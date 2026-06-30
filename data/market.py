import yfinance as yf
import pandas as pd


def get_stock_data(ticker: str):
    
    try:
        if not ticker or not isinstance(ticker, str):
            raise ValueError("Ticker inválido")

        ticker = ticker.upper().strip()

        data = yf.Ticker(ticker)

        hist = data.history(period="6mo")

        # =========================
        # validações de segurança
        # =========================
        if hist is None:
            raise ValueError("yfinance retornou None")

        if isinstance(hist, pd.DataFrame) and hist.empty:
            raise ValueError(f"Sem dados para o ticker: {ticker}")

        required_cols = ["Close", "Open", "High", "Low"]

        for col in required_cols:
            if col not in hist.columns:
                raise ValueError(f"Coluna ausente no yfinance: {col}")

        # limpa NaNs críticos
        hist = hist.dropna()

        if len(hist) < 30:
            raise ValueError("Dados insuficientes para análise (mínimo 30 candles)")

        return hist

    except Exception as e:
        # NÃO deixa o Streamlit quebrar
        raise RuntimeError(f"Erro ao buscar dados de mercado ({ticker}): {str(e)}")