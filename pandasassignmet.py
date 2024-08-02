import pandas as pd
#1. ***exercise1***
df = pd.read_csv("iris.csv")
#print(df)

#Display the first 10 rows of the dataset.
#print(df.head(10))

#Display the data types of each column
#print(df.dtypes)


#2. ***exercise2***
#Calculate summary statistics for each feature.
#print(df.describe())

#Calculate the mean sepal length for each species.

#print(df['Sepal.Length'].agg(['mean']))

#3. Exercise 3: Data Cleaning
# print("Missing values in each column before imputation:")
# print(df.isnull().sum())

# Identify numeric columns
#numeric_columns = df.select_dtypes(include='number').columns

# Replace missing values in numeric columns with the mean of each column
#df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Verify that there are no missing values left
#print("\nMissing values in each column after imputation:")
#print(df.isnull().sum())

#  ***Exercise 4: Data Filtering***
#df_filtered = df[df['Sepal.Length']>5.0]
#print(df_filtered)

# df_setosa = df[df['Species'] == 'setosa']
# print(df_setosa)
# print("Filtered dataset shape:", df_setosa.shape)


#5.1
#print(df.groupby('Species')['Petal.Length'].agg(['mean', 'median', 'std']))
#5.2
#print(df['Species'].value_counts())
#5.3
#print(df.groupby('Species')['Petal.Width'].agg(['min', 'max']))
#5.4
print(df.groupby('Species')['Sepal.Width'].mean().sort_values(ascending=False).head(5))











