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