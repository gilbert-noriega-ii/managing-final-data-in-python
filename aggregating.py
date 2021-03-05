'''
Inspect nyse using .info().
With broadcasting and .div(), create a new column market_cap_m that contains the market capitalization in million USD.
Omit the column 'Market Capitalization' with .drop().
Apply the .groupby() method to nyse, using 'Sector' as the column to group your data by.
Calculate the median of the market_cap_m column as median_mcap_by_sector.
Plot the result as a horizontal bar chart with the title 'NYSE - Median Market Capitalization'. Use plt.xlabel() with 'USD mn' to add a label.
Show the result. 
'''

