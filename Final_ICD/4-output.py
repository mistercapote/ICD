import pandas as pd

#Criação do DataFrame para inserção dos dados minerados
dataset = pd.DataFrame({"Tituto": [], 
                        "Descricao": [],
                        "Valor": [],
                        "Revisao": [],
                        "Nota": []})

#Criar linha para alocar os dados
row_data = []

#Adicionar nova linha no DataFrame
dataset.loc[len(dataset)] = row_data

#Verificar no terminal antes de criar arquivo
#print(dataset.head())

#Salvar em um arquivo no CSV
dataset.to_csv("trab_pinho.csv", index=False)
