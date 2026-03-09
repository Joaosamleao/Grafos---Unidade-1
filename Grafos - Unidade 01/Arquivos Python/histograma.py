import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300
plt.style.use('seaborn-v0_8-whitegrid')

try:
    df_in = pd.read_csv('distribuicao_indegree.csv').sort_values('Grau')
    df_out = pd.read_csv('distribuicao_outdegree.csv').sort_values('Grau')

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(df_in['Grau'], df_in['Frequencia'],
           color='#3498db', alpha=0.5, label='In-degree (Entrada)',
           edgecolor='#2980b9', linewidth=0.5)

    ax.bar(df_out['Grau'], df_out['Frequencia'],
           color='#e74c3c', alpha=0.5, label='Out-degree (Saída)',
           edgecolor='#c0392b', linewidth=0.5)

    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_title('Distribuição de Graus (Histograma Log-Log)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel(r'Grau ($k$)', fontsize=12)
    ax.set_ylabel(r'Frequência ($N_k$)', fontsize=12)

    ax.legend(frameon=True, fontsize=10)

    plt.tight_layout()

    plt.savefig('histograma_sobreposto_in_out.png', bbox_inches='tight')
    plt.show()

    print("Histograma de barras sobrepostas gerado com sucesso!")

except Exception as e:
    print(f"Erro ao gerar o histograma: {e}")