#Load the 'per_capita_income.csv' file into income. No additional arguments other than the file name are needed. (Note that this is a csv file.)
#Inspect the column names and data types with .info().
#Using .sort_values(), sort (in descending order) the income DataFrame by the column which contains the income information.
#Display the first five rows of income using .head() and the last five rows using .tail().


income = pd.read_csv('per_capita_income.csv')

income.info()

income = income.sort_values('Income per Capita', ascending = False)

print(income.head())
print(income.tail())


#Use the appropriate function to calculate the global mean of 'Income per Capita'.
#Use the appropriate function to calculate the global median of 'Income per Capita'.
#Using broadcasting, create a new column 'Income per Capita (,000)' equal to income['Income per Capita'] // 1000. Then use the appropriate function to calculate the mode for this new column.


print(income['Income per Capita'].mean())

print(income['Income per Capita'].median())

income['Income per Capita (,000)'] = income['Income per Capita'] // 1000

income['Income per Capita (,000)'].mode()


#Using the appropriate functions, calculate the mean of income per capita as mean and the standard deviation as std.
#Without using .quantile(), calculate and print the upper and lower bounds of an interval of one standard deviation around the mean in a list bounds:
#subtract std from mean as the first element
#add std to mean as the second element
#Using .quantile() and a list of two appropriate decimal values, calculate and print the first and the third quartile of 'Income per Capita' as quantiles. Do the values match?
#Calculate and print the IQR, iqr, using the simple subtraction expression you learned in the video.


mean = income['Income per Capita'].mean()

std = income['Income per Capita'].std()

bounds = [mean - std, mean + std]
print(bounds)

quantiles = income['Income per Capita'].quantile([.25, .75])
print(quantiles)

iqr = quantiles[.75] - quantiles[.25]
print(iqr)


#Generate the percentages from 10% to 90% with increments of 10% using np.arange(), assign the result to quantiles, and print it.
#Using quantiles and .quantile(), calculate the deciles for the income per capita as deciles, and print the result.
#Plot and show the result as a bar chart with plt.tight_layout(). Title it 'Global Income per Capita - Deciles'


quantiles = np.arange(start = .1, stop = .91, step = .1)

print(quantiles)

deciles = income['Income per Capita'].quantile(quantiles)

print(deciles)

deciles.plot(kind = 'bar', title='Global Income per Capita - Deciles')

plt.tight_layout()

plt.show()


#Import seaborn as sns and matplotlib.pyplot as plt.
#Print the summary statistics provided by .describe().
#Plot and show a basic histogram of the 'Income per Capita' column with .distplot().
#Create and show a rugplot of the same data by setting the additional arguments bins equal to 50, kde to False, and rug to True.


import seaborn as sns
import matplotlib.pyplot as plt

print(income.describe())

sns.distplot(income['Income per Capita'])

plt.show()

sns.distplot(income['Income per Capita'], bins = 50, kde = False, rug = True)

plt.show()


#Load the file 'income_growth.csv' into the variable growth. Parse the 'DATE' column into dtype datetime64 and set it as the index.
#Inspect the summary statistics for these three growth rates using the appropriate function.
#Iterate over the growth.columns attribute in a for loop to access their labels. Most of the code has been outlined for you.
#In each iteration of distplot(), pass in the iteration variable column to select the respective column, set the keyword hist to False, and set label to column.
#Show the result.


growth = pd.read_csv('income_growth.csv', parse_dates=['DATE']).set_index('DATE')

growth.describe()

for column in growth.columns:
    sns.distplot(growth[column], hist=False, label=column)
    
plt.show()


#Assign the column 'Income per Capita' to inc_per_capita.
#Filter to keep only the rows in inc_per_capita that are lower than the 95th percentile. Reassign to the same variable.
#Plot a default histogram for the filtered version of inc_per_capita and assign it to ax.
#Use ax.axvline() with color='b' to highlight the mean of inc_per_capita in blue,
#Use ax.axvline() with color='g' to highlight the median in green. Show the result!


inc_per_capita = income['Income per Capita']

inc_per_capita = inc_per_capita[inc_per_capita < inc_per_capita.quantile(.95)]

ax = sns.distplot(inc_per_capita)

ax.axvline(inc_per_capita.mean(), color='b')

ax.axvline(inc_per_capita.median(), color='g')

plt.show()


#Create a list exchanges containing the exact strings of the names 'amex', 'nasdaq', and 'nyse'.
#Use a for loop to iterate over exchanges with an iterator variable exchange that contains the name of each exchange. In each iteration:
#Apply .value_counts() to 'Sector' and assign the result to sectors.
#Sort sectors in descending order and plot them in a bar plot.
#Show the result.


exchanges = ['amex', 'nasdaq', 'nyse']

for exchange in exchanges:
    sectors = listings[exchange].Sector.value_counts()
    sectors.sort_values(ascending = False).plot(kind = 'bar')
    plt.show()


#Use a for loop with iterator variable exchange that contains the name of each exchange.
#In each iteration, append the DataFrame corresponding to the key exchange in listings to all_listings.
#After the loop completes, use pd.concat() to combine the three DataFrames in all_listings and assign the result to listing_data.
#Filter listing_data for 'Technology' companies and assign the result to tech_companies.
#Assign the 'IPO Year' column from tech_companies to ipo years.
#For this data, use .dropna() to remove missing values and .astype() to convert to int.
#Apply .value_counts() to ipo_years, sort the years in ascending order, and create a bar plot titled 'Tech IPOs by Year'.
#Rotate xticks by 45 degrees and show the result.


exchanges = ['amex', 'nasdaq', 'nyse']
all_listings = []

for exchange in exchanges:
    all_listings.append(listings[exchange])
    
listing_data = pd.concat(all_listings)

tech_companies = listing_data[listing_data.Sector == 'Technology']

ipo_years = tech_companies['IPO Year']

ipo_years = ipo_years.dropna().astype(int)

ipo_years.value_counts(ascending = True).plot(kind = 'bar', title = 'Tech IPOs by Year')

plt.xticks(rotation = 45)

plt.show()