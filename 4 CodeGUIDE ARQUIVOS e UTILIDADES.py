# funcoes de arquivos de texto
# modos de se abrir um arquivo de texto

arq1 = open("arquivos/arquivo2.txt", "r")
# r = somente leitura (READ)

arq1 = open("arquivos/arquivo2.txt", "w")
# w = sobrescrever conteudo do arquivo (WRITE)

arq1 = open("arquivos/arquivo2.txt", "a")
# a = acrescentar texto ao conteudo do arquivo (APPEND)

# ações para fazer com arquivos de texto

arq1.read()
# read() = ler o arquivo

arq1.write()
# write() = escrever no arquivo

arq1.close()
# close() = fechar o arquivo

arq1.seek(0, 0)
# seek() = ir para algum ponto específico do arquivo linha / caracter

arq1.tell()
# tell() = contar o numero de caracteres de um arquivo

arq1.readlines()
# readlines() = ler linha a linha de um arquivo de text

# função with
with open("c:/LUCCA/1-lucca/Teste.txt", "w") as arquivo:
    pass
# ela executa o .close() automaticamente quando termina o loop

###############################################################################################################
# funcoes de arquvos .csv (arquivos que tem suas colunas separadas por virgulas e linhas por "enter")

# lembrar de utilizar o import "csv" para utilizar suas funções
import csv

# criar objeto de gravação
writer = csv.writer(csvfile)

# gravar uma linha no arquivo
writer.writerow(("nota1", "nota2", "nota3"))

# criar objeto de leitura
leitor = csv.reader(csvfile)

# P.S: se utilizar loop for em um arquivo csv, cada i significa uma linha no arquivo

# imprimir a partir da segunda linha
dados = list(leitor)

for i in dados[1:]:
    print(i)

###############################################################################################################
# funcoes de aruqivo .JSON (ele funciona a base de dicionários)

# lembrar de utilizr o import "json" para utilizar suas funções
import json

# converter dados para a linguagem JSON
json.dumps(obj)

# carregar dados de uma variavel em JSON
json.loads(obj)

###############################################################################################################
# extração de arquivos da web

# lembrar de utilizar o metodo de import (from urllib.request import urlopen)
from urllib.request import urlopen

###############################################################################################################


# funcao MAP
# ela consegue apicar uma função a varios valores ao mesmo temo atraves de uma lista
def aoquadrado(x):
    return x**2


numeros = [1, 2, 3, 4, 5]
list(map(aoquadrado, numeros))

# da pra usar com lambda tbm

list(map(lambda x: (5.0 / 9) * (x - 32), numeros))

# P.S: sempre usar LIST na frente pois senao o resultado vai ser um codigo estranho chamado de iterator

###############################################################################################################

# funcao reduce
# extrair do import functools (from functools import reduce)

# parecido com o map mas ele aplica o que a função manda porem concatena os itens em uma coisa só no final

from functools import reduce

num = [1, 2, 3, 4, 5]


def soma(a, b):
    x = a + b
    return x


reduce(soma, num)

###############################################################################################################

# funcao filter
# tambem bem parecido com os dois acima porem ai ele é comparado com um filtro
# também é importante ressaltar que ela precisa receber o list na frente senão ela vai retornar um ITERATOR
# ITERATOR = Código de restreio na memória
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def verificapar(x):
    if x % 2 == 0:
        return True
    else:
        return False


list(filter(verificapar, lista))

###############################################################################################################

# funcao ZIP
# ela serve para combinar os elementos de duas listas
# P.S: o mais importante é que se ela não encontra um par para formar, automaticamente ela descarta o item
# também é importante ressaltar que ela precisa receber o list na frente senão ela vai retornar um ITERATOR
# ITERATOR = Código de restreio na memória

x = [1,2,3]
y = [4,5,6]

zip(x, y) # ISSO ESTÁ ERRADO!!!!

list(zip(x,y))

