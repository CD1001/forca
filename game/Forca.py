#biblioteca para Escolhas aleatorias
import random

#importando as funções do outro arquivo
import fucoes as fun

#Lista para o filtro 1
letra1 = "abcdefghijklmnopqrstuvwxyz"

#Usando a função que importar as palavras do arquivo texto
conteudo, x = fun.impot_palavras()

#escolhendo uma linha aleatoria
numero = random.randrange(0, x)

#diminuindo a fonte da palavra e tirando os espaços
palavra = conteudo[numero].lower().strip()

#lista de letras erradas e numero de tentativas
letras = []
tentativas = 0

#lista com a palavra sorteada mas com '_' no lugar das letras 
tracos = ['_' for i in palavra ]
fun.limpa_tela()
print("Bem vindo ao Jogo da forca.")
print("Adivinhe a palavra abaixo:")

while tentativas < 7:
    fun.desenha_forca(tentativas)

    print(''.join(tracos))

    print("\nTentativas Restantes:",tentativas)
    
    print("letras Eradas:\n",letras)
    
    #pedindo para escolher a letra
    escolha = input("Escolha uma letra\n").lower()
    
    #filtro 1, recusa qualquer entrada diferente de letras
    if escolha in letra1:
    
        #filtro 2, não considera letras repetidas
        if escolha not in letras and escolha not in tracos:
    
            #Checando se a letra escolhida esta na palavra
            if escolha in palavra:
                index = 0
    
                for letra in palavra:
                    if escolha == letra:
                        fun.limpa_tela()
                        tracos[index] = escolha
                    index += 1
    
            #Caso a letra não esteja na palavra
            else:
                fun.limpa_tela()
                letras.append(escolha)
                tentativas +=1
    
            #checagem para ver se a pessoa já completou a palavra secreta
            if "_" not in  tracos:
                print("Você venceu, a palavra era:", palavra)
                print("Sobraram",tentativas,"tentativas.")
                print("Você errou essas Letras",letras)
                break
    
        else:
          fun.limpa_tela()
          print(escolha,' Já foi escolhida\n')   
    
    else:
        fun.limpa_tela()
        print(escolha,' Não é uma letra.\n')

#Mesagem de derrota após a tentativas acabarem
if "_" in tracos:
    fun.desenha_forca(tentativas)
    print("Letras eradas:", letras)
    print("\nVocê perdeu, a palavra era:", palavra)
