
# Para desenvolver o jogo da forca em Python, você pode seguir os seguintes passos:
# 1- Definir a lista de palavras possíveis*
# 2- Escolher uma palavra aleatória da lista*
# 3- Criar uma lista vazia para armazenar as letras adivinhadas*
# 4- Definir o número máximo de tentativas permitidas*
# 5- Enquanto o número de tentativas não atingir o limite máximo:
# a. Mostrar a palavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos*
# b. Pedir ao jogador que adivinhe uma letra*
# c. Verificar se a letra adivinhada está na palavra*
# d. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
# e. Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]
# f. Verificar se todas as letras da palavra foram adivinhadas
# g. Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"
# h. Se o número de tentativas restantes chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo
#Função de desenha a forca
#Biblioteca para fução de limpar a tela a cada execução
from os import system, name
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

    # Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

#importando as palavras do arquivo texto
def impot_palavras():
    with open('texto.txt','r') as arquivo:
        conteudo = arquivo.readlines()
    #Lendo o numero de linhas do arquivo das palavras
        x = len(conteudo)
    return conteudo,x