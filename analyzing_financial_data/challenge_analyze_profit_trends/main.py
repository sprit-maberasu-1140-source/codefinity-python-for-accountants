import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_profit_trends(csv_file):
    # If the file does not exist, create a sample for demonstration (for notebook/test environments)
    if not os.path.exists(csv_file):
        data = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            'Revenue': [1000, 1200, 1100, 1300, 1250],
            'Expenses': [700, 800, 900, 850, 1000],
        }
        pd.DataFrame(data).to_csv(csv_file, index=False)
    df = pd.read_csv(csv_file)
    df['Profit'] = df['Revenue'] - df['Expenses']
    df['Profit_MA'] = df['Profit'].rolling(window=3, min_periods=1).mean()
    months = df['Month']
    profits = df['Profit']
    moving_averages = df['Profit_MA']
    plt.figure(figsize=(10, 5))
    plt.plot(months, profits, label='Monthly Profit', marker='o')
    plt.plot(months, moving_averages, label='3-Month Moving Average', linestyle='--')
    plt.xlabel('Month')
    plt.ylabel('Profit')
    plt.title('Monthly Profit and Moving Average')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Sample call
analyze_profit_trends('monthly_data.csv')
