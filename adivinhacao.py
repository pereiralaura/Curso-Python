#bibliotecas
import random

#definir função, todo código identado vai ficar dentro dessa função
def jogar():

  #mensagem inicial
  print("********************************")
  print("Bem vindo no jogo de Adivinhação")
  print("********************************")

  #variáveis
  numero_secreto = random.randrange(1,101) #random gera número aleatório
  total_de_tentativas = 0
  pontos = 100

  #níveis de dificuldade
  print("Qual nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina um nível: "))

  if(nivel == 1):
    total_de_tentativas = 20
  elif(nivel == 2):
    total_de_tentativas = 10
  else:
    total_de_tentativas = 5

  #lógica das rodadas
  for rodada in range( 1, total_de_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    #condições do jogo
    if(chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue

    #acertos e erros
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    #retorno do jogo
    if(acertou):
      print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
      break
    else: 
      if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
      elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

      #pontuação
      pontos_perdidos = abs(numero_secreto - chute)
      pontos = pontos - pontos_perdidos

  #final do jogo
  print("Fim de jogo! O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

#determinação se o programa é principal ou não
if(__name__ == "__main__"): #__name__ é uma variável embutida que avalia o nome do módulo atual  
  jogar()