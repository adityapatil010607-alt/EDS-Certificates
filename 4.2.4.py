import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# Group products sold by each date
date_groups = df.groupby('Date')['Product'].apply(list)

# Count product pairs
pair_counter = Counter()

for products in date_groups:
	unique_products = set(products)
	pairs = combinations(sorted(unique_products), 2)
	pair_counter.update(pairs)

# Find the maximum frequency of any product pair
if pair_counter:
	max_count = max(pair_counter.values())

	# Get all product pairs with the maximum frequency
	most_common_pairs = [pair for pair, count in pair_counter.items() if count == max_count]
	
	# Print the most common product pairs in sorted order
	for pair in sorted(most_common_pairs):
		print(f"{pair[0]} and {pair[1]}: {max_count} times")

