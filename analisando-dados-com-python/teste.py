# Passo a passo do projeto
# Passo 1: Importar a base de dados de clientes
# Passo 2: Visualizar a base de dados
# Passo 3: Corrigir as cagadas da base de dados
# Passo 4: Análise dos cancelamentos
# Passo 5: Análise da causa do cancelamento

import pandas as pd

# Passo 1: Importar a base de dados de clientes
tabela = pd.read_csv("cancelamentos_sample.csv")

# Passo 2: Visualizar a base de dados
# colunas inúteis - informações que não te ajudam, te atrapalham
tabela = tabela.drop(columns="CustomerID")
print(tabela)

# Passo 3: Corrigir as cagadas da base de dados
# valores vazios - erros de preenchimento 
print(tabela.info())
tabela = tabela.dropna()
print(tabela.info())

# Passo 4: Análise dos cancelamentos
print(tabela["cancelou"].value_counts())

print(tabela["cancelou"].value_counts(normalize=True))
#display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

import plotly.express as px

# criar o grafico
grafico = px.histogram(tabela, x="idade", color="cancelou")

# exibir o grafico
grafico.show()
