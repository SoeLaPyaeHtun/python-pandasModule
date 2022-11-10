import pandas as pd


reviews = pd.read_csv("../simple.csv")

# print(reviews.groupby('Salary').Salary.count())
# print(reviews.groupby('Salary').Salary.min())
# print(reviews.groupby('Salary').Salary.max())

# print(reviews.groupby(['Salary','First Name']).Salary.min())
# print(reviews.loc[(reviews['First Name'] == 'Katherine')])

print(reviews.groupby(['First Name']).Salary.agg([len, min, max]))