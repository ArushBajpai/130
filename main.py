import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

print(df.shape)

del df["Luminosity"]

print(df.shape)

df.to_csv('main.csv')  