import pandas as pd
df = pd.read_csv("pandas/Automobile_data.csv")
print(df['company'].value_counts())