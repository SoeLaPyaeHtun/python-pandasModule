import pandas as pd

# print(pd.DataFrame({"Yes":[1,2], "No":[3,4]}))


# print(pd.DataFrame({
#     "Bob":['I like it','it was awful'],
#     "Sue":['pretty good','bland']
# }))

# print(pd.DataFrame({
#     "bob":['I like it','it was awful'],
#     "sue":['pretty good','bland']
# },index=['product A','product B']
# ))

print(pd.Series([1,2,3,4,7]))

print(pd.Series([12,34,56], index=['sale one',"sale two","sale three"], name="product A"))

print(pd.Series(["4 cups","1cups","2 large","1 can"],index=['Flour','Mile','Eggs','Spam'],name="Dinner"))