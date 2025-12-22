def trade_recommendation(analysis):
    score = 0

    if analysis["trend"] == "Bullish":
        score += 40
    if analysis["momentum"] == "Strong":
        score += 30
    if analysis["volatility"] == "Normal":
        score += 30

    if score >= 70:
        action = "BUY"
    elif score >= 40:
        action = "HOLD"
    else:
        action = "SELL"

    risk = "Low" if score >= 70 else "Medium" if score >= 40 else "High"

    return {
        "risk_score": score,
        "action": action,
        "risk_level": risk
    }
