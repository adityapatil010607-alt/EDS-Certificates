import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])





# Display the first five rows of the data frame
print("First five rows:")
print(data.head())

# Calculate the average age of the students (limit to 2 decimal places)
average_age = round(data['Age'].mean(), 2)
print("Average age:", average_age)

# Filter out the students who have a grade above a certain threshold ('B')
filtered_data = data[data['Grade'] <= 'B']
print("Students with a grade up to B")
print(filtered_data)


