# codigo criado para informar algo sobre a linguagem python caso voce tenha esquecido

######################################################################################
# OPERAÇÕES RELACIONAIS
# retorna um valor booleano (True/False)
# P.S = (> MAIOR QUE), (< MENOR QUE), (>= MAIOR OU IGUAL A), (<= MENOR OU IGUAL A), (== IGUALDADE)
6 > 3
# true

3 > 7
# false

4 <= 4
# true

5 == 5
# true

######################################################################################

######################################################################################
# CONDICIONAL IF
# ela executa uma ação se o resultado dela for true
if 5 > 2:
    print("A sentença é verdadeira!")

# CONDICIONAL ELSE
# ela executa uma ação caso o if não seja executado
if 5 < 2:
    print("A sentença é verdadeira!")
else:
    print("A sentença é falsa!")

# CONDICIONAL ELIF
# ela adiciona mais uma condição de True
dia = ()
if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")
######################################################################################

######################################################################################
# CONDICIONAIS ANINHADOS
# (and SO RETORNA TRUE SE TUDO FOR TRUE) (or RETORNA TRUE CASO UMA DAS DECLARACOES FOR TRUE) (not INVERTE TRUE/FALSE)
# OPERADOR AND
# ela so executa a ação caso a funcao retorne true nas duas declaracoes
nome  = "Bob"
idade = 18
if idade > 17 and nome == "Bob":
    print("Autorizado!")

# OPERADOR OR
# ela executa a ação caso uma das declaracoes retornar true
numero = 4

if (numero > 5) or (numero % 2 == 0):
    print("Isso está sendo impresso porque uma duas condições é verdadeira!")

# OPERADOR NOT
# ela inverte os sinais de true e false
numero = 4

if not(numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")
######################################################################################

######################################################################################
# PLACEHOLDERS
# sao caracteres identificados por % que podem ser utilizados como seguradores de lugar
# é so voce identificar ele no final da linha que no final ele ira ser subistituido pelo que voce quiser
disciplina = 'Data Science'
nota_final = 90
semestre = 2

if disciplina == 'Data Science' and nota_final >= 80 and semestre != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')
######################################################################################

######################################################################################
# LOOP FOR
# é uma funcao que normalmente se utiliza para ler varios numeros numa lista pre ou nao estabelecida
tp = (2,3,4)
for i in tp:
    print(i)

# Imprimindo os números pares da lista de números
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print (num)

# Listando os números no intervalo entre 0 e 101, contando de 2 em 2
for i in range(0,101,2):  
    print(i)

# listando os caracteres de uma frase
for caracter in 'Python é uma linguagem de programação divertida!':
    print (caracter)

# Some os números pares da primeira lista com os números pares da segunda lista
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

for lista in [lista1, lista2]:
    for num in lista:
        if num % 2 == 0:
            soma += num

print("O soma dos números pares das duas listas é igual a", soma)

# Some os números pares da primeira lista com os números pares da segunda lista
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num

print("Soma dos valores pares:", soma)

# Loop em lista de listas (matrizes) para encontrar o maior número
matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior_numero = 0

for linha in matriz:
    for num in linha:
        if num > maior_numero:
            maior_numero = num

print("Maior número:", maior_numero)

# Listando as chaves de um dicionário
dict = {'k1':'Python','k2':'R','k3':'Scala'}
for item in dict:
    print(item)

# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k,v in dict.items():
    print (k,v)
######################################################################################

# exemplo do TRY e EXCEPT
try:
    8 + 's'
except TypeError:
    print("Operação não permitida")

# da pra usar o else no final pra caso o except não seja aplicado
try:
    f = open('arquivos/testandoerros','r')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()

# e por fim temos o FINALLY que funciona como algo que sempre executa independente da condição que foi colocado
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print ("Comandos no bloco finally são sempre executados!")

# P.S: Mesmo que o EXCEPT IOError seja aplicado, o esle vai ser ignorado mas o finally vai ser executado de qualquer maneira