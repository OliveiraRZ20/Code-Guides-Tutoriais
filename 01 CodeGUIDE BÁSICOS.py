# codigo criado para informar algo sobre a linguagem python caso voce tenha esquecido

######################################################################################
# OPERAÇÕES COM NUMEROS
# Soma
4 + 4

# Subtração
4 - 3

# Multiplicação
3 * 3

# Divisão (float)
3 / 2
# Divisão (int)
3 // 2

# Potência
4**2

# Módulo (Resto da divisão)
10 % 3

# Operações com tipos diferentes de números
# float + float = FLOAT
3.1 + 6.4
# 9.5

# int + float = FLOAT
4 + 4.0
# 8.0

# int + int = INT
4 + 4
# 8
######################################################################################

######################################################################################
# CONVERSÃO E IDENTIFICAÇÃO DE NÚMEROS
# Hexadecimal
hex(394)

# Binário
bin(286)

# Função Type
# Ela pode gerar três respostas (int [inteiro], float [decimais], str [string])
type(5)
# int
type(5.0)
# float

ex = "Isso aqui é uma variavel string"
type(ex)
# str

# A FUNÇÃO TYPE PODE RESPONDER TAMBEM PARA LISTAS, DICIONARIOS E TUPLAS
# LISTA = list
# DICIONÁRIO = dict
# TUPLA =

######################################################################################

######################################################################################
# FUNÇÕES
# Valor absoluto (módulo) [abs]
abs(-8)
# 8

# Valor com x casas decimais [round]
x = 2
round(3.14151922, x)

# Potência, número elevado a x potência [pow]
x = 2
pow(4, x)
######################################################################################

######################################################################################
# INDEXAÇÃO
# DICA, O CODIGO QUE UTILIZAR O : FUNCIONA ASSIM [A MOSTRA DESDE : ATÉ ONDE]
# P.S = primeiro numero em python é o [0]
ex2 = "Lucca"
ex2[0]
# L

# P.S = da pra colocar numeros negativos e ler ao contrário [-1]
ex2 = "Lucca"
ex2[-1]
# a

# Slicing ex[x:] começa a mostrar a partir do x caracter
ex2 = "Lucca"
ex2[1:]
# ucca

# Slicing ex[:x] so mostra até o x caracter
ex2 = "Lucca"
ex2[:1]
# L

# P.S = para fazer ele ler ao contrário basta colocar ex[::-1]
ex2 = "Lucca"
ex2[::-1]
# accuL
######################################################################################

######################################################################################
# FUNÇÕES BUILT-IN DE STRING (SEM NECESSIDADE DE FAZER [import])
# Colocar tudo maiusculo [.upper()]
ex3 = "foda-se"
ex3.upper()

# Colocar tudo minusculo [.lower()]
ex3 = "foda-se"
ex3.lower()

# Dividir string por espaços em branco [.split()]
ex4 = "eu gosto muito de comer chocolate"
ex4.split()
# Dividir string por um caracter x [.split(x)]
ex4 = "eu gosto muito de comer chocolate"
ex4.split("x")

# Colocar letra maiuscula no inicio da string [.captalie()]
ex4 = "eu gosto muito de comer chocolate"
ex4.capitalize()

# Contar quantas vezes aparece o caracter x na string [.count("x")]
ex4 = "eu gosto muito de comer chocolate"
ex4.count("x")

# Checar se o conteúdo da string é somente numero [.isalnum()] ou [.isdigit()]
ex4 = "eu gosto muito de comer chocolate"
ex4.isalnum()

# Checar se o conteudo da string esta todo em minúsculo [.islower()]
ex4 = "eu gosto muito de comer chocolate"
ex4.islower()

# Checar se o conteudo da string é somente espaco em branco [.isspace()]
ex4 = "eu gosto muito de comer chocolate"
ex4.isspace()

# Checar se a string acaba com o caracter x [.endswith("x")]
ex4 = "eu gosto muito de comer chocolate"
ex4.endswith("x")
######################################################################################

######################################################################################
# COMPARAÇÃO DE STRING
# é so colocar dois sinais de = entre dois itens que ele retorna [true] ou [false]
print("Python" == "R")
# False
print("Python" == "Python")
# True
######################################################################################

######################################################################################
# LISTAS
# é como se voce criasse uma variavel e guardasse varias coisas nela com colchetes
lista1 = ["arroz", "feijao", "frango", "batata doce"]

# é possivel atribuir cada valor da lista a uma outra variavel
lista1 = ["arroz", "feijao", "frango", "batata doce"]
item1 = lista1[0]
item2 = lista1[1]
item3 = lista1[2]
print(item1)

