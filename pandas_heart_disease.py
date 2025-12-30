import pandas as pd
import numpy as np

"""
    Using pandas to import flat files as DataFrames (2)
In the last exercise, you were able to import flat files containing columns with different datatypes as numpy arrays. 
However, the DataFrame object in pandas is a more appropriate structure in which to store such data and, thankfully,    
we can easily import files of mixed data types as DataFrames using the pandas functions read_csv() and read_table().
"""

# Assign the filename: file
file = 'Heart_Disease_Prediction.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# Print the head of the DataFrame df
print(df.head())

# Print the info of the DataFrame df
print(df.info())

# Print the column names of the DataFrame df
print(df.columns)

# Print the shape of the DataFrame df
print(df.shape)

# convert dataframe to numpy array
data = df.to_numpy()
data = np.array(df)

print(data)

# Print the datatype of data
print(type(data))
# Print the shape of data
print(data.shape)

# Select the 'age' column from df and print its datatype
age = df['age']
print(type(age))

