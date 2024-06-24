# |====================================================================================================================|

# INTRODUÇÃO A BIBLIOTECA

# instruções de como se utilizar a biblioteca Matplotlib, sendo mais utilizada na criação
# de gráficos para analise de dados e visualização de dataframes

# o primeiro de tudo é importar a biblioteca para o seu arquivo
# P.S = normalmente utilizamos o nome mpl por que é mais facil de chamar quando for executar comandos

import matplotlib as mpl

# a segunda coisa é adicionar outra biblioteca que personaliza os gráficos gerados pelo mpl, ela se chama
# pyplot, então é so importar ela junto, lembrando que ela faz parte do mpl, então fica asssim:

import matplotlib.pyplot as plt

# Se estiver usando um JUPYTER NOTEBOOK:
# Uma opção interessante é fazer o mpl gerar os graficos na mesma pagina e não ficar abrindo outras
# janelas com o seguinte comando:

'''
%matplotlib inline
'''

# |====================================================================================================================|

# UTILIZANDO PYPLOT

# SEUS PRIMEIROS GRÁFICOS:
# A partir daqui entramos na sessão de explicação de cada tipo de gráfico com informações adicionais sobre cada um

# Plot padrão:
# esse tipo de gráfico só faz a associação de duas variáveis, então tudo que precisa é utilizar o plt.plot("Dados")
# que o gráfico está feito, segue o exemplo abaixo

plt.plot([1,3,5], [2,4,7])
plt.show() # P.S = Sempre lembrar de usar o .show() no final pra mostrar o gráfico ok

# para utilizar mais de uma linha no gráfico, basta colocar mais linhas .plot, pois cada comando server pra uma linha diferente

plt.plot([1,3,5], [2,4,7])
plt.plot([3,4,5], [4,6,7])
plt.show()

# argumentos do Plot padrão:

# label= "Str" = definição de legendas no gráifco, lembrar de usar o .legend() para aplicar elas no gráfico

plt.plot([1, 2, 3],[4, 5, 6], label= "Gráfico com Matplotlib")

# color= "Str" = definição da cor da variavel no gráfico, lembrar do nome das cores ou do atalho de uma letra da cor escolhida

# b : blue, g : green, r : red, c : cyan, m : magenta, y : yellow, k : black, w : white

plt.plot([1, 2, 3],[4, 5, 6], color= "blue")


# métodos dos Plots:

# plt.xlabel("Str") = definição do nome do eixo X com o "Str" que estiver como argumento

plt.xlabel("Variável 1")


# plt.ylabel("Str") = definição do nome do eixo X com o "Str" que estiver como argumento

plt.ylabel("Variavel 2")


# plt.title("Str") = definição do título do gráfico com o "Str" que estiver como argumento

plt.title("Teste Plot")


# plt.legend() = aplicação da legenda no gráfico gerado com o argumento label="Str" dentro do .plot() 

plt.legend()

# |====================================================|

# Gráfico de barras

x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]

plt.bar(x1, y1, label = 'Listas1', color = 'blue')
plt.show()

# |====================================================|

# Gráfico histograma

idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(idades, bins, histtype = 'bar', rwidth = 0.9)
plt.show()

# Argumentos dos histogramas

# histtype = "Str" = ‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’

plt.hist(idades, bins, histtype= 'barstacked')
plt.show()

# rwidth = int = largura das barras do gráfico.

# |====================================================|

# Gráfico de dispersão

x2 = [1,2,3,4,5,6,7,8]
y2 = [5,2,4,5,6,8,4,8]

plt.scatter(x2, y2, label = 'Pontos', color = 'r', marker = 'o')

# argumentos dos gráficos de dispersão

# marker= "Str" = "o", "*"

plt.scatter(x2, y2, marker="o")
plt.show()

# |====================================================|

# Gráfico de Área empilhada

dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m','c','r','k','b'])
plt.show()

# |====================================================|

# Gráfica de pizza

fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0,0.2,0,0))
plt.show()

# argumentos do gráfico de pizza

# startangle = int = 0 to 360 = define o angulo de começo das categorias

plt.pie(fatias, labels = atividades, colors = cores, startangle = 90)
plt.show()

# shadow = bool = True or False = define se o gráfico vai ter sombra ou não

plt.pie(fatias, labels= atividades, shadow= True)
plt.show()

# explode = (tuple int) = define a separação para fora de alguma categoria específica, em ordem de aparição na lista

plt.pie(fatia, labels= atividades, explode= (0,0.2,0,0))
plt.show()

# |====================================================================================================================|

# UTILIZANDO O PYLAB

# lembrar de importar a biblioteca "pylab"

from pylab import *

# Gráficos de Linha:

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Define a escala dos eixos
axes = fig.add_axes([1, 0, 0.8, 0.8])

# Cria o plot
axes.plot(x, y, 'r')

# Labels e título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')

# Gráficos de linha com 2 figuras

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Cria os eixos
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # eixos da figura principal
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # eixos da figura secundária

# Figura principal
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura secundária
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária')