

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

tips_df = pd.read_csv('/content/tips.csv')
print(tips_df.head())
print(tips_df.info())
print('The descriptive statistics of tip_df:')
print(tips_df.describe())

#create a bar plot to understand the relationship between tip and total_bill.
plt.bar(tips_df['total_bill'],tips_df['tip'],width = 0.9)
plt.title("relationship between the tips and total_bill ")
plt.xlabel('total_bill')
plt.ylabel('tip')
plt.show()

#create a bar plot to understand the relationship between tip and sex.
plt.bar(tips_df['sex'],tips_df['tip'])
plt.title("relationship between the tips and sex ")
plt.xlabel('sex')
plt.ylabel('tip')
plt.show()

#create a bar plot to understand the relationship between tip and smoker.
plt.bar(tips_df['smoker'],tips_df['tip'])
plt.title("relationship between the tips and smoker ")
plt.xlabel('smoker')
plt.ylabel('tip')
plt.show()

#create a bar plot to understand the relationship between tip and day.
plt.bar(tips_df['day'],tips_df['tip'])
plt.title("relationship between the tips and day ")
plt.xlabel('day')
plt.ylabel('tip')
plt.show()

#create a bar plot to understand the relationship between tip and time.
plt.bar(tips_df['time'],tips_df['tip'])
plt.title("relationship between the tips and time ")
plt.xlabel('time')
plt.ylabel('tip')
plt.show()

#create a bar plot to understand the relationship between tip and size.
plt.bar(tips_df['size'],tips_df['tip'])
plt.title("relationship between the tips and size ")
plt.xlabel('size')
plt.ylabel('tip')
plt.show()

"""1. The higher the total bill, the higher the tip tends to be. However, this is not always the case, as there can be fluctuations in the tip amount compared to the total bill.
2. The male group has given more tips than the female group.
3. Smokers tend to give higher tips than non-smokers.
4. There were more tips  on Saturday.
5. There were a higher number of tips during dinner time compared to lunch.
6. Party size represents the number of people in a dining party. Parties of three have generated the most tips.
"""

# Fitting an ordinary least squares (OLS) regression model using statsmodels
model = smf.ols(formula="tip ~ total_bill + sex + smoker + day + time + size", data=tips_df).fit()

# Printing a detailed summary of the regression results
print(model.summary())

# Extracting and assigning coefficients from the fitted model
intercept = model.params[0]  # intercept - the first parameter
sex_coeff = model.params[1]
smoker_coeff = model.params[2]
satday_coeff = model.params[3]
sunday_coeff = model.params[4]
thursday_coeff = model.params[5]
time_coeff = model.params[6]
total_bill_coeff = model.params[7]
size_coeff = model.params[8]

# Printing individual coefficients for interpretation
print("Intercept ", intercept)
print("sex_coefficient", sex_coeff)
print("smoker_coefficient", smoker_coeff)
print("satday_coefficient", satday_coeff)
print("sunday_coefficient", sunday_coeff)
print("thursday_coefficient", thursday_coeff)
print("time_coefficient", time_coeff)
print("total_bill_coefficient", total_bill_coeff)
print("size_coefficient", size_coeff)

# Printing all the estimated parameters of the model
print()
print(model.params)

"""1. The F-statistic p-value of 1.20e-28 indicates a statistically significant model. This means that at least one of the independent variables in the model has a significant relationship with the dependent variable (tip amount).
2. The positive coefficients of total_bill and size indicate a positive relationship with the tip amount. In other words, as the total bill and party size increase, the tip amount tends to increase as well.
The R-squared value of 0.470 represents the proportion of the variance in the tip amount that can be explained by the model. In simpler terms, it tells us how well the model fits the data.
3. The negative coefficients for sex, smoker, and days (Saturday, Sunday, Thursday) indicate a negative relationship with the tip amount. This suggests that, on average, females tip less than males, smokers tip less than non-smokers, and tips are lower on Saturdays, Sundays, and Thursdays compared to other days.
4. The p-values for individual columns can vary. A low p-value for a specific variable indicates a statistically significant relationship between that variable and the tip amount.
"""

# Forcast the tips given the values of total_bill,sex,size,day,time
# Print the last 10 rows of economic_growth to determine a test value

print(tips_df.tail(10))

# Calculate the regression model for this mode (general : y = m.x + b) y = dependent variable m = slope/coefficient x is the test value
# b is the intercept

total_bill_x = 30.99
sex_x = 'Female'
smoker_x = 'Yes'
day_x = 'Sat'
time_x = 'Dinner'
size_x = 4

predicted_tip = (total_bill_x * total_bill_coeff +
                 (1 if sex_x == 'Female' else 0) * sex_coeff +
                 (1 if smoker_x == 'Yes' else 0) * smoker_coeff +
                 (1 if day_x == 'Sat' else 0) * satday_coeff +
                 (1 if time_x == 'Dinner' else 0) * time_coeff +
                 size_x * size_coeff +
                 intercept)

print(f'The predicted tip is ${predicted_tip:,.2f}')

"""1. The model predicts an average tip of 4.26 dollars.
2. Several factors influence the tip amount, including gender, smoking status, party size, bill total, day of the week, and time of day.
3. Considering all relevant factors is crucial to understand how much a server might receive in tips.
"""