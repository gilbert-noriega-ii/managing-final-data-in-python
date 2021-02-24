#Load pandas as pd.
#Use pd.read_csv() to load the file nasdaq-listings.csv into the variable nasdaq.
#Use .head() to display the first 10 rows of the data. Which data type would you expect pandas to assign to each column? What symbol is used to represent a missing value?
#Use .info() to identify dtype mismatches in the DataFrame summary. Specifically, are there any columns that should have a more appropriate type?


import pandas as pd

nasdaq = pd.read_csv('nasdaq-listings.csv')

print(nasdaq.head(10))

nasdaq.info()


#Read the file nasdaq-listings.csv into nasdaq with pd.read_csv(), adding the arguments na_values and parse_dates equal to the appropriate values. You should use 'NAN' for missing values, and parse dates in the Last Update column.
#Display and inspect the result using .head() and .info() to verify that the data has been imported correctly.


nasdaq = pd.read_csv('nasdaq-listings.csv', na_values ='NAN', parse_dates =['Last Update'])

print(nasdaq.head())

nasdaq.info()


#Read only the 'nyse' worksheet of 'listings.xlsx' where the symbol 'n/a' represents missing values. Assign the result to nyse.
#Display and inspect nyse with .head() and .info().


nyse = pd.read_excel('listings.xlsx', sheet_name = 'nyse', na_values = 'n/a')

print(nyse.head())

nyse.info()


#Create a pd.ExcelFile() object using the file 'listings.xlsx' and assign to xls.
#Save the sheet_names attribute of xls as exchanges.
#Using exchanges to specify sheet names and n/a to specify missing values in pd.read_excel(), read the data from all sheets in xls, and assign to a dictionary listings.
#Inspect only the 'nasdaq' data in this new dictionary with .info().


xls = pd.ExcelFile('listings.xlsx')

exchanges = xls.sheet_names

listings = pd.read_excel(xls, sheet_name = exchanges, na_values = 'n/a')

listings['nasdaq'].info()



#Import data in listings.xlsx from sheets 'nyse' and 'nasdaq' into the variables nyse and nasdaq, respectively. Read 'n/a' to represent missing values.
#Inspect the contents of both DataFrames with .info() to find out how many companies are reported.
#With broadcasting, create a new reference column called 'Exchange' holding the values 'NYSE' or 'NASDAQ' for each DataFrame.
#Use pd.concat() to concatenate the nyse and nasdaq DataFrames, in that order, and assign to combined_listings.

nyse = pd.read_excel('listings.xlsx', sheet_name = 'nyse', na_values = 'n/a')
nasdaq = pd.read_excel('listings.xlsx', sheet_name = 'nasdaq', na_values = 'n/a')

nyse.info()
nasdaq.info()

nyse['Exchange'] = 'NYSE'
nasdaq['Exchange'] = 'NASDAQ'

combined_listings = pd.concat([nyse, nasdaq]) 


#Create the pd.ExcelFile() object using the file listings.xlsx and assign to the variable xls.
#Retrieve the sheet names from the .sheet_names attribute of xls and assign to exchanges.
#Create an empty list and assign to the variable listings.
#Iterate over exchanges using a for loop with exchange as iterator variable. In each iteration:
#Use pd.read_excel() with xls as the the data source, exchange as the sheetname argument, and 'n/a' as na_values to address missing values. Assign the result to listing.
#Create a new column in listing called 'Exchange' with the value exchange (the iterator variable).
#Append the resulting listing DataFrame to listings.
#Use pd.concat() to concatenate the contents of listings and assign to listing_data.
#Inspect the contents of listing_data using .info().


xls = pd.ExcelFile('listings.xlsx')

exchanges = xls.sheet_names

listings = []

for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname = exchange, na_values = 'n/a')
    listing['Exchange'] = exchange
    listings.append(listing)

listing_data = pd.concat(listings)

listing_data.info()