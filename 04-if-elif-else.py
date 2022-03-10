# Exercício 1:

# Escreva um programa que diga se um número dado pelo usuário é par ou ímpar

number = int(input("Digite um número: "))

if number % 2 == 0:
    print("O número é par.")
elif number == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
        
# Exercício 2:

# Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.

number1 = int(input("Digite o primeiro número: "))

number2 = int(input("Digite o segundo número: "))

division = number1 % number2

if division == 0:
    print(f"O número {number1} é divisível pelo número {number2}.")
else:
    print(f"O número {number1} não é divisível pelo número {number2}.")


# Exercício 3:

# A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
# Barulho	Nível sonoro (dB)
# Britadeira	130
# Cortador de grama	106
# Despertador	70
# Cômodo em silêncio	40


# Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 

valor = int(input("Digite o valor medido em decibeis: "))

if valor > 130:
    print("O ruido é superior ao de uma britadeira.")
elif valor == 130:
    print("O ruido é igual ao de uma britadeira.")
elif valor > 106:
    print("O ruido está entre o emitido por um cortador de grama e uma britadeira.")
elif valor == 106:
    print("O ruido é igual ao de um cortador de grama.") 
elif valor > 70:
    print("O ruido está entre o emitido por um cortador de grama e um despertador.")
elif valor == 70:
    print("O ruido é igual ao de um despertador.")
elif valor > 40:
    print("O ruido está entre o emitido por um cômodo em silêncio e um despertador.")
elif valor == 40:
    print("O ruido é igual ao de um cômodo em silêncio.")
else:
    print("O ruido emitido é inferior ao de um cômodo em silêncio.")

# Exercício 4:

# Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:

# 1.	Um ano que é divisível por 400 é bissexto.
# 2.	Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
# 3.	Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
# 4.	Todos os outros anos não são bissextos

ano = int(input("Digite um ano: "))

if ano%400 == 0:
    print(f"{ano} é ano bissexto.")
elif ano%4 == 0 and ano%100 != 0:
    print(f"{ano} é ano bissexto.")
else:
    print(f"{ano} não é ano bissexto.")

# Exercício 5:

# Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
# •	Dada a entrada ABT-1234 o programa deveria exibir True
# •	Dada a entrada JKL9999 o programa deveria exibir False
# •	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 

placa = input("Digite a placa: ")

if "-" in placa:
    partes = placa.split("-")     
    print(len(partes[0]) == 3 and len(partes[1]) == 4 and partes[0].isalpha() and partes[1].isdigit())
else:
    print(False)
