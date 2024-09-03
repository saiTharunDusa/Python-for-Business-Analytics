# Created by Dusa Sai Tharun, sd2672 (6329289)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/bike_share_data.csv')
print(df.head())
print()
print(df.describe())

# Create a histogram to better understand the distribution of no of registered bike users.
plt.hist(df['registered'], bins = 10)
plt.title('Distribution of registered bike users')
plt.xlabel('No of registered bike users')
plt.ylabel('Records')
plt.show()

"""From the above histogram, we can conclude that the no of registered bike users are decreasing steadily."""

# Create a bar plot that shows the median number of registered riders (grouped by month) for each month for the year 2011.
# Create another bar plot that shows the median number of registered riders (grouped by month) for each month for the year 2012.

df['dteday'] = pd.to_datetime(df['dteday'])
df['year'] = df['dteday'].dt.year
df['month'] = df['dteday'].dt.month
#print(df.head())

df_year_2011 = df[df['year'] == 2011]
df_year_2012 = df[df['year'] == 2012]

median_2011 = df_year_2011.groupby('month')['registered'].median()
median_2012 = df_year_2012.groupby('month')['registered'].median()

plt.bar(median_2011.index, median_2011.values)
plt.title('Median of registered users for each month in the year 2011.')
plt.xlabel('Month')
plt.ylabel('Median of no of registered users.')
plt.show()

plt.bar(median_2012.index, median_2012.values)
plt.title('Median of registered users for each month in the year 2012.')
plt.xlabel('Month')
plt.ylabel('Median of no of registered users.')
plt.show()

"""1.In the year 2011, in the 6th month the median is high which is around 130. That implies there are more no of registered bike users are in the 6th month. Whereaas in the year 2012, 9th month has more no of registered bike users.

2.In both years, the no of registered bike users are less in the first month.

3.In the year 2012 has more no of registered bike users compared to the year 2011 since the highest median of 2012 is higher than the highest median of 2011.

"""

# Create a bar plot showing the median number of registered riders (grouped by hour) for each hour for the month of July (include both years).
df_year_2011_2012 = df[(df['year'] == 2011) | (df['year'] == 2012)]
df_month_july = df_year_2011_2012[df_year_2011_2012['month'] == 7]
median_july = df_month_july.groupby('hr')['registered'].median()
plt.bar(median_july.index, median_july.values)
plt.title('Median no of registered riders grouped by each hour in the month of july of the years 2011 and 2012.')
plt.xlabel('Hours')
plt.ylabel('Median of no of registered bike users.')
plt.show()

"""1. In the month of july of both year 2011 and 2012, the 16th &17th hour has more no of registered bike users.
2.At the 3rd and 4th hour there are least no of registered bike users.
"""

# Create a bar plot showing the median number of registered riders (grouped by day) for each day (include both years)
# we have date frame which includes the both years 2011 and 2012.
df_year_2011_2012['day'] = df_year_2011_2012['dteday'].dt.day
median_day = df_year_2011_2012.groupby('day')['registered'].median()

plt.bar(median_day.index, median_day.values)
plt.xlabel('Days')
plt.ylabel('Median of registered bike users.')
plt.title('Median no of registered rideres grouped by day for each day in the year 2011 and 2012')
plt.show()

"""1.On the 17th day, no of registered bike users are more. And it was on day 21 where the no of registered bike users are least.
2.Almost every day has almost similar no of registered bike users.
"""

# Create a scatter plot to show the relationship between windspeed and the number of registered riders only for the month of March in the year 2011.
# We already have data frame for the year 2011.
df_march_2011 = df_year_2011[df_year_2011['month'] == 3]
plt.scatter(df_march_2011['windspeed'], df_march_2011['registered'])
plt.title('Relationship between windspeed and no of registered riders for the month of march in the year 2011.')
plt.xlabel('Windspeed')
plt.ylabel('Registered Bike Users')
plt.show()

"""1. As windspeed increases, the no of registered bike users decreases.
2. The more no of registered bike users are at the windspeed 0.3

`

1. To address the potential decline in ridership on windy days, the bike-sharing company might consider implementing a marketing strategy that is tailored to weather conditions.

2. With an increasing number of registered users, the company should intensify marketing efforts targeting this demographic. Additionally, promotional activities could be extended to loyal customers.

3. I am curious to find out whether there are any consistent customers among the user base.
"""