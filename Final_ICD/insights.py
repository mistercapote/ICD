from openai import OpenAI

#Funcao para solicitar palavra a ChatGPT
def chat(prompt, chave, model = "gpt-3.5-turbo-0125", max_tokens = 1000, temperature = 0.5):
    client = OpenAI(api_key=chave)
    resposta = client.chat.completions.create(
        messages = prompt,
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
    )
    return resposta

def interpretar(lista_avaliacoes, chave):
    texto = "Condidere a seguinte lista de avaliações acerca de um produto: {lista_avaliacoes}."
    
    prompt = [{"role":"user", "content":f"{texto} Resuma todas as avaliações em uma sentença de no máximo duas linhas."}]
    avaliacaoMedia = chat(prompt, chave).choices[0].message.content

    prompt = [{"role":"user", "content":f"{texto} Dê o veredito sobre o produto. Retorne apenas 'Bom' ou 'Ruim'."}]
    sentimento = chat(prompt, chave).choices[0].message.content

    return avaliacaoMedia, sentimento

def avaliarNome(lista_nomes, chave):
    texto = "Condidere a seguinte lista de nomes de pessoas: {lista_nomes}."
    prompt = [{"role":"user", "content":f"{texto} Dê a quantidade de nomes masculinos e de nomes femininos. Retorne apenas 'x homens e y mulheres' nessa ordem."}]
    resposta = chat(prompt, chave).choices[0].message.content.split(" ")
    qtdHomens = resposta[0]
    qtdMulheres = resposta[3]
    return qtdMulheres, qtdHomens


#prompt.append({"role":"assistant","content":resposta.choices[0].message.content}) 


    
    


