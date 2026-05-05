import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# 1. Display the first 5 rows of the dataset
print(data.head())

# 2. Display the last 5 rows of the dataset

print(data.tail())

# 3. Get the shape of the dataset (number of rows and columns)

print(data.shape)

# 4. Get a summary of the dataset using .info()
data.info()

# 5. Get basic statistics (mean, standard deviation, etc.) of the dataset using .describe()
print("None")
print(data.describe())

# 6. Check for missing values and display the count of missing values for each column
print(data.isnull().sum())

# 7. Fill missing values in the 'Age' column with the median age
median_age =data['Age'].median()
data['Age'].fillna(median_age, inplace=True)

# 8. Fill missing values in the 'Embarked' column with the most frequent value (mode)
mode_embarked = data['Embarked'].mode()[0]
data['Embarked'].fillna(mode_embarked, inplace=True)

# 9. Drop the 'Cabin' column due to many missing values
data.drop(columns=['Cabin'], inplace=True)

# 10. Create a new column 'FamilySize' by adding the 'SibSp' and 'Parch' columns
data['FamilySize'] = data['SibSp'] + data['Parch']

