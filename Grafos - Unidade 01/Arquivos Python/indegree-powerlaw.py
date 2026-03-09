import pandas as pd
import matplotlib.pyplot as plt
import powerlaw
import numpy as np

plt.rcParams['figure.dpi'] = 300
plt.style.use('seaborn-v0_8-whitegrid')

try:
    df = pd.read_csv('distribuicao_indegree.csv')
    df = df.sort_values('Grau')

    dados_brutos = np.repeat(df['Grau'].values, df['Frequencia'].values)
    fit = powerlaw.Fit(dados_brutos, discrete=True)

    R, p = fit.distribution_compare('power_law', 'lognormal')
    print(f"(R): {R}")
    print(f"P-value: {p}")

    alpha = fit.power_law.alpha
    xmin = fit.power_law.xmin

    v_total = 262111
    df['Probabilidade'] = df['Frequencia'] / v_total

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(df['Grau'], df['Probabilidade'], color='#2c3e50', alpha=0.6, s=20, label='Dados Observados')

    x_fit = np.linspace(xmin, df['Grau'].max(), 100)
    y_fit = (x_fit**-alpha) * (df[df['Grau'] >= xmin]['Probabilidade'].max() * (xmin**alpha))

    ax.plot(x_fit, y_fit, color='red', linestyle='--', linewidth=2, label=f'Ajuste Power Law (Alpha: {alpha:.2f})')

    ax.axvline(
        x=xmin,
        color='gray',
        linestyle=':',
        alpha=0.5,
        label=f'x_min = {int(xmin)}'
    )
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title('Distribuição de In-Degree e Power Law', fontsize=16, fontweight='bold')
    ax.set_xlabel('Grau do Vértice (k) - Log')
    ax.set_ylabel('Probabilidade P(k) - Log')

    ax.legend(loc='lower left')
    plt.tight_layout()
    plt.savefig('grafico_apresentacao_power_law.png', bbox_inches='tight')
    plt.show()

except Exception as e:
    print(f"Erro ao gerar gráfico: {e}")