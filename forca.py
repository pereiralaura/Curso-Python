
#definir função, todo código identado vai ficar dentro dessa função
def jogar():
    
    #mensagem inicial
    print("**************************")
    print("Bem vindo no Jogo da Forca")
    print("**************************")

    #variáveis
    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    
    print(letras_acertadas)
    
    #lógica do jogo
    while (not enforcou and not acertou):  #enquanto (True) continua executando
        
        chute = input("Qual letra? ")
        chute = chute.strip() #devolve uma string sem espaços
        
        index = 0 #posição
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #str.upper() deixa todas as letras maiúsculas
                    letras_acertadas[index] = letra
            index = index + 1
        
        print(letras_acertadas)

    #final do jogo
    print("Fim de jogo!")
    
#determinação se o programa é principal ou não
if(__name__ == "__main__"): #__name__ é uma variável embutida que avalia o nome do módulo atual    
    jogar()