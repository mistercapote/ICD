import word as wd
import levels as ll

def play(usuario, setting):
    #Definir um print padrão
    def prints(guessed, tries, resposta, band):
        print("=========================")
        if band: tries=7
        print(ll.dead_levels(tries, usuario))
        print(resposta)
        print("Adivinhe:", guessed)
        print("========================")

    #Iniciar a palavra
    if len(setting) == 0:
        word = wd.get()
    else:
        word = wd.get(difficulty = setting.get("difficulty"),
                      lenght = setting.get("lenght"), 
                      language = setting.get("language"), 
                      context = setting.get("context")
        )
    
    #Iniciar variaveis
    word = word.lower()
    guessed = "_" * len(word)
    band = False
    historic_letter = []
    guessed_word = []
    tries = 6

    print("Vamos jogar!!!!")
    prints(guessed, tries, "", band)

    while not band and tries > 0:
        resposta = ""
        letter = input("Digite uma letra: ").lower()
        #Validar se o digitado realmente é uma letra:
        if len(letter) == 1 and letter.isalpha():
            #Verificar se a letra ja foi enviada:
            if letter in historic_letter:
                resposta = f"A letra {letter} já foi enviada!"
            #Verificar se a letra pertence a palavra:
            elif letter not in word:
                resposta = f"A letra {letter} não está na palavra!"
                historic_letter.append(letter)
                tries -= 1
            #A letra pertence a palavra:
            else:
                resposta = f"A letra {letter} está na palavra!"
                historic_letter.append(letter)
                word_as_list = list(guessed)
                indices = [i for i, l in enumerate(word) if l == letter]
                #Atualizar a palavra escondida com a letra digitada:
                for index in indices:
                    word_as_list[index] = letter
                guessed = "".join(word_as_list)
                #Verificar se o jogo acabou:
                if "_" not in guessed:
                    band = True
        #Verificar se o usuario adivinhou a palavra
        elif len(letter) >= 2 and letter.isalpha():
            if letter in guessed_word:
                resposta = f"A palavra {letter} já foi enviada!"
            elif letter != word:
                resposta = f"{letter} não é a palavra"
                tries -= 1
                guessed_word.append(letter)
            else:
                band = True
                guessed = word
        else:
            resposta = "Apenas letras"
        prints(guessed, tries, resposta, band)
    
    if band:
        print("Vitória!!!")
    else:
        print("Nhe, a palavra era " + word + ". Mais triste que Palmeiras com Mundial")
    

#Definir configuracoes
def settings():
    setting = dict()
    setting["difficulty"] = input("Dificuldade: ")
    setting["lenght"] = input("Tamanho da palavra: ")
    setting["language"] = input("Idioma: ")
    setting["context"] = input("Tema: ")
    return setting


#Iniciar o programa:
def main():
    usuario = input("Nome de usuario: ")
    entrada = input("Digite J para Jogar ou C para configurações: ").lower()
    setting = dict()
    if entrada == "j":
        play(usuario, setting)
    elif entrada == "c":
        setting = settings()
        play(usuario, setting)
   
main()