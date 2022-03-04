# Exercício 1:

# Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
# •	Alunos matriculados em inglês:
# o	João Alves dos Santos
# o	Maria Magalhães
# o	Antônio da Silva Ferreira
# o	José Júnior Jarbas
# o	Henrique da Silva Sauro
# o	Joaquina Ferreira da Silva
# o	Fabiana Aparecida Bianco
# o	Marrone Gutierres
# o	Carlos Magno Farad
# o	Antônio da Silva Júnior Amaral

# •	Alunos matriculados em francês:
# o	João Alves dos Santos
# o	Antônio da Silva Ferreira
# o	Fernanda Abdala Mohamed
# o	Abner Mignon Alib
# o	Alisson Figueiredo
# o	Henrique da Silva Sauro
# o	Maria Magalhães
# o	Marrone Gutierres
# o	Joaquina Ferreira da Silva

# Faça um programa que responda as seguintes perguntas:

# 1.	Quantos alunos estão matriculados na escola, no total?
# 2.	Quantos e quais estão matriculados APENAS em INGLES?
# 3.	Quantos e quais estão matriculados APENAS em FRANCES?
# 4.	Quantos e quais estão matriculados EM AMBOS os cursos?
# 5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?

# ingles = ["João Alves dos Santos", "Maria Magalhães", "Antônio da Silva Ferreira", "José Júnior Jarbas", "Henrique da Silva Sauro", "Joaquina Ferreira da Silva", "Fabiana Aparecida Bianco", "Marrone Gutierres", "Carlos Magno Farad", "Antônio da Silva Júnior Amaral"]

# frances = ["João Alves dos Santos", "Antônio da Silva Ferreira", "Fernanda Abdala Mohamed", "Abner Mignon Alib", "Alisson Figueiredo", "Henrique da Silva Sauro", "Maria Magalhães", "Marrone Gutierres", "Joaquina Ferreira da Silva"]

# todos_alunos_com_duplicatas = ingles + frances

# todos_alunos = set(todos_alunos_com_duplicatas)

# todos_alunos = list(todos_alunos)

# apenas_ingles = list(set(todos_alunos) - set(frances))

# apenas_frances = list(set(todos_alunos) - set(ingles))

# ambos_cursos_sem_ingles = list(set(todos_alunos) - set(apenas_ingles))

# ambos_cursos = list(set(ambos_cursos_sem_ingles) - set(apenas_frances))

# apenas_frances_ingles = apenas_ingles + apenas_frances

# print(f"1. Estão matriculados na escola, no total, {len(todos_alunos)} alunos.")

# print(f"2. Estão matriculados apenas em inglês, no total, {len(apenas_ingles)} alunos, sendo eles: {apenas_ingles}.")

# print(f"3. Estão matriculados apenas em frances, no total, {len(apenas_frances)} alunos, sendo eles: {apenas_frances}.")

# print(f"4. Estão matriculados em ambos os cursos, no total, {len(ambos_cursos)} alunos, sendo eles: {ambos_cursos}.")

# print(f"5. Estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos, no total, {len(apenas_frances_ingles)} alunos, sendo eles: {apenas_frances_ingles}.")

# Exercício 2:

# Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

# >>> Digite um estado: SP
# >>> O nome completo do estado é São Paulo.

# siglas_estados = {"AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul", "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná", "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"}

# sigla = input("Digite um estado: ")

# estado = siglas_estados[sigla]

# print(f"O nome completo do estado é {estado}")

# Exercício 3:

# Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
# >>> {“matemática”: 81, “física”: 83, “química”: 87} 
# a saída deve ser 
# >>> {“química”: 87, “física”: 83, matemática”: 81}

# dictionary = {"matemática": 81, "física": 83, "química": 87}

# dictionary_sorted = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse = True))

# print(dictionary_sorted)

# Exercício 4:

# Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
# >>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
# A saída deverá ser
# >>> {1: 8, 2: 4, 3: 6}

# dictionary = {1: "vermelho", 2: "azul", 3: "marrom"}

# len1 = len(dictionary[1])

# len2 = len(dictionary[2])

# len3 = len(dictionary[3])

# dictionary_numbers = dict([(1,len1), (2, len2), (3, len3)])

# print(dictionary_numbers)

# Exercício 5:

# Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
# >>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
# A saída deve ser
# >>> Nota máxima -> Júnior : 80
# >>> Nota mínima -> Theodoro : 20

# dictionary_grades = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

# list_grades = list(dictionary_grades.values())

# list_names = list(dictionary_grades.keys())

# max_grade = max(list_grades)

# min_grade = min(list_grades)

# position_max_grade = list_grades.index(max_grade)

# position_min_grade = list_grades.index(min_grade)

# max_name = list_names[position_max_grade]

# min_name = list_names[position_min_grade]

# print(f"Nota máxima -> {max_name} : {max_grade} \nNota mínima -> {min_name} : {min_grade}")