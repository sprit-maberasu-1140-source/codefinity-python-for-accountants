import pandas as pd

def fetch_market_data(symbol: str, days: int = 5) -> pd.DataFrame:
    """
    Mock function for testing: returns a DataFrame with 'Close' and 'Volume' columns
    """
    data = {
        'Close': [100.0, 102.5, 101.0, 103.0, 104.5],
        'Volume': [2000, 2200, 2100, 2300, 2400]
    }
    return pd.DataFrame(data)

# Complete this function:
def market_impact_report(symbol: str) -> dict:
    """
    Returns a dictionary with keys:
        'average_close': average of closing prices over last 5 business days
        'total_volume': total traded volume over last 5 business days
        'max_close': maximum closing price over last 5 business days
    Use fetch_market_data(symbol) to get the data.
    """
    df = fetch_market_data(symbol)
    average_close = float(df['Close'].mean())
    total_volume = int(df['Volume'].sum())
    max_close = float(df['Close'].max())

    return {
        'average_close': average_close,
        'total_volume': total_volume,
        'max_close': max_close
    }

# Testing
report = market_impact_report("AAPL")
print("Market Impact Report for AAPL:")
print(f"  Average Close: {report['average_close']}")
print(f"  Total Volume:  {report['total_volume']}")
print(f"  Max Close:     {report['max_close']}")