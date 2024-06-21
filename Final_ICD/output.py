import pandas as pd

#Criação do DataFrame para inserção dos dados minerados

def create():
    dataset = pd.DataFrame({"Produto": [], 
                            "Valor": [],
                            "Valor Pix": [],
                            "Valor à prazo": [],
                            "Avaliação Média": [],
                            "Sentimento": [],
                            "Estrelas Média": [],
                            "Mulheres": [],
                            "Homens": []
                            })
    return dataset

def add(dataset, produto):
    #Criar linha para alocar os dados
    row_data = [produto["titulo"],
                produto["valorOriginal"],
                produto["valorPix"],
                produto["valorPrazo"],
                produto["avaliacao"],
                produto["sentimento"],
                produto["estrelas"],
                produto["qtdMulheres"],
                produto["qtdHomens"]
        ]
    #Verificar no terminal antes de criar arquivo
    dataset.loc[len(dataset)] = row_data
    return dataset

#Salvar em um arquivo no CSV
def save(dataset):
    dataset.to_csv("god_pinho_final.csv", index=False)
