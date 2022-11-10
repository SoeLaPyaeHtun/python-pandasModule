import pandas as pd

review = pd.read_csv("../simple.csv")


# print(review['First Name'])
# print(review['First Name'][55])


#print(review['Start Date'])

# print(review.iloc[-5:])
# print(review.iloc[-5,:])
# print(review.iloc[5:])
# print(review.iloc[5,:])


# print(review.loc[0,'First Name'])
# print(review.loc[:,['First Name','Gender','Salary']])

# print(review['First Name'] == 'Douglas')


# print(review.loc[(review['First Name'] == 'Douglas') & (review['Salary'] > 100000) ])
# print(review.loc[(review['First Name'] == 'Douglas') | (review['Salary'] > 100000) ])

print(review.loc[review['First Name'].isin(['Douglas','Maria'])])