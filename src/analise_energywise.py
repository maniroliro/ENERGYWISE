import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("../data/consumo_energia.csv")

# Estatísticas básicas
media = df["consumo_kwh"].mean()
pico = df["consumo_kwh"].max()
horario_pico = df.loc[df["consumo_kwh"].idxmax(), "hora"]
menor = df["consumo_kwh"].min()

# Plot 1: Consumo diário
plt.figure(figsize=(10, 4))
plt.plot(df["hora"], df["consumo_kwh"])
plt.xlabel("Hora do dia")
plt.ylabel("Consumo (kWh)")
plt.title("Consumo energético ao longo do dia")
plt.grid(True)
plt.savefig("../outputs/grafico_consumo.png")
plt.close()

# Identificar desperdícios
# Regra: consumo acima de 80 kWh é considerado crítico
df["critico"] = df["consumo_kwh"] > 80

# Plot 2: Destaque dos picos
plt.figure(figsize=(10, 4))
plt.plot(df["hora"], df["consumo_kwh"])
picos = df[df["critico"]]
plt.scatter(picos["hora"], picos["consumo_kwh"])
plt.xlabel("Hora do dia")
plt.ylabel("Consumo (kWh)")
plt.title("Picos de consumo identificados")
plt.grid(True)
plt.savefig("../outputs/grafico_picos.png")
plt.close()

# Estimativa de economia
energia_desperdicada = df[df["critico"]]["consumo_kwh"].sum() - (80 * len(df[df["critico"]]))
economia_mensal_kwh = energia_desperdicada * 30
economia_mensal_reais = economia_mensal_kwh * 0.95  # tarifa média

# Gerar relatório
with open("../outputs/relatorio_resultados.md", "w") as f:
    f.write("# Resultados da Análise EnergyWise\n")
    f.write(f"\n**Consumo médio diário:** {media:.2f} kWh")
    f.write(f"\n**Consumo máximo:** {pico} kWh às {horario_pico}h")
    f.write(f"\n**Menor consumo:** {menor} kWh")
    f.write("\n\n## Identificação de desperdícios")
    f.write(f"\nHoras críticas: {len(df[df['critico']])}")
    f.write(f"\nEnergia desperdiçada/dia: {energia_desperdicada:.2f} kWh")
    f.write(f"\nEconomia mensal estimada: R$ {economia_mensal_reais:.2f}")
