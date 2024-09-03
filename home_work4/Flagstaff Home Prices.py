import pandas as pd

def main():
    # reading the from the .csv file
    data = pd.read_csv("flagstaff_real_estate_data.csv")
    # printing the header.
    print(data.head())
    print()


    # descriptive statistics
    print('The descriptive analysis of the Flagstaff Home Prices: ')
    print(data.describe())
    print()

    # median
    print('The median value of the home prices: ')
    print(data['PRICE'].median())
    print()

    # median of home price for each year
    print('The median of home price for each year:')
    print(data.groupby(['YEAR']).median(['PRICE']))
    print()
    
    # subset of the years 2010 - 2019
    print('Take the subset off that include the year 2010-2019: ')
    year_data = data.loc[(data['YEAR'] <= 2019) & (data['YEAR'] >= 2010)]
    print(year_data)
    print()

    # Generating the descriptive statistics for year_data.
    print('The descriptive analysis of the Flagstaff Home Prices between 2010 - 2019:')
    print(year_data.describe())
    print()

    # Median of Home price for each year of year_data
    print('The median of home price for each year:')
    print(year_data.groupby(['YEAR']).median(['PRICE']))
    print()

    # Median of Home price for each month of year_data
    print('The median of home price for each month:')
    print(year_data.groupby(['MONTH']).median(['PRICE']))
    print()
    


main()
