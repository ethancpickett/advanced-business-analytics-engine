import logging
import math

# Configure logging for the advanced analytics engine
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_dupont_analysis(net_income, revenue, total_assets, shareholders_equity):
    """
    Computes the 3-step DuPont Analysis for Return on Equity (ROE).
    Components:
    1. Net Profit Margin = Net Income / Revenue
    2. Asset Turnover = Revenue / Total Assets
    3. Equity Multiplier = Total Assets / Shareholders' Equity
    ROE = Net Profit Margin * Asset Turnover * Equity Multiplier
    """
    try:
        net_profit_margin = net_income / revenue if revenue else 0
        asset_turnover = revenue / total_assets if total_assets else 0
        equity_multiplier = total_assets / shareholders_equity if shareholders_equity else 0

        roe = net_profit_margin * asset_turnover * equity_multiplier

        logging.info(f"DuPont calculated: NPM={net_profit_margin:.4f}, AT={asset_turnover:.4f}, EM={equity_multiplier:.4f} -> ROE={roe:.4f}")

        return {
            "net_profit_margin": round(net_profit_margin, 4),
            "asset_turnover": round(asset_turnover, 4),
            "equity_multiplier": round(equity_multiplier, 4),
            "roe": round(roe, 4)
        }
    except Exception as e:
        logging.error(f"Error in DuPont analysis calculation: {e}")
        raise

def calculate_liquidity_ratios(current_assets, current_liabilities, inventory=0):
    """
    Computes baseline operational liquidity ratios:
    - Current Ratio = Current Assets / Current Liabilities
    - Quick Ratio = (Current Assets - Inventory) / Current Liabilities
    """
    try:
        current_ratio = current_assets / current_liabilities if current_liabilities else 0
        quick_ratio = (current_assets - inventory) / current_liabilities if current_liabilities else 0

        logging.info(f"Liquidity computed: Current Ratio={current_ratio:.2f}, Quick Ratio={quick_ratio:.2f}")
        return {
            "current_ratio": round(current_ratio, 2),
            "quick_ratio": round(quick_ratio, 2)
        }
    except Exception as e:
        logging.error(f"Error in liquidity ratio calculation: {e}")
        raise

def detect_anomalies(data_series, threshold=2.0):
    """
    Detects statistical anomalies (outliers) in a financial time series using Z-scores.
    Z = (x - mean) / std_dev
    Returns items that exceed the absolute threshold.
    """
    if not data_series:
        return []

    n = len(data_series)
    mean = sum(data_series) / n

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data_series) / n
    std_dev = math.sqrt(variance)

    anomalies = []
    for item in data_series:
        if std_dev == 0:
            z_score = 0
        else:
            z_score = (item - mean) / std_dev

        if abs(z_score) >= threshold:
            anomalies.append({
                "value": item,
                "z_score": round(z_score, 2)
            })

    logging.info(f"Anomaly detection complete. Found {len(anomalies)} anomalies at threshold {threshold}.")
    return anomalies
