#Import openAI
from openai import OpenAI
client = OpenAI(api_key="sk-proj-ojCZAlob0m5GVMbjhj5YT3BlbkFJvWELfJ1tHGqLjAEKS6fP")

#Funcao para solicitar palavra ao ChatGPT
def make(prompt, model = "gpt-3.5-turbo-0125", max_tokens = 100, temperature = 1):
    resposta = client.chat.completions.create(
        messages = prompt,
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
    )
    prompt.append({"role":"assistant","content":resposta.choices[0].message.content})
    return resposta.choices[0].message.content

#Funcao para pegar parametros passados pelo usuario e solicitar palavra
def get(difficulty = "Media", lenght = 5, language = "Ingles", context = "qualquer"):
    if(difficulty==None or difficulty==""):
        difficulty = "Media"
    if(lenght==None or lenght==""):
        lenght = 5
    if(language==None or language==""):
        language = "Inglês"
    if(context==None or context==""):
        context = "qualquer"

    prompt = [{"role":"user", "content":f"Gere uma palavra de exatas {lenght} letras em {language} relacionada a um contexto {context} para um jogo de forca na dificuldade {difficulty}. Retorne apenas a palavra sem acentuação, sem pontuação e em minúsculo."}]
    return make(prompt)
    


