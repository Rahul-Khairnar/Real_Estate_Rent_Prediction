import pandas as pd

df = pd.read_csv("Properties_cleaned.csv")
df_dummy = pd.get_dummies(df)

df_final = df_dummy.drop("locality_Others",axis = 1)

df_without_dependent = df_final.drop("price",axis = 1)

df_dependent = df_final["price"]

