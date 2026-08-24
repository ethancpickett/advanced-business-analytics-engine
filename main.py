from src.analytics_engine import calculate_dupont_analysis, calculate_liquidity_ratios, detect_anomalies

def run_advanced_analytics():
    print("--- Executing Advanced Business Analytics Engine ---")

    # 1. DuPont Analysis Evaluation
    net_income = 150000
    revenue = 1000000
    total_assets = 800000
    shareholders_equity = 400000

    dupont_results = calculate_dupont_analysis(net_income, revenue, total_assets, shareholders_equity)
    print(f"DuPont Analysis Results: {dupont_results}")

    # 2. Liquidity Ratios Evaluation
    current_assets = 250000
    current_liabilities = 150000
    inventory = 50000

    liquidity_results = calculate_liquidity_ratios(current_assets, current_liabilities, inventory)
    print(f"Liquidity Ratios: {liquidity_results}")

    # 3. Statistical Anomaly Detection (e.g., tracking monthly operational expenses)
    monthly_expenses = [42000, 43500, 41000, 42500, 78000, 43000, 41500]
    anomalies = detect_anomalies(monthly_expenses, threshold=2.0)
    print(f"Detected Expense Anomalies: {anomalies}")

    print("--- Advanced Analytics Engine Execution Completed Successfully ---")

if __name__ == "__main__":
    run_advanced_analytics()
