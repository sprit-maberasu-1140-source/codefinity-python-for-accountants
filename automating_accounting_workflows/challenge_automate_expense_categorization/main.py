import pandas as pd

def categorize_expense(description):
    desc = description.lower()
    if "restaurant" in desc or "dining" in desc or "cafe" in desc:
        return "Meals & Entertainment"
    elif "uber" in desc or "taxi" in desc or "lyft" in desc or "transport" in desc:
        return "Travel"
    elif "office" in desc or "stationery" in desc or "supply" in desc:
        return "Office Supplies"
    elif "hotel" in desc or "lodging" in desc:
        return "Lodging"
    elif "airline" in desc or "flight" in desc:
        return "Travel"
    elif "software" in desc or "subscription" in desc:
        return "Software & Subscriptions"
    elif "utilities" in desc or "electric" in desc or "water" in desc:
        return "Utilities"
    elif "fuel" in desc or "gas" in desc:
        return "Automobile"
    else:
        return "Other"

def automate_expense_categorization(input_csv, output_csv):
    import os
    if not os.path.exists(input_csv):
        df = pd.DataFrame([
            {'Amount': 25.00, 'Description': 'Uber ride downtown'},
            {'Amount': 40.00, 'Description': 'Office stationery purchase'},
            {'Amount': 15.50, 'Description': 'Lunch at local cafe'},
            {'Amount': 120.00, 'Description': 'Hotel stay'},
            {'Amount': 10.00, 'Description': 'Monthly software subscription'},
            {'Amount': 30.00, 'Description': 'Electric utilities payment'},
            {'Amount': 17.00, 'Description': 'Fuel for company car'},
            {'Amount': 9.99, 'Description': 'Water utilities'},
            {'Amount': 50.00, 'Description': 'Flight to conference'},
            {'Amount': 20.00, 'Description': 'Dining with client'},
            {'Amount': None, 'Description': 'Taxi to airport'},
            {'Amount': 5.00, 'Description': None},
            {'Amount': 8.00, 'Description': 'Book purchase'}
        ])
        df.to_csv(input_csv, index=False)
    df = pd.read_csv(input_csv)
    df = df.dropna(subset=["Amount", "Description"])
    df["Category"] = df["Description"].apply(categorize_expense)
    summary = df.groupby("Category")["Amount"].sum().reset_index()
    summary.to_csv(output_csv, index=False)
    return summary

input_csv = "expenses_raw.csv"
output_csv = "expense_summary.csv"
summary = automate_expense_categorization(input_csv, output_csv)
print(summary)