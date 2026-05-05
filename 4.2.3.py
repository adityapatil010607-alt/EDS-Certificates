import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# Group the data by 'City' and sum the 'Quantity' for each city
city_sales = df.groupby('City')['Quantity'].sum()

# Find the city that sold the most products
best_city = city_sales.idxmax()

# Display the result
print(f"City sold the most products: {best_city}")
