import csv
from datetime import datetime

# Part 1: Reading and Writing CSV Files using csv module

# Task 1: Reading Data from a CSV File
def read_data(file_path):
  # try-except block to handle exceptions
    # open the file in read mode
      # create a csv reader object
  data = []
      # add the rows to the data list
  return data
  # handle FileNotFoundError
  print("File not found.")
  # handle csv.Error
  print(f"CSV error: {e}")
  # if there is an error return None
  return None

# Task 2: Writing Data to a CSV File
def write_data(data, file_path, headers):
  # try-except block to handle exceptions
    # open the file in write mode
      # create a csv writer object (not the DictWriter object)
      # write the headers
      # write the data rows
  print(f"Data successfully written to {file_path}")
  # handle csv.Error
  print(f"CSV error: {e}")

# Task 3: Data Cleaning and Transformation
def clean_and_transform_data(file_path):
  # try-except block to handle exceptions
    # open the file in read mode
      # create a csv dictionary reader object
  cleaned_data = []
      # iterate over each row in the csv reader object
        # Remove leading and trailing spaces from 'Product' and 'Customer' columns

        # Remove leading and trailing spaces from 'Sales' column and convert to float

        # Transform 'Date' column to datetime object

        # add the row to the cleaned_data list
  return cleaned_data
  # handle FileNotFoundError
  print("File not found.")
  # handle csv.Error
  print(f"CSV error: {e}")
  # if there is an error return None
  return None

# Task 4: Data Aggregation and Analysis
def data_aggregation_and_analysis(data):
  # Calculate total sales
  total_sales = None
  # Calculate average sales
  average_sales = None
  # Find the row with the maximum sales
  max_sale = None
  # Find the row with the minimum sales
  min_sale = None
  return total_sales, average_sales, max_sale, min_sale

# Task 5: Data Filtering
def filter_and_select_data(file_path, category, min_quantity):
  # try-except block to handle exceptions
    # open the file in read mode
      # create a csv dictionary reader object
      # filter the data rows where the 'Category' column matches the category argument and the 'Quantity' column is less than the min_quantity argument
  filtered_data = []
  return filtered_data
  # handle FileNotFoundError
  print("File not found.")
  # handle csv.Error
  print(f"CSV error: {e}")
  # if there is an error return None
  return None
