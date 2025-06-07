import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("gasolina.csv")

# Criar gráfico
sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="dia", y="venda", marker="o")
plt.title("Preço da Gasolina em SP - Julho 2021")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.savefig("gasolina.png")
plt.show()
