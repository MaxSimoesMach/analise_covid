import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
print(df.head())

df_brasil = df[df["location"] == "Brazil"][["date", "total_cases", "new_cases", "total_deaths", "new_deaths"]]
df_brasil["date"] = pd.to_datetime(df_brasil["date"])
df_brasil = df_brasil.dropna()
df_brasil.head()
df_brasil["fatality_rate"] = (df_brasil["total_deaths"] / df_brasil["total_cases"]) * 100

plt.figure(figsize=(12, 6))
plt.plot(df_brasil["date"], df_brasil["total_cases"], label="Casos Totais", color="blue")
plt.plot(df_brasil["date"], df_brasil["total_deaths"], label="Mortes Totais", color="red")
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.title("Evolução da COVID-19 no Brasil")
plt.legend()
plt.xticks(rotation=45)
plt.show()

df_brasil.to_excel("covid_brasil.xlsx", index=False)

print("Arquivo covid_brasil.xlsx salvo com sucesso!")

