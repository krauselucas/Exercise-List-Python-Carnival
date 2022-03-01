# Exercício 1:

# Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
# •	A soma de A e B;
# •	A diferença quando se subtrai B de A;
# •	O produto (multiplicação) entre A e B;
# •	O quociente (parte inteira da divisão) quando se divide A por B;
# •	O resto da divisão entre A e B;
# •	O resultado de log10 de A;
# •	O resultado de A elevado a B;

# Dica!
# Para calcular o log10, utilize a função log10 do módulo math conforme exemplo abaixo
# >>> from math import log10
# >>> log10(100)
# 2.0

# A = int(input("Digite um número inteiro: "))

# B = int(input("Digite um número inteiro: "))

# soma = A + B

# diferenca = A - B

# produto = A * B

# quociente = A // B

# resto = A % B

# from math import log10

# resultado_log = log10(A)

# resultado_exp = A ** B

# print(f"O resultado da soma é: {soma}.\nO resultado da diferença é: {diferenca}.\nO resultado da multiplicação é: {produto}.\nO quociente da divisão é: {quociente}.\nO resto da divisão é: {resto}.\nO resultado do log10 de A é: {resultado_log}.\nO resultado da exponenciação é: {resultado_exp}.")

# Exercício 2:

# Faça um programa que receba a base e altura de um triângulo e imprima a área dele.

# Dica!
# A área de um triângulo é dada pela seguinte fórmula abaixo
# area=(base x altura)/2

# base = float(input("Digite o valor da base do triângulo: "))

# altura = float(input("Digite o valor da base do triângulo: "))

# unidade_medida = input("Digite a unidade de medida dos valores indicados do triângulo: ")

# area = (base * altura) / 2

# print(f"A área do triângulo é de {area} {unidade_medida}².")

# Exercício 3:

# No exercício acima você calculou a área de um triângulo a partir da sua base e altura. Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.


# Dica!
# A área de um triângulo também é dada pela seguintes fórmulas abaixo
# s=(s1+s2+s3)/2
# area=√(s.(s-s1).(s-s2).(s-s3))

# lado1 = float(input("Digite o valor do lado1 do triângulo: "))

# lado2 = float(input("Digite o valor do lado2 do triângulo: "))

# lado3 = float(input("Digite o valor do lado3 do triângulo: "))

# unidade_medida = input("Digite a unidade de medida dos valores indicados do triângulo: ")

# s = (lado1 + lado2 + lado3) / 2

# from math import isqrt

# area = isqrt(int(s * (s - lado1) * (s - lado2) * (s - lado3)))

# print(f"A área do triângulo é de {area} {unidade_medida}².")

# Exercício 4:

# Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.

# Dica!
# O IMC é calculado de acordo com a fórmula abaixo
# IMC=peso/altura^2

# peso = float(input("Digite seu peso em kg: "))

# altura = float(input("Digite sua altura em metros: "))

# imc = peso / (altura ** 2)

# print(f"Seu IMC é {imc}.")

# Exercício 5:

# Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.

# numero = input("Digite um número inteiro com 4 dígitos: ")

# digitos = [int(x) for x in str(numero)]

# soma = int(sum(digitos))

# print(f"O somatório dos dígitos de {numero} é {digitos[0]} + {digitos[1]} + {digitos[2]} + {digitos[3]} = {soma}.")