#Importar módulos úteis
from bs4 import BeautifulSoup
import requests
import pandas as pd


#Acessar o site que queremos minerar
url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

#Procurar a informação e filtrar por produto
price = soup.find_all("div", class_="product-wrapper card-body")

#Criação do DataFrame para inserção dos dados minerados
dataset = pd.DataFrame({"Tituto": [], 
                        "Descricao": [],
                        "Valor": [],
                        "Revisao": [],
                        "Nota": []})

#Iterar sobre cada prdouto e pegar as infromações úteis
for produto in price:
    #Criar linha para alocar os dados
    row_data = []
    #Minerar dados
    titulo = produto.find("a", class_="title").text.strip()
    valor = produto.find("h4", class_="price float-end card-title pull-right").text.strip()
    descricao = produto.find("p", class_="description card-text").text.strip()
    revisao = produto.find("p", class_="review-count float-end").text.strip()
    nota = len(produto.find_all("span", class_="ws-icon ws-icon-star"))
    #Alocar os dados minerados
    row_data = [titulo, descricao, valor, revisao, nota]
    #Adicionar nova linha no DataFrame
    dataset.loc[len(dataset)] = row_data

#Verificar no terminal antes de criar arquivo
#print(dataset.head())

#Salvar em um arquivo no CSV
dataset.to_csv("trab_pinho.csv", index=False)