# exemplo do P.S:
a = [1,2,3]
b = [4,5,6,7,8]

list(zip(a,b)) 

# funciona também com dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

# Zip vai unir as chaves
list(zip(d1,d2))

# P.S: Com dicionários ele por padrão une as chaves automaticamente, caso queria utilizar as chaves utilize .values()
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

list(zip(d1, d2.values()))

###############################################################################################################

# funcão ENUMERATE
# ele conta os itens de uma sequência de itens enumerando cada item com um numero, formando no final uma lista como (numero, valor)
# também é importante ressaltar que ela precisa receber o list na frente senão ela vai retornar um ITERATOR
# ITERATOR = Código de restreio na memória

seq = ['a','b','c']

enumerate(seq) # ISSO ESTÁ ERRADO!!!!!

list(enumerate(seq))

# visualização do trabalho do ENUMERATE
seq = ['a','b','c']

for indice, valor in enumerate(seq):
    print (indice, valor)

# ele funciona também com strings

for i, item in enumerate('Data Science Academy'):
    print(i, item)

###############################################################################################################

# try e except

# ela funciona como forma de tratamento de erro parcial, ela não resolve diretamente o erro mas pode ajudar
# o erro não para de existir mas ele permite a execução do resto do código

# try significa TENTAR, então ele vai executar aquilo independentmente de qualquer coisa
# except significa CASO ALGO DE ERRADO, então ele executa caso tenha algum erro especificado e aplica o que tem dentro de seu bloco


# print('Hello)
# SyntaxError: EOL while scanning string literal

8 + 's'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

def numDiv (num1, num2):
    resultado = num1 / num2
    return resultado
    

numDiv(4,0)
# ZeroDivisionError: division by zero

###############################################################################################################

# expressoes regulares

# P.S: lembrar de importar o re quando for utilizar expressoes regulares
import re

# sua definicao pode ser decrita como uma função para manipular strings e realizar tarefas como
# validação de entrada de dados, extração de informação de strings e substituição de texto

# link da documentação https://docs.python.org/3.9/library/re.html

# exemplo

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."

# utilize o comando re.findall("*char*", *Variavel*)
# esse comando fará uma lista com todos os *char* que ele encontrar, então segue o comando

resultado = len(re.findall("@", texto))
print("O caractere '@' apareceu", resultado, "vezes no texto.")
# O caractere '@' apareceu 2 vezes no texto.

# exemplo 2

# utilize o comando re.findall também mas dessa vez utilizando argumentos especificos da biblioteca re

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."
resultado = re.findall(r'você (\w+)', texto)
# o r antes da string vem para conseguir utilizar o contrabarra como parte do método
# então ele vai procurar palavras que tenham "você " antes dela e adicionar o que ele achar numa lista

print("A palavra após 'você' é:", resultado[0])
# ai ele coloca uma indexação de lista apos fazer a chamada do resultado jutamente pois
# a variavel resultado é uma lista com as palavras captadas do padrão escolhido por você.


# P.S: se for usar algo da lista abaixo utiliza o r"string" senão nao funciona ok

# \b = identifica a beirada de uma palavra

# \d = identifica todo o númerico [0-9]

# \s = identifica os [\t \n \r \f \v]

# \w = identifica todo o alfanumérico [a-zA-Z0-9_] significa literalmente alfabeto, numeros e underline
# p.s \w = w{3} singifica palavra com 3 letras como "cat" "the" "123"

# \s = identifica espaços em brando [espaço, tabulação, quebra de linha]

# extra: + significa encontrar mais de uma ocorrencia do padrão descrito
# p.s + = utilizando isso ele vai buscar as beiradas da "palavra e aplicar o padrão nela"
# p.s + = se vc usar numa sequencia de numeros: normal [0,1,2,3,4,5,6,7,8,9], com o + [012,345,6789] na ordem que aparecer mesmo

# extra: . significa encontrar tudo tirando a quebra de linha