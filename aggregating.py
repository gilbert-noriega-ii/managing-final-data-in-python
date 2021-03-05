# Inspect nyse using .info().
# With broadcasting and .div(), create a new column market_cap_m that contains the market capitalization in million USD.
# Omit the column 'Market Capitalization' with .drop().
# Apply the .groupby() method to nyse, using 'Sector' as the column to group your data by.
# Calculate the median of the market_cap_m column as median_mcap_by_sector.
# Plot the result as a horizontal bar chart with the title 'NYSE - Median Market Capitalization'. Use plt.xlabel() with 'USD mn' to add a label.
# Show the result. 



nyse.info()

nyse['market_cap_m'] = nyse['Market Capitalization'].div(1e6)

nyse = nyse.drop('Market Capitalization', axis=1)

mcap_by_sector = nyse.groupby('Sector')

median_mcap_by_sector = mcap_by_sector.market_cap_m.median()

median_mcap_by_sector.plot(kind = 'bar', title='NYSE - Median Market Capitalization')

plt.xlabel('USD mn')

plt.show()


# Inspect and display listings using .info() and .head().
# Using broadcasting, create a new column market_cap_m for listings that contains the market cap in millions of USD.
# Select all companies with an 'IPO Year' after 1985.
# Drop all missing values in the 'IPO Year' column, and convert the remaining values to dtype integer.
# Group listings by 'IPO Year', select the market_cap_m column and calculate the median, sort with .sort_index(), and assign the result to ipo_by_year.
# Plot and show the results as a bar chart.


listings.info()

print(listings.head())

listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)

listings = listings[listings['IPO Year'] > 1985]

listings['IPO Year'] = listings['IPO Year'].dropna().astype(int)

ipo_by_year = listings.groupby('IPO Year').market_cap_m.median().sort_index()

ipo_by_year.plot(kind='bar')

plt.show()


# Inspect the nasdaq data using .info().
# Create a new column market_cap_m that contains the market cap in millions of USD. On the next line, drop the column 'Market Capitalization'.
# Group your nasdaq data by 'Sector' and assign to nasdaq_by_sector.
# Call the method .describe() on nasdaq_by_sector, assign to summary, and print the result.
# This works, but result is in long format and uses a pd.MultiIndex() that you saw earlier. Convert summary to wide format by calling .unstack().

nasdaq.info()

nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)

nasdaq.drop('Market Capitalization', axis=1, inplace=True)

nasdaq_by_sector = nasdaq.groupby('Sector')

summary = nasdaq_by_sector.describe()

print(summary)

summary = summary.unstack()

print(summary)


# Group your data by both 'Sector' and 'Exchange', assigning the result to by_sector_exchange.
# Calculate the median market capitalization for by_sector_exchange and assign to mcap_by_sector_exchange.
# Display the first 5 rows of the result with .head().
# Call .unstack() on mcap_by_sector_exchange to move the Exchange labels to the columns, and assign to mcap_unstacked.
# Plot the result as a bar chart with the title 'Median Market Capitalization by Exchange' and xlabel set to 'USD mn',
# Show the result.


by_sector_exchange = listings.groupby(['Sector', 'Exchange'])

mcap_by_sector_exchange = by_sector_exchange.market_cap_m.median()

print(mcap_by_sector_exchange.head())

mcap_unstacked = mcap_by_sector_exchange.unstack()

mcap_unstacked.plot(kind = 'bar', title='Median Market Capitalization by Exchange')

plt.xlabel('USD mn')

plt.show()


# With broadcasting and .div(), create a new column 'market_cap_m' that contains the market capitalization data in millions of USD.
# Group your data by both 'Sector' and 'Exchange', assigning the result to by_sector_exchange.
# Assign the market_cap_m column of by_sector_exchange to a variable bse_mcm.
# Use .agg() and a dictionary argument to calculate the mean, median, and standard deviation for market_cap_m storing the results in 'Average', 'Median', and 'Standard Deviation', respectively, and assign to summary.
# Print the result to your console.


listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)

by_sector_exchange = listings.groupby(['Sector', 'Exchange'])

bse_mcm = by_sector_exchange['market_cap_m']

summary = bse_mcm.agg({'Average': 'mean', 'Median': 'median', 'Standard Deviation': 'std'})

print(summary)


# Filter listings to only include IPO years after the year 2000.
# Convert the data in the column 'IPO Year' to integers.
# Plot a sns.countplot() of listings using 'IPO Year' as the x variable and 'Exchange' for hue.
# Rotate the xticks() by 45 degrees and show the result.


listings = listings[listings["IPO Year"] > 2000]

listings['IPO Year'] = listings["IPO Year"].astype(int)

sns.countplot(x = 'IPO Year', hue = 'Exchange', data = listings)

plt.xticks(rotation=45)

plt.show()


# Inspect income_trend using .info().
# Create a sns.barplot() using the column 'Year' for x and 'Income per Capita' for y, and show the result after rotating the xticks by 45 degrees.
# Use plt.close() after the initial plt.show() to be able to show a second plot.
# Create a second sns.barplot() with the same x and y settings, using estimator=np.median to calculate the median, and show the result.


income_trend.info()

sns.barplot(x='Year', y='Income per Capita', data=income_trend)

plt.xticks(rotation=45)

plt.show()

plt.close()

sns.barplot(x="Year", y='Income per Capita', data=income_trend, estimator=np.median)

plt.xticks(rotation=45)

plt.show()



# Import seaborn as sns.
# Filter listings to have companies with IPOs after 2000 from all exchanges except the 'amex'.
# Convert the data in column 'IPO Year' to integers.
# Create the column market_cap_m to express market cap in USD million.
# Filter market_cap_m to exclude values above the 95th percentile.
# Create a pointplot of listings using the column 'IPO Year' for x, 'market_cap_m' for y, and 'Exchange' for hue. Show the result after rotating the xticks by 45 degrees.


import seaborn as sns

# Exclude IPOs before 2000 and from the 'amex'
listings = listings[(listings['IPO Year'] > 2000) & (listings.Exchange != 'amex')]

listings['IPO Year'] = listings['IPO Year'].astype(int)

listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)

listings = listings[listings.market_cap_m < listings.market_cap_m.quantile(.95)]

sns.pointplot(x='IPO Year', y='market_cap_m', hue='Exchange', data=listings)

plt.xticks(rotation=45)

plt.show()


# Inspect inflation using .info().
# Group inflation by 'Country' and assign to inflation_by_country.
# In a for loop, iterate over country, data pairs returned by inflation_by_country. In each iteration, use .plot() on data with title set to country to show the historical time series.


inflation.info()

inflation_by_country = inflation.groupby('Country')

for country, data in inflation_by_country:
    data.plot(title = country)
    plt.show()


# Create and show a boxplot of the inflation data with 'Country' for x and 'Inflation' for y.
# Create and show sns.swarmplot() with the same arguments.


sns.boxplot(x='Country', y='Inflation', data= inflation)

plt.show()

plt.close()

sns.swarmplot(x="Country", y="Inflation", data=inflation)

plt.show()