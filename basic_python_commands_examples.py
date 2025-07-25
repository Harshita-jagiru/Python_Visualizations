# -*- coding: utf-8 -*-
"""Basic_python_commands_examples.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/152IUdwrSe2h3szpYF7Despzx0rIwCe45
"""

import pandas as pd

df=pd.read_csv('Salaries.csv')

# data is stored in the form of a data frame
type(df)

df

# to display first 5 records in dataset
df.head()

# to display bottom 5 records in dataset
df.tail()

df.shape

#to display names of columns
df.columns

# to display the data types
df.dtypes

# to get information about null values in dataset
df.info()

#to
df.describe()

# prompt: can you use the head fucntion on the above data and tell me the first 5 record in the dataset

print(df.head(10))

# prompt: can you find out the shape of the above dataset

df.shape

# prompt: can you tell me about what are the names of the columns in this dataset

df.columns

# to decribe basic stats infor on numerical columns
df.describe()

# to
df.mean(numeric_only=True)

df['salary']

# to find out the mean value for salary column
df['salary'].mean()

df['salary'].median()

df['salary'].mode()

df[['salary','service','phd']]

df['salary'].var()

df['salary'].std()

df['salary'].min()

df['salary'].max()

# prompt: i want to select 2 columns salary and service from the above dataset

df[['salary','service']]

# prompt: find out the variance of salary, service column

df[['salary','service']].var()

# prompt: to find out the std of salary column

df['salary'].std()

df['salary'].skew()

df['salary'].kurt()

# prompt: find put the skewness and kurtosis in salary column

print("Skewness:", df['salary'].skew())
print("Kurtosis:", df['salary'].kurt())

df.isnull()

pd.set_option('display.max_rows',None)

# prompt: i want to see al lthe records in my dataset , it is ony showing me first 5 records and last five records

pd.set_option('display.max_rows', None)
df

df.isnull().sum()

# prompt: i wnat to confirm if there are any null values in my dataset , in every column

df.isnull().sum()

# prompt: to find ou the max value and min vaue in salary column

print("Maximum salary:", df['salary'].max())
print("Minimum salary:", df['salary'].min())