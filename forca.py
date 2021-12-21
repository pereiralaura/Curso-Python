
#definir função, todo código identado vai ficar dentro dessa função
def jogar():
    
    #mensagem inicial
    print("**************************")
    print("Bem vindo no Jogo da Forca")
    print("**************************")

    #variáveis
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    
    #lógica do jogo
    while (not enforcou and not acertou):  #enquanto (True) continua executando
        
        chute = input("Qual letra? ")
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        
        print("Jogando...")

    #final do jogo
    print("Fim de jogo!")
    
#determinação se o programa é principal ou não
if(__name__ == "__main__"): #__name__ é uma variável embutida que avalia o nome do módulo atual    
    jogar()