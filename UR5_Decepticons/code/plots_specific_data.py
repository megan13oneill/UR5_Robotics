import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# 14.5.25 - 15:56
# 15.5.25 - 13.23.05 - row 3127
# 15.5.25 - 13:35:42, row 3238


# === Load CSV ===
df = pd.read_csv('RGB_values.csv')

# === Select Rows from 10 to 25 ===
selected_rows = df.iloc[10:26]

# === Plot Each Selected Row ===
for idx, row in selected_rows.iterrows():
    sample_id = row['Sample ID']
    
    # Assuming all columns except 'Sample ID' and 'Time' are values
    value_columns = [col for col in df.columns if col not in ['Sample ID', 'Time']]

    plt.figure(figsize=(6, 4))
    plt.plot(value_columns, row[value_columns].values, marker='o')
    plt.title(f'Sample ID: {sample_id} (Row {idx})')
    plt.xlabel('Measurement')
    plt.ylabel('Value')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'plot_row_{idx}_sample_{sample_id}.png')
    plt.show()

