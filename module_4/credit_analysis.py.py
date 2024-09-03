import pandas as pd

credit_data = pd.read_csv('/content/credit.csv')
print(credit_data.head())
print()

#print the descriptive statistics
print('Printing the descriptive statistics:\n')
print(credit_data.describe())
print()

#group the data by PAY_1 and show the mean for BILL_AMT1
print('Printing the mean of BILL_AMT1 which is grouped by PAY_1\n')
grouped_data = credit_data.groupby(['PAY_1']).mean(['BILL_AMT1'])
print(grouped_data)
print()

#group the data by PAY_2 and show the mean for AGE.
print('Printing the mean for AGE which is groupedby PAY_2\n')
grouped_data1 = credit_data.groupby(['PAY_2']).mean(['AGE'])
print(grouped_data1)
print()
print('No of unique ages in PAY_2 : ')
print(grouped_data1['AGE'].nunique())

# Two subsets of data.
female_data = credit_data.loc[credit_data['SEX'] == 2]
male_data = credit_data.loc[credit_data['SEX'] == 1]
# apply the .nunique method to each subset.
male_unique_data1 = male_data['PAY_1'].nunique()
male_unique_data2 = male_data['PAY_6'].nunique()
female_unique_data1 = female_data['PAY_1'].nunique()
female_unique_data2 = female_data['PAY_6'].nunique()

print(f'Male unique data for PAY_1 - {male_unique_data1}')
print(f'Male unique data for PAY_6 - {male_unique_data2}')
print(f'Female unique data for PAY_1 - {female_unique_data1}')
print(f'Female unique data for PAY_6  - {female_unique_data2}')