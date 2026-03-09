import pandas as pd
import matplotlib.pyplot as plt
import powerlaw
import numpy as np

plt.rcParams['figure.dpi'] = 300
plt.style.use('seaborn-v0_8-whitegrid')

df = pd.read_csv('distribuicao_indegree.csv')
df = df.sort_values('Grau').reset_index(drop=True)

dados_brutos = np.repeat(df['Grau'].values, df['Frequencia'].values)

fit = powerlaw.Fit(dados_brutos, discrete=True, verbose=False)

R, p = fit.distribution_compare('power_law', 'lognormal')

print(f"Comparação (R): {R}")
print(f"P-value: {p}")

mu = fit.lognormal.mu
sigma = fit.lognormal.sigma
xmin = fit.lognormal.xmin
ks = fit.lognormal.D

print("Lognormal MU =", mu)
print("Lognormal SIGMA =", sigma)
print("X_MIN =", xmin)
print("KS =", ks)

x_fit = np.arange(int(xmin), int(df['Grau'].max()) + 1)

tail_fraction = np.sum(dados_brutos >= xmin) / len(dados_brutos)

y_fit = fit.lognormal.pdf(x_fit) * tail_fraction

fig, ax = plt.subplots(figsize=(10,6))

v_total = len(dados_brutos)
df['Probabilidade'] = df['Frequencia'] / v_total

ax.scatter(
    df['Grau'],
    df['Probabilidade'],
    color='#2c3e50',
    alpha=0.6,
    s=20,
    label='Dados Observados'
)

ax.plot(
    x_fit,
    y_fit,
    color='green',
    linestyle='--',
    linewidth=2,
    label=f'Ajuste Lognormal (μ: {mu:.2f}, σ: {sigma:.2f})'
)

ax.axvline(
    x=xmin,
    color='gray',
    linestyle=':',
    alpha=0.5,
    label=f'x_min = {int(xmin)}'
)

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_title(
    'Distribuição de In-Degree e Ajuste Lognormal',
    fontsize=16,
    fontweight='bold',
    pad=20
)

ax.set_xlabel('Grau do Vértice (k) - Log', fontsize=12)
ax.set_ylabel('Probabilidade P(k) - Log', fontsize=12)

ax.legend(loc='lower left')

plt.tight_layout()
plt.savefig('grafico_final_lognormal.png', bbox_inches='tight')
plt.show()