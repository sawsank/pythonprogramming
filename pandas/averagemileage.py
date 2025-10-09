import pandas as pd

# 1. Provide your CSV file path
df = pd.read_csv("pandas/Automobile_data.csv")

# 2. Group by 'company' and calculate mean of 'average-mileage'
mileageDf = df.groupby('company', as_index=False)['average-mileage'].mean()

print(mileageDf)