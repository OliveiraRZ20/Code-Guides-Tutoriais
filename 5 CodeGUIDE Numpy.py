# funcoes da biblioteca NUMPY que ja vem com anaconda mas tem que lembrar de importar sempre que for usar seu bobao

######################################################################################

# O Numpy é traduzido para numerical python, que acaba falando por si so o que ele sabe fazer ne
# A ideia principal dele é matematica, principalmente falando de arrays e matrizes

# a primeira coisa que da pra mostrar é a criação de um array comum
# é bem parecido com uma lista normal do python mas a partir dai vc cria um objeto de array do numpy

# OBS: sempre lembrar de importar ele primeiro

######################################################################################
# CRIAR ARRAY

import numpy

arr1 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr1)
# Saida: [ 1  2  3  4  5  6  7  8  9 10]

######################################################################################

# TIPO DE OBJETO
# o tipo de objeto que voce criou pode ser visto usando o comando type

type(arr1)
# Saida: numpy.ndarray

######################################################################################

# TAMANHO DE UM ARRAY

arr1.shape
# Saida: (10,)

######################################################################################

# IMPRIMIR ELEMENTOS ESPECIFICOS

# a idea por tras é identica a do python original
# utilize os colchetes e até o ":"

arr1[4]
# Saida: 5

# uma outra estratégia é criar uma lista com os indices necessários

indices = [1,2,5,6]

arr1[indices]
# Saida: array([2, 3, 6, 7])

# ou talvez uma mascara para aplicar uma função encima dos itens do array
# o exemplo abaixo faz uma mascara booleana encima do arr1 retorando True ou False para cada item
mask = (arr1 % 2 == 0)

arr1[mask]
# Saida: array([ 2,  4,  6,  8, 10])

######################################################################################

# TRANSFORMAÇÃO DE ELEMENTOS DE UM ARRAY

# é possivel alterar o valor de itens de um array com o comando abaixo

arr1[0] = 100

print(arr1)
# Saida: [100   2   3   4   5   6   7   8   9  10]

# Porém, não é possivel incluir elementos de outro tipo dentro do array

try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida!")

# Saida: Operação nãO permitida!

######################################################################################

arr2 = numpy.array([1, 2, 3, 4, 5])

# Método CUMSUM = faz um somatório dos itens de um array a medida de avança

arr2.cumsum()
# Saida: array([ 1,  3,  6, 10, 15])

######################################################################################

# Método CUMPROD = faz a mesma coisa so que multiplicando os itens a medida que avança

arr2.cumprod()
# Saida: array([  1,   2,   6,  24, 120])

######################################################################################

# Função ARANGE = igual ao RANGE do python (Começa por, Termina em, de quantos em quantos)

arr3 = numpy.arange(0, 50, 5)

print(arr3)
# Saida: [ 0 5 10 15 20 25 30 35 40 45]

######################################################################################

# Função ZEROS = cria um array preenchido com zeros {numpy.zeros(n)}

arr4 = numpy.zeros(10)
# Saida: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

######################################################################################

# Funçao EYE = retorna 1 nas posicoes em diagonal e 0 no restante

arr5 = numpy.eye(3)
# Saida: [[1. 0. 0.]
#         [0. 1. 0.]
#         [0. 0. 1.]]

######################################################################################

# Função DIAG = transforma lista de valores em matriz com os mesmos na diagonal em volta de zeros

arr6 = numpy.diag(dsa.array([1, 2, 3, 4]))
# Saída: [[1 0 0 0]
#         [0 2 0 0]
#         [0 0 3 0]
#         [0 0 0 4]]

######################################################################################

# Função ONES = retorna uma matriz de tamanho especificado no comando somente com números 1

arr10 = dsa.ones((2,3))
# Saída: [[1. 1. 1.]
#         [1. 1. 1.]]

######################################################################################

# é Possivel criar arrays utilizando praticamente tudo, desde valores booleanos como True e False
# até strings completas como segue o exemplo abaixo

arr7 = numpy.array([True, False, False, True])
# Saída: [ True False False  True]

arr8 = numpy.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])
# Saída: ['Linguagem Python' 'Linguagem R' 'Linguagem Julia']

######################################################################################

# Criando uma matriz
arr9 = numpy.array( [ [1,2,3] , [4,5,6] ] ) 

type(arr9)
# Saída: numpy.ndarray

print(arr9)
# Saída: [[1 2 3]
#         [4 5 6]]

print(arr9.shape)
# Saída: (2,3)

# Outro jeito de se criar matrizes

lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]

arr11 = dsa.matrix(lista)

type(arr11)
# Saída: numpy.matrix

print(arr11)
# Saída: [[13 81 22]
#         [ 0 34 59]
#         [21 48 94]]

dsa.shape(arr11)
# Saída: (3,3)

# P.S = matrix é pra matematica, ndarray é pra analise de dados
# Dica da data science

######################################################################################

# Metodo Size = ele retorna o numero de elementos presentes naquele array por completo

arr11.size
# Saída: 9

######################################################################################

# Indexação de matriz

arr11[2,1]
# Saída: 48

# P.S: lembre se que python começa em 0, então seria linha 2 coluna 1 (significa 3,2)

######################################################################################

# Alterando um elemento da matriz
arr11[1,0] = 100

print(arr11)

# Saída: [[ 13  81  22]
#         [100  34  59]
#         [ 21  48  94]]

######################################################################################

# Função Dtype

