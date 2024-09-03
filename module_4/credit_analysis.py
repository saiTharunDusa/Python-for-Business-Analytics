import pandas as pd

def main():
    # read the data from credit.csv file
    credit_data = pd.read_csv('credit.csv')
    # print the head.
    print(credit_data.head())
    print('hello world')
    print()


    #print the descriptive statistics
    print(credit_data.describe())
    print()

main()
