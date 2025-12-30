import pandas as pd

file = 'battledeath.xlsx'
# Read the Excel file into a DataFrame: df
# df = pd.read_excel(file)
# df = pd.read_csv(file)

xls = pd.ExcelFile(file)
# df = pd.read_excel(xls, '2004')
print(xls.sheet_names)
# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004') 

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())