x = dsa.array([1, 2])  # NumPy decide o tipo dos dado
y = dsa.array([1.0, 2.0])  # NumPy decide o tipo dos dado
z = dsa.array([1, 2], dtype = dsa.float64)  # Forçamos um tipo de dado em particular

print(x.dtype, y.dtype, z.dtype)
# Saída: int64 float64 float64

######################################################################################

arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)

# funcao itemsize = fala o numero de bytes necessarios para armazenar cada item no array

arr12.itemsize
# Saída: 8

######################################################################################

# funcao nbytes = fala o numero de bytes total que aquele array consome

arr12.nbytes
# Saída: 64

######################################################################################

# função ndim = fala o numero de dimensoes do array tal.

arr12.ndim
# Saída: 2

######################################################################################

# ARRAYS EM 3D

arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

# Saída: 
#[[[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# [[13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]]

arr_3d.ndim
# Saída: 3

arr_3d.shape
# Saída: (2,3,4)

arr_3d[0, 2, 1]
# Saída: 10

######################################################################################

# manipulação de arquivos com numpy

# use o (import os) para poder utilizar arquivos do computador

import os
filename = os.path.join('dataset.csv')

# função loadtxt

arr13 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1,2,3), skiprows = 1)

# delimiter = separador para cada item
# usecols = escolher colunas a serem utilizadas
# skiprows = pular n linhas para evitar pegar os títulos

######################################################################################

# função mean

# ela realiza a média de um array numpy

arr14 = dsa.array([15, 23, 63, 94, 75])

dsa.mean(arr14)
# Saída: 54.0

######################################################################################

# função std (desvio padrão)

# ela realiza o desvio padrão de um array numpy

dsa.std(arr14)
# Saída: 30.34468652004828

######################################################################################

# função var (variância)

# ela realiza a variância de um array numpy

dsa.var(arr14)
# Saída: 920.8

######################################################################################

# função dot (multiplicação de matrizes)

# ele vai multiplicar as duas matrizes 
# P.S = o numero de colunas da primeira tem que ser igual ao de linhas da segunda

arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])

arr19.shape
# Saída: (2, 2)

arr20.shape
# Saída: (2, 2)

arr21 = dsa.dot(arr19, arr20)

print(arr21) 

# Saída: [[ 5 20]
#         [15 46]]

# OBS: tambem é possivel utilizar o @ como comando de multiplicação que funciona da mesma maneira

arr21 = arr19 @ arr20

print(arr21) 

# Saída: [[ 5 20]
#         [15 46]]

######################################################################################

# função de fatiamento (slicing) no numpy

# quand for chamar um array, utilize a seguinte indexação

arr22 = dsa.diag(dsa.arange(3))

print(arr22)
# Saída: [[0 0 0]
#         [0 1 0]
#         [0 0 2]]

arr22[1, 1]
# Saída: 1

arr22[1]
# Saída: array([0, 1, 0])

# SLICING (chamou uma coluna completa)
arr22[:,2]
#Saída: array([0, 0, 2])

######################################################################################

# comparação de arrays

# é só utilizar o metodo ("==") que ele gera um array de valores booleanos

a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])

a == b
# Saída: array([False,  True, False,  True])

# comparação global array_equal(x, y)

# ele compara os dois como um todo e diz se eles são completamente iguais diretamente

dsa.array_equal(arr22, arr23)
# Saída: False

######################################################################################

# função min()

# retorna o valor mínimo de um array

arr23 = dsa.arange(10)

print(arr23)
# Saída: [0 1 2 3 4 5 6 7 8 9]

arr23.min()
# Saída: 0

######################################################################################

# função max()

# retorna o valor máximo de um array

arr23.max()
# Saída: 9

######################################################################################

# somando um valor a cada elemento do array

dsa.array([1, 2, 3]) + 1.5
# Saída: array([2.5, 3.5, 4.5])

######################################################################################

# função around(x)

# ela vai arredondar todos os valores do array para o inteiro mais próximo
# P.S = 5 arredondado vai pra cima

arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])

print(arr24)
# Saída: [1.2 1.5 1.6 2.5 3.5 4.5]

arr25 = dsa.around(arr24)

print(arr25)
# Saída: [1. 2. 2. 2. 4. 4.]

######################################################################################

# função flatten()

# ela faz um achatamento de matriz, transformando ela em uma lista com uma única dimensão

arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr26)
# Saída: [[1 2 3 4]
#         [5 6 7 8]]

arr27 = arr26.flatten()

print(arr27)
# Saída: [1 2 3 4 5 6 7 8]

######################################################################################

# função repeat(array(x), n vezes)

# ele vai pegar cada item do array original e duplicar ele pro número (n)

arr28 = dsa.array([1, 2, 3]) 

print(arr28)
# Saída: [1 2 3]

dsa.repeat(arr28, 3)
# Saída: array([1, 1, 1, 2, 2, 2, 3, 3, 3])

######################################################################################

# função tile(array(x), n vezes)

# ele vai pegar o array por completo e duplicar ele em sequencia (n) vezes

arr28 = dsa.array([1, 2, 3])

print(arr28)
# Saída: [1 2 3]

dsa.tile(arr28, 3)
# Saída: array([1, 2, 3, 1, 2, 3, 1, 2, 3])

######################################################################################

# função copy(x)

# ela vai copiar exatamente o array (x) e atribuir a outra variável

arr29 = dsa.array([5, 6])

arr30 = dsa.copy(arr29)

print(arr30)
# Saída: [5 6]

######################################################################################