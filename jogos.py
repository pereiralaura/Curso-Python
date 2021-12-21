#Bibliotecas e Importações
import forca
import adivinhacao

def escolhe_jogo():
    #mensagem inicial
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************")
    print("(1) Forca (2) Adivinhação")

    #Variáveis
    jogo = int(input("Qual jogo?"))

    #Lógica da escolha
    if(jogo == 1):
        print("Jogando forca")
        forca.jogar() #colocar nome do módulo antes para chamar
    elif(jogo ==2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

#determinação se o programa é principal ou não
if(__name__ == "__main__"): #__name__ é uma variável embutida que avalia o nome do módulo atual  
    escolhe_jogo()
    