import pandas as pd

# Path to the Excel file
excel_file = 'sample_ecommerce_data.xlsx'
# Path where the CSV file will be saved
csv_file = 'sample_ecommerce_data.csv'

# Read the Excel file
df = pd.read_excel(excel_file, engine='openpyxl')  # Specify engine if needed

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False)
