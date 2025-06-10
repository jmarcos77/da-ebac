import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="dia", y="venda", marker='o', label="Preço médio")
plt.title("Preço médio da gasolina em São Paulo - Julho 2021 (dias 1 a 10)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)
plt.legend()
plt.savefig("gasolina.png")
