from bs4 import BeautifulSoup
import requests
import clean
import insights
import output

LINK = "https://www.casaevideo.com.br"

def mine(link, chave):
    #Criar tabela de armazenamento com PANDAS:
    dataset = output.create()

    #Acessar o site, encontrar os produtos:
    url = LINK+link
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    produtos = soup.find_all("a", class_="card gap-2 card-compact md:max-w-[242px] md:max-h-[435px] group w-full bg-neutral-50 p-2 md:py-4 card-bordered border-brand-secondary-100 rounded-lg text-start false")

    #Iterar sobre cada prdouto e pegar as informações úteis:
    for produto in produtos:
        link = produto.get('href')
        titulo = produto.find("h3", class_="truncate text-[#393939] x-small-bold md:body-bold line-clamp-2 whitespace-break-spaces").text.strip()
        valorOriginal = clean.cleanNum(produto.find("span", class_="line-through").text.strip())
        valorPix = clean.cleanNum(produto.find("div", class_="body-bold md:h6-bold-20 text-neutral-dark").text.strip())
        valorPrazo = clean.cleanNum(produto.find("div", class_="text-brand-secondary-900 x-small-regular truncate").text.strip())
        lista_nomes = []
        lista_avaliacoes = []
        lista_estrelas = []

        #Entrar na pagina do produto:
        url = LINK+link
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")
        avaliacoes = soup.find_all("div", class_="flex flex-col w-full border-t-[2px] first:border-0 border-neutral-100 pt-2 first:pt-0")
        
        #Iterar sobre cada avaliacao e pegar as informações úteis:
        for avaliacao in avaliacoes:
            lista_nomes.append(avaliacao.find("strong", class_="small-bold md:body-bold").text.strip())
            #data = clean.cleanData(avaliacao.find("span", class_="x-small-regular text-neutral-500").text.strip())
            lista_avaliacoes.append(avaliacao.find("span", class_="small-regular mt-4").text.strip())
            lista_estrelas.append(len(avaliacao.find_all("use", href="/sprites.svg?__frsh_c=a0b175bd898bea29671733055889f81d68b6bb76#FullStar")))
            
        #Calculo da média de estrelas:
        estrelasMedia = sum(lista_estrelas)/len(lista_estrelas)

        #Consultar OpenAI para avaliar comentarios e definir sexo conforme nome:
        avaliacaoMedia, sentimento = insights.interpretar(lista_avaliacoes, chave)
        qtdMulheres, qtdHomens = insights.avaliarNome(lista_nomes, chave)
        
        #Criar dicionario para armazenar os dados
        produto = {
            "titulo": titulo,
            "valorOriginal": valorOriginal,
            "valorPix": valorPix,
            "valorPrazo": valorPrazo,
            "avaliacao": avaliacaoMedia,
            "sentimento": sentimento,
            "estrelas": estrelasMedia,
            "qtdMulheres": qtdMulheres,
            "qtdHomens": qtdHomens
        }
        #Adicionar nova linha à tabela PANDAS
        dataset = output.add(dataset, produto)
    #Gerar arquivo CSV
    output.save(dataset)

def main():
    chave = input()
    for i in range(1,5):
        mine("/eletroportateis?page="+f"{i}", chave)
