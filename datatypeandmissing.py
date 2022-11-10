import pandas as pd

reviews = pd.read_csv("../simple.csv")

# print(reviews.Salary.dtype)
# print(reviews.dtypes)

# print(reviews.Salary.astype('float64'))

print(reviews)
print(reviews.Team.fillna("Unknown"))
print(reviews[pd.isnull(reviews.Salary)])