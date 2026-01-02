# Data manipulation means transforming, cleaning, and organizing data to make it suitable for analysis. In the context of using the Pandas library in Python, data manipulation involves various operations such as filtering, sorting, aggregating, merging, and reshaping data stored in DataFrames and Series. These operations help in preparing the data for further analysis, visualization, or modeling by ensuring that it is in the right format and structure. Pandas provides a wide range of functions and methods to facilitate efficient data manipulation tasks.
# Data analysis, on the other hand, refers to the process of examining, interpreting, and drawing insights from data. It involves exploring the data to identify patterns, trends, and relationships, as well as performing statistical analyses to test hypotheses or make predictions. Data analysis often includes summarizing data using descriptive statistics, visualizing data through charts and graphs, and applying various analytical techniques to extract meaningful information that can inform decision-making. 
  
import pandas as pd

#read data from a CSV file into a DataFrame
# df = pd.read_csv('filename.csv')

#read data from an Excel file into a DataFrame
# df = pd.read_excel('filename.xlsx')

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df)

df.to_csv('output.csv', index=False) #index false to avoid writing row numbers
df.to_excel('output.xlsx', index=False) #index false to avoid writing row numbers   

#df.head()  # Display the first few rows of the DataFrame
#df.tail()  # Display the last few rows of the DataFrame 


#info()  # Get a summary of the DataFrame, including data types and non-null counts
# 1) number of rows and columns
# 2) column names
# 3) data types of each column
# 4) non null counts 
# 5) memory usage of the DataFrame

print(df.info())

#describe()  # Generate descriptive statistics for numerical columns
print(df.describe())

# df.shape  # Get the dimensions of the DataFrame (rows, columns)
# df.columns  # Get the column names of the DataFrame

# selecting columns
# - a series
# -dataframe multiple columns of data 

column = df['Column Name']  # Select a single column as a Series
subset = df[["Column", "Column2"]]    # Select multiple columns as a DataFrame 

# filtering rows
# boolean indexing

#based on simgle condition
filtered_df = df[df['Age'] > 25]  # Filter rows where Age is greater than  25 

#based on multiple conditions
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'New York')]  # Filter rows based on multiple 


data ={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Names (single column return series):")
name = df['Name']
print(name)


subset = df[['Name', 'City']]
print("Subset (multiple columns return DataFrame):")
print(subset)

high_Age = df[df['Age'] > 25]
print("Filtered DataFrame (Age > 25):")
print(high_Age)


#add a new column
df['New_Age'] = df['Age'] + 5
print("DataFrame after adding New_Age column:")
print(df)

#adding column at a specific location by Insert method
#df.insert(loc,"Column Name", data)

df.insert(0,"Employee_ID", [101, 102, 103, 104, 105])

#update existing column values
#df.loc[row_index, 'Column Name'] = new_value
df.loc[0, 'Age'] = 25  # Update Age for the first row

#update existing column
df['City'] = df['City'].str.upper()  # Convert all city names to uppercase 

#removing
df = df.drop('New_Age', axis=1)  # Remove the 'New_Age' column
#here axis=1 indicates that we are dropping a column. For rows, use axis=0
#by default if axis is not specified, it is considered as 0.

df.drop(columns=['Employee_ID'], inplace=True) #removing column using columns parameter
#inplace=True to make changes in the original dataframe.


#handle missing data
#NaN (Not a Number) represents missing values in Pandas 
#None (for object data types) also represents missing values
data_with_nan = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [24, None, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', None]
}

df = pd.DataFrame(data_with_nan)
print(df)
print(df.isnull().sum())  


df.dropna(inplace=True)  # Remove rows with any missing values 
#Output : data_with_nan dataframe will have only rows with complete data

df.fillna(0, inplace=True)  # Fill missing values with 0
df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'}, inplace=True)  # Fill missing values



df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill missing values in 'Age' with the mean age
print(df)

#Interpolation - estimating missing values based on surrounding data points

#Linear interpolation
# preserve data integrity by estimating missing values based on existing data points.
# smooth trends in time series data by filling gaps with interpolated values.
#avoid data loss that can occur with row/column removal methods.

#linear, polynomial, time, spline, index, nearest, zero, quadratic, cubic

data = {
    'Time': [1, 2, 3, 4, 5],
    'Value': [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print(df)

# Interpolate missing values
df['Value'].interpolate(method='linear', inplace=True)
print(df)

#disadvantage of interpolation
# Assumes a specific pattern in the data that may not be accurate.
# May introduce bias if the underlying data distribution is not considered.
# Not suitable for categorical data or non-numeric columns.

#Sorting and aggregation
#df.sort_values(by='Column Name', ascending=True, inplace=True)  # Sort DataFrame by a specific column in ascending order

data= {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Salary': [50000, 60000, 55000, 70000]
}
df.sort_values(by='Age', ascending=False, inplace=True)  # Sort DataFrame by 'Age' in descending order

df.sort_values(by=['Age', 'Salary'], ascending=[True, False], inplace=True)  # Sort by 'Age' ascending and 'Salary' descending  


#aggregation - combining multiple values into a single summary value
#summary statistics - mean, median, sum, count, min, max, std (standard deviation), var (variance)
mean_age = df['Age'].mean()  # Calculate the mean of the 'Age' column


#grouping data
#groupby() method is used to group data based on one or more columns and perform aggregate functions on the grouped data.
grouped = df.groupby('City')['Salary'].mean()  # Group by 'City' and calculate the mean 'Salary' for each city
print(grouped)


#mergeing and joining
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df_orders = pd.DataFrame({
    'OrderID': [101, 102, 103], 
    'CustomerID': [1, 2, 4,],
    'Amount': [250, 150, 300]
})

merged_df = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')  # Inner join on 'CustomerID'


#joining vertically

df_region1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [24, 27]
})
df_region2 = pd.DataFrame({
    'Name': ['Charlie', 'David'],   
    'Age': [22, 32]
})

df_concatenated = pd.concat([df_region1, df_region2], axis =1, ignore_index=True)  # Concatenate DataFrames vertically 
