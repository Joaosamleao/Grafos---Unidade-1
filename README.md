---

# Análise Estatística da Rede Amazon 0302

Este projeto realiza uma análise estrutural e estatística do dataset **Amazon 0302 (SNAP)**, uma rede direcionada de copropriedade de produtos. O objetivo é processar os dados da rede e determinar se a distribuição de graus segue uma Lei de Potência (*Power Law*) ou uma distribuição **Lognormal**.

## Resumo dos Dados
- **Vértices:** 262.111
- **Arestas:** 1.234.877
- **Grau de Saída Médio:** 4,71
- **Densidade:** $1,79 \times 10^{-5}$

## Tecnologias e Bibliotecas
- **Java:** Biblioteca `Algs4` (Princeton) para manipulação de grafos.
- **Python:** 
  - `pandas` e `numpy` para manipulação de dados.
  - `powerlaw` para testes estatísticos e ajustes.
  - `matplotlib` para visualização de dados.

## Instruções para Reprodução

### 1. Processamento Estrutural (Java)
O código em Java utiliza a classe `Digraph` para carregar a rede e exportar a distribuição de frequências.

1. Certifique-se de ter o arquivo `algs4.jar` no seu classpath.
2. Coloque o dataset `data.txt` na raiz do projeto.
3. Compile e execute o arquivo `AnaliseGrafos.java`.
   - **Saída:** Serão gerados os arquivos `distribuicao_indegree.csv` e `distribuicao_outdegree.csv`.

### 2. Análise Estatística (Python)
Com os arquivos CSV gerados, o script Python realiza o ajuste dos modelos matemáticos.

1. Instale as dependências: `pip install pandas matplotlib powerlaw numpy`.
2. Execute os scripts de análise para gerar os gráficos e métricas presentes em `Grafos-Unidade 01/Arquivos Python`.

*Replicável com outros grafos direcionados.
