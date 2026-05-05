'''import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)


print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
'''
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)


# Ensure that the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a new column for total sales (Quantity * Price)
df['Total_Sales'] = df['Quantity'] * df['Price']

# Extract the month and year from the 'Date' column
df['Month'] = df['Date'].dt.to_period('M')

# Group the data by 'Month' and sum the total sales for each month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# Find the month with the highest total sales
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()


print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
