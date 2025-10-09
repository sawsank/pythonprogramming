import pandas as pd

df = pd.read_csv("pandas/Automobile_data.csv")

# Group by company
car_Manufacturers = df.groupby('company')

# Use a list to select multiple columns
priceDf = car_Manufacturers[['company', 'price']].max()

print(priceDf)
