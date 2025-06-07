import pandas as pd

df = pd.read_csv("DataAnalyst.csv")
print(df.head())

df = df.dropna(subset=["Заробітна плата"])
df["Заробітна плата"] = pd.to_numeric(df["Заробітна плата"], errors="coerce")

print("Середня зарплата:", df["Заробітна плата"].mean())
print("Максимальна зарплата:", df["Заробітна плата"].max())
print("Мінмальна зарплата:", df["Заробітна плата"].min())


