# Exercício 1:

# Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). Imprima na tela o elemento e sua respectiva posição na lista. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
# >>> Elemento 1 na posição 0
# >>> Elemento 3 na posição 1
# >>> Elemento 6 na posição 2
# >>> Elemento “H” na posição 3

# lista = [1, 2, 3, 4, 5]

# print(f"Elemento {lista[0]} na posição {lista.index(1)}\nElemento {lista[1]} na posição {lista.index(2)}\nElemento {lista[2]} na posição {lista.index(3)}\nElemento {lista[3]} na posição {lista.index(4)}\nElemento {lista[4]} na posição {lista.index(5)}\n")

# Exercício 2:

# Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser
# >>> [[7,7,7], “H”, 6, 3, 1]

# lista_normal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lista_normal.reverse()

# print(lista_normal)


# Exercício 3:

# Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
# >>> O maior elemento é 8 e está na posição 3
# >>> O menor elemento é 3 e está na posição 4

# Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.

# lista = [3, 1, 4, 7, 5, 6]

# maior_elemento = max(lista)

# menor_elemento = min(lista)

# lista.index(maior_elemento)

# lista.index(menor_elemento)

# print(f"O maior elemento é {maior_elemento} e está na posição {lista.index(maior_elemento)}\nO menor elemento é {menor_elemento} e está na posição {lista.index(menor_elemento)}")

# Exercício 4:

# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
# >>> Meses com temperatura acima da média anual de 35,5°:
# >>> 1 – janeiro
# >>> 3 – março
# >>> 6 – junho

# jan = float(input("Temperatura de janeiro: "))
# fev = float(input("Temperatura de fevereiro: "))
# mar = float(input("Temperatura de março: "))
# abr = float(input("Temperatura de abril: "))
# mai = float(input("Temperatura de maio: "))
# jun = float(input("Temperatura de junho: "))
# jul = float(input("Temperatura de julho: "))
# ago = float(input("Temperatura de agosto: "))
# set = float(input("Temperatura de setembro: "))
# out = float(input("Temperatura de outubro: "))
# nov = float(input("Temperatura de novembro: "))
# dez = float(input("Temperatura de dezembro: "))

# lista_temp = [jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]

# media_temp = sum(lista_temp) / len(lista_temp)

# print(f"Meses com temperatura acima da média anual de {media_temp}°")

# if jan > media_temp:
#     print(f"{jan} - janeiro")

# if fev > media_temp:
#     print(f"{fev} - fevereiro")

# if mar > media_temp:
#     print(f"{mar} - março")

# if abr > media_temp:
#     print(f"{abr} - abril")

# if mai > media_temp:
#     print(f"{mai} - maio")

# if jun > media_temp:
#     print(f"{jun} - junho")

# if jul > media_temp:
#     print(f"{jul} - julho")

# if ago > media_temp:
#     print(f"{ago} - agosto")

# if set > media_temp:
#     print(f"{set} - setembro")

# if out > media_temp:
#     print(f"{out} - outubro")

# if nov > media_temp:
#     print(f"{nov} - novembro")

# if dez > media_temp:
#     print(f"{dez} - dezembro")


# Exercício 5:

# Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após o elemento 6000 na lista acima. O resultado final deverá ser:
# >>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# lst2 = lst.pop(2)

# lst3 = lst2.pop(2)

# lst3.append(7000)

# lst2.insert(2, lst3)

# lst.insert(2, lst2)

# print(lst)

# Exercício 6:

# Faça um programa que remova strings vazias de uma lista de strings. Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
# >>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]

# lista = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]

# qtd_vazios = lista.count("")

# for i in range(qtd_vazios):
#     lista.remove("")

# print(lista)

# Exercício 7:

# Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

# Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.

# lista1 = ["1", "7", "99", "15"]

# lista1_int = [int(i) for i in lista1]

# print(lista1_int)

# lista2 = [1, 7, 99, 15]

# lista2_str = [str(i) for i in lista2]

# print(lista2_str)