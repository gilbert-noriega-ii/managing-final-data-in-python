#Import the DataReader from pandas_datareader.data and date from the datetime library.
#Using date(), set the start date to January 1, 2016 and end date to December 31, 2016.
#Set ticker to Apple's stock ticker 'AAPL' and data_source to 'iex'.
#Create a DataReader() object to import the stock prices and assign to a variable stock_prices.
#Use .head() and .info() to display and inspect the result.

from pandas_datareader.data import DataReader

from datetime import date

start = date(2016, 1, 1)
end = date(2016,12,31)

ticker = 'AAPL'

data_source = 'iex'

stock_prices = DataReader(ticker, data_source, start, end)

print(stock_prices.head())
stock_prices.info()


#Import matplotlib.pyplot as plt.
#Using date(), set the start and end dates to January 1, 2016 and December 31, 2016, respectively.
#Set ticker to Facebook's stock ticker 'FB' and data_source to 'iex'.
#Create a DataReader() object to import the stock prices and assign to stock_prices.
#Plot the 'close' data in stock_prices, set ticker as the title, and show the result.


import matplotlib.pyplot as plt

start = date(2016, 1, 1)
end = date(2016, 12, 31)

ticker = 'FB'
data_source = 'iex'

stock_prices = DataReader(ticker, data_source, start, end)

stock_prices['close'].plot(title = ticker)
plt.show()


#Use date() to set start to January 1, 1968, and set series to series code 'GOLDAMGBD228NLBM'.
#Pass series as the data,'fred' as the data source, and start as the start date to DataReader(). Assign to gold_price.
#Inspect gold_price using .info().
#Plot and show the gold_price series with title 'Gold Price'.


start = date(1968, 1, 1)

series = 'GOLDAMGBD228NLBM'

gold_price = DataReader(series, 'fred', start=start)

gold_price.info()

gold_price.plot(title = "Gold Price")

plt.show()


#Using date(), set start to January 1, 1950.
#Create series as a list containing the series codes 'UNRATE' and 'CIVPART', in that order.
#Pass series, the data source 'fred', and the start date to DataReader(), and assign the result to econ_data.
#Use the .columns attribute to assign 'Unemployment Rate' and 'Participation Rate' as the new column labels.
#Plot and show econ_data using the subplots=True argument, and title it 'Labor Market'.


start = date(1950, 1, 1)

series = ['UNRATE', 'CIVPART']

econ_data = DataReader(series, 'fred', start=start)

econ_data.columns = ['Unemployment Rate', 'Participation Rate']

econ_data.plot(subplots = True, title = 'Labor Market')

plt.show()


#Using date(), set the start date to January 1, 2008.
#Set the series codes as a list containing 'BAMLHYH0A0HYM2TRIV' and 'SP500'.
#Use DataReader() to import both series from 'fred' and assign to data.
#Plot and show data with subplots, titled 'Performance Comparison'.


start = date(2008, 1, 1)

series = ['BAMLHYH0A0HYM2TRIV', 'SP500']

data = DataReader(series, 'fred', start=start)

data.plot(subplots = True, title = "Performance Comparison")

plt.show()


#Without using .loc[], filter listings based on the condition that the 'Sector' is equal to 'Consumer Services' and assign to consumer_services.
#Sort consumer_services by 'Market Capitalization' in descending order and assign it to consumer_services2.
#Using .head(), display the first 5 rows of the 'Company Name', 'Exchange', and 'Market Capitalization' columns.


consumer_services = listings[listings.Sector == 'Consumer Services']

consumer_services2 = consumer_services.sort_values('Market Capitalization', ascending=False)

print(consumer_services2[['Company Name', 'Exchange', 'Market Capitalization']].head())


#Use .loc[] to filter rows where 'Sector' is equal to 'Consumer Services', select the column 'Market Capitalization', and apply .idxmax() to assign the ticker of the largest Consumer Services company to ticker.
#Using date(), set start to January 1, 2015.
#Use DataReader() to extract the stock data for the ticker from 'iex' since start and store in data.
#Plot the 'close' and 'volume' values in data, with arguments secondary_y='volume' and title=ticker.


listings_ss = listings.set_index('Stock Symbol')

ticker = listings_ss.loc[listings_ss.Sector == 'Consumer Services', 'Market Capitalization'].idxmax()

start = date(2015, 1, 1)

data = DataReader(ticker, 'iex', start= start)

data[['close', 'volume']].plot(secondary_y='volume', title=ticker)

plt.show()


#Set 'Stock Symbol' as the index for listings.
#Use .loc[] to filter rows where 'Sector' is 'Consumer Services' and IPO Year starting 1998, and also select the 'Market Capitalization' column. Apply .idxmax() and assign the result to ticker.
#Set the start date to January 1, 2015.
#Use the DataReader to get the stock data for the ticker from 'iex' since start.
#Plot the 'close' and 'volume' prices of this company, using 'volume' for secondary_y and ticker as the title.


listings = listings.set_index('Stock Symbol')

ticker = listings.loc[(listings.Sector == 'Consumer Services') & (listings['IPO Year'] > 1998), 'Market Capitalization'].idxmax()

start = date(2015, 1, 1)

data = DataReader(ticker, 'iex', start=start)

data[['close', 'volume']].plot(secondary_y = 'volume', title = ticker)

plt.show()


#Set 'Stock Symbol' as the index for listings, assigning it to listings_ss.
#Use .loc[] to filter rows where the company sector is 'Finance'and extract the 'Market Capitalization' column. Apply .nlargest() to assign the 3 largest companies by market cap to top_3_companies.
#Convert the index of the result to a list and assign it to top_3_tickers.
#Use date() to set start to January 1, 2015.
#Use date() to set end to April 1, 2020.
#Use the DataReader() to get the stock data for the top_3_tickers from 'iex' since start until end and assign it to result.
#We are then creating a DataFrame by iterating over the ticker-data pairs and create a MultiIndex by appending 'ticker' to 'date' in the Index.
#Select 'close' from data, apply .unstack(), and inspect the resulting DataFrame, now in wide format, with .info().


listings_ss = listings.set_index('Stock Symbol')

top_3_companies = listings_ss.loc[listings_ss.Sector == 'Finance', 'Market Capitalization'].nlargest(n=3)

top_3_tickers = top_3_companies.index.to_list()

start = date(2015, 1, 1)

end = date(2020, 4, 1)

result = DataReader(top_3_tickers, 'iex', start, end)
result = result[~result.index.duplicated()]
data = pd.DataFrame()
for ticker in result.columns.levels[1]:
    index = pd.MultiIndex.from_arrays([
            [ticker] * len(result),
            result.index.values
            ], names=['ticker', 'date'])
    ticker_df = pd.DataFrame(index=index)
    for col in result.columns.levels[0]:
        ticker_df[col] = result[col][ticker].values
    data = pd.concat([data, ticker_df])

data['close'].unstack().info()

