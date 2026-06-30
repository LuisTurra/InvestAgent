import yfinance as yf

def get_company_info(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap")
    }