# substituir item na lista (colocar coordenada)
listaex = ["01", "02", "03", "04"]
listaex[2] = "chocolate"
print(listaex)

# deletar item de uma lista (colocar coordenada)
lista1 = ["arroz", "feijao", "frango", "batata doce"]
del lista1[1]

# listas dentro de listas
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# anexar uma sub-lista a uma variavel
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_01 = lista2[0]
print(list_01)

# anexar item especifico de uma sub-lista a uma variavel
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listitem01 = lista2[0][0]
print(listitem01)

# somar duas listas (somente adicionar sem nenhuma interação)
lista1 = ["arroz", "feijao", "frango", "batata doce"]
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_total = lista1 + lista2
print(lista_total)

# checar existencia de valor especifico [True/False]
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(10 in lista2)

# comprimento de uma lista [len()]
lista1 = ["arroz", "feijao", "frango", "batata doce"]
len(lista1)

# valor maximo de uma lista [max()]
listanum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max(listanum)

# valor mínimo de uma lista [min()]
listanum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min(listanum)

# adicionar item a uma lista [.append("x")]
lista1 = ["arroz", "feijao", "frango", "batata doce"]
lista1.append("x")
print(lista1)

# copiar itens de uma lista pra outra
lista_blank = []
for item in lista1:
    lista_blank.append(item)
print(lista_blank)

# checar qual a coordenada do valor x [.index("x")]
lista1 = ["arroz", "feijao", "frango", "batata doce"]
lista1.index("frango")

# inserir valor em lista [.insert(coordenada, "x")]
lista1 = ["arroz", "feijao", "frango", "batata doce"]
lista1.insert(2, "x")
print(lista1)

# remover item da lista [.remove("x")]
lista1 = ["arroz", "feijao", "frango", "batata doce"]
lista1.remove("x")
print(lista1)

# colocar a lista ao contrário [.reverse()]
lista1 = ["arroz", "feijao", "frango", "batata doce"]
lista1.reverse()
print(lista1)

# ordenar lista CRESCENTE [.sort()]
listanum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listanum.sort()
print(listanum)
######################################################################################

######################################################################################
# DICIONARIOS
# são listas mas cada elemento tem um valor ao seu lado divido por um : e é cercado por {}
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}

# referenciar a um nome especifico do dicionário retorna o valor dele
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
dict_ex["Lucca"]

# adicionar itens e seus valores a um dicionário
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
dict_ex["Marcelo"] = 23
dict_ex["Marcelo"]

# limpar completamente um dicionário [.clear()]
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
dict_ex.clear()
print(dict_ex)

# DELETAR um dicionário inteiro
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
del dict_ex
print(dict_ex)

# identificar somente os nomes dos itens no dicionario [.keys()]
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
dict_ex.keys()

# identificar somente os valores dos itens do dicionário [.values()]
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
dict_ex.values()

# atualizar valores de um dicionario com outro dicionário [.update()]
dict_ex = {"Lucca": 18, "Bruna": 20, "Ronaldo": 26}
dict_update = {"Roberta": 55, "Jessica": 24}
dict_ex.update(dict_update)

# operacoes com itens de listas dentro do dicionário {dicionário[item][valor].comando()}
dict_lists = {
    "Chave1": ["picanha", "fraldinha", "alcatra"],
    "Chave2": 1230,
    "Chave3": [22, 453, 73, 4],
}
dict_lists["Chave1"][0].upper()

# operação que atualiza o item dentro da lista
dict_lists = {
    "Chave1": ["picanha", "fraldinha", "alcatra"],
    "Chave2": 1230,
    "Chave3": [22, 453, 73, 4],
}
dict_lists["Chave3"][0] -= 2
print(dict_lists)
######################################################################################

######################################################################################
# TUPLAS
# tuplas são basicamente os conjunto do python que usamos geralmente
tupla1 = "Chocolate"

# verificar comprimento da tupla [len(x)]
tupla1 = "Chocolate"
len(tupla1)

# DICA, O CODIGO QUE UTILIZAR O : FUNCIONA ASSIM [A MOSTRA DESDE : ATÉ ONDE]
# Slicing de tuplas funciona mas ele retira itens inteiros ao inves de caracteres
tupla2 = ("Chocolate", 23, "Lucca", 9.8, "Python")
tupla2[1:]
# (23, 'lucca', 9.8, 'Python')

# P.S = tuplas não aceitam substituição de item direto e nem o [.append()]
# para fazer isso voce pode transforar a tupla em lista de usar o [.append()]
