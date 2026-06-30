def detect_market_regime(ind):

    trend_strength = abs(ind["ema20"] - ind["ema50"]) / ind["ema50"]

    if ind["volatility"] > 0.35:
        return "VOLATILE"

    if trend_strength > 0.03:
        return "TRENDING"

    return "SIDEWAYS"
def technical_score_v2(ind, regime):

    score = 50

    ema_signal = 1 if ind["ema20"] > ind["ema50"] else -1
    macd_signal = 1 if ind["macd"] > ind["signal"] else -1

    rsi = ind["rsi"]

    # =========================
    # TRENDING MARKET
    # =========================
    if regime == "TRENDING":

        score += ema_signal * 25
        score += macd_signal * 25

        if 40 <= rsi <= 70:
            score += 10

        elif rsi > 80 or rsi < 20:
            score -= 10

    # =========================
    # SIDEWAYS MARKET
    # =========================
    elif regime == "SIDEWAYS":

        score += ema_signal * 5     
        score += macd_signal * 25   

        if 45 <= rsi <= 60:
            score += 25
        else:
            score -= 20

        # penaliza tendência falsa
        if abs(ind["ema20"] - ind["ema50"]) / ind["ema50"] < 0.01:
            score += 5

    # =========================
    # VOLATILE MARKET
    # =========================
    elif regime == "VOLATILE":

        # risco domina tudo
        score += macd_signal * 10
        score -= abs(ind["volatility"]) * 40

        if rsi > 70:
            score -= 20
        elif rsi < 30:
            score -= 20

    return max(0, min(100, score))


def trend_score_v2(ind, regime):

    gap = (ind["ema20"] - ind["ema50"]) / ind["ema50"]

    if regime == "TRENDING":
        score = 50 + gap * 800
    else:
        score = 50 + gap * 400

    return max(0, min(100, score))


def momentum_score_v2(ind, regime):

    score = 50

    rsi = ind["rsi"]

    macd = 1 if ind["macd"] > ind["signal"] else -1

    price_above_ema = 1 if ind["price"] > ind["ema20"] else -1

    if regime == "TRENDING":

        score += macd * 30
        score += price_above_ema * 20

        if rsi > 60:
            score += 10
        elif rsi < 40:
            score -= 10

    elif regime == "SIDEWAYS":

        score += macd * 15

        if 45 <= rsi <= 55:
            score += 20
        else:
            score -= 10

    elif regime == "VOLATILE":

        score += macd * 10
        score -= abs(ind["volatility"]) * 30

    return max(0, min(100, score))
def risk_score_v2(ind, regime):

    vol = ind["volatility"]
    atr_pct = (ind["atr"] / ind["price"])

    base_risk = vol * 100 + atr_pct * 200

    if regime == "TRENDING":
        base_risk *= 0.8

    elif regime == "SIDEWAYS":
        base_risk *= 1.0

    elif regime == "VOLATILE":
        base_risk *= 1.4

    return max(0, min(100, base_risk))