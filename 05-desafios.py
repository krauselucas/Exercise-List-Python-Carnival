# Desafio 1:

# Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

# 1.	O jogo deve sortear um número entre 1 e 100.
# 2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 1 ou superior a 100. Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
# 3.	O número do usuário deve ser analisado:
# a.	Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é maior.”.
# b.	Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é menor.”.
# c.	Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado” e o jogo deve ser finalizado, sendo apresentado ao usuário a quantidade de tentativas efetuadas até este momento.
# 4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

# Dica!
# Pesquise sobre o módulo buit-in do Python chamado random

import random as rd

restart = "S"

while restart == "S":

    numero_sorteado = rd.randint(1,100)
    
    numero_usuario = int(input("Digite um número entre 1 e 100: "))
    tentativas = 1
        
    while numero_sorteado != numero_usuario:
        while numero_usuario < 1 or numero_usuario > 100:
            numero_usuario = int(input("Digite um novo número, dessa vez, entre 1 e 100: "))
            
        if numero_sorteado > numero_usuario:
            print("O número sorteado é maior.")
            numero_usuario = int(input("Digite outro número entre 1 e 100: "))
                
        elif numero_sorteado < numero_usuario:
            print("O número sorteado é menor.")
            numero_usuario = int(input("Digite outro número entre 1 e 100: "))                
        tentativas = tentativas + 1

    print(f"Parabéns! Você acertou o número sorteado: {numero_sorteado}.\nVocê precisou somente de {tentativas} tentativas.")
    restart = input("Para jogar de novo, digite 'S' e pressione Enter.").upper()

print("Que pena, volte logo!")

# Desafio 2:
# Implemente um jogo em que o usuário tenha que adivinhar o somatório de dois dados.
# 1.	O jogo deve sortear um número para cada dado. Estes números devem variar entre 1 e 6, inclusive. Deve-se calcular a soma dos dois valores.
# 2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 2 ou superior a 12. Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
# 3.	O número do usuário deve ser analisado e o resultado da jogada deve ser apresentado na tela:
# a.	Caso o usuário informe um número superior ou inferior à soma dos dados, o jogo deve apresentar a mensagem “Você errou. A soma dos dados é x. O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo x o valor da soma, d1 o valor do primeiro dado e d2 o valor do segundo dado.
# b.	Caso o usuário informe um número igual ao valor da soma, o jogo deve apresentar a mensagem “Parabéns! Você acertou a soma dos dados! O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo d1 o valor do primeiro dado e d2 o valor do segundo dado
# 4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

import random as rd

restart = "S"
while restart == "S":

    d1 = rd.randint(1,6)
    d2 = rd.randint(1,6)
    x = d1 + d2
    
    numero_usuario = int(input("Digite um número entre 2 e 12: "))

    while numero_usuario < 2 or numero_usuario > 12:
        numero_usuario = int(input("Digite um outro número, dessa vez, entre 2 e 12: "))

    if x != numero_usuario:
        print(f"Você errou. A soma dos dados é {x}.\nO valor do primeiro dado é {d1} e o do segundo é {d2}.")
    else:
        print(f"Parabéns! Você acertou a soma dos dados!\nO valor do primeiro dado é {d1} e o do segundo é {d2}.")

    restart = input("Para jogar de novo, digite 'S' e pressione Enter.").upper()

print("Jogo encerrado, até a próxima!")

# Exercício 3:
# Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.

# O que são anagramas? https://pt.wikipedia.org/wiki/Anagrama

# Bom divertimento!
