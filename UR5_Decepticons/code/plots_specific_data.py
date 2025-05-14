import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def GraphPlotter():
    """ will take values from csv and plot them. e.g. sample 1 colour intensity over time."""
    csv_file = "RGV_values.csv"
    output_dir = "graphs_outputted"

    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])

if ""




    



# Simulate multiple iterations: Let's say you're grouping by some column like 'Category'
# For this example, assume your CSV has: Date, Value, Category

if 'Category' in df.columns:
    grouped = df.groupby('Category')
    for category, group_df in grouped:
        plt.figure(figsize=(10, 6))
        plt.plot(group_df['Date'], group_df['Value'], marker='o', linestyle='-')
        plt.title(f'Value over Time - {category}')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.grid(True)
        plt.tight_layout()

        # Create a safe filename
        filename = f"{category.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(output_dir, filename)
        plt.savefig(filepath)
        print(f"Saved: {filepath}")
        plt.close()
else:
    # If no grouping, just plot once
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Value'], marker='o', linestyle='-')
    plt.title('Value over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.tight_layout()

    filename = f"plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    print(f"Saved: {filepath}")
    plt.close()





