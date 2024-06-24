# instrução feita de forma mais linear com um arquivo .py pq achei melhor mesmo

# algo muito comum é utilizar o pandas como pd então utilizar o comando abaixo

import pandas as pd

# primeiro passo para se ter algo no pandas é utilizar um dicionário onde se segue a seguinte identação

# {COLUNA : [dados], COLUNA02 : [dados]}

# então aí teremos uma introdução a utilização do pandas com o seguinte exemplo

dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

# próximo passo é chamar uma função muito importante que é o DataFrame, que permite que os dicionairio que vc criou
# virem realmente tabelas estilo o que nós vimos no excel

from pandas import DataFrame

# então a partir daí a gente precisa primeiramente definir uma variavel como um DataFrame

df = DataFrame(dados)

# nesse caso acima nós não utilizamos nenhuma ferramenta para ordenar as colunas do nosso DataFrame
# então utilizaremos o seguinte:

df = DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Ano'])

# isso aí ajuda para ordenar do jeito que quiser as colunas da tabela quando for imprimir na tela

# para nomear o INDEX da tabela e deixar de ser (0,1,2,3,4,5...) podemos usar o método [index=]
# então ficaria asssim:

df = DataFrame(dados, 
                columns = ['Estado', 'Taxa Desemprego', 'Ano'], 
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

# para mostrar o DataFrame na tela baste chamar pelo nome dele e executar
# ficaria assim:

df

# para importar um DataFrame de outro lugar é necessário utilizar o comando para o tipo de arquivo certo

# para arquivos CSV:

df_csv = pd.read_csv("C:\LUCCA\PythonDSA\Vscode\DSA ARCHIVES\Cap10CodeGUIDE07\dataset.csv")

# para arquivos xlsx:

df_excel = pd.read_excel("C:\\LUCCA\\1-lucca\\Top Musicas Piano.xlsx")

# |====================================================================================================================|

# Métodos básicos dos dataframes:

# Método .values

# ele vai retornar todos os valores de todas as colunas de uma linha em forma de lista python
# isso tudo para todas as linhas

df.values

# |====================================================|

# Método .dtypes

# ele vai retorna o tipo de dado em cada coluna em forma de lista 
# então se vc chamar o item x ele retorna o tipo dele

df.dtypes

# |====================================================|

# Método .columns

# ele vai retornar uma lista python com o nome de todas as colunas do seu DataFrame
# então se vc chamar o item x ele retorna o nome da coluna x

df.columns

# |====================================================|

# Método .index

# ele vai retornar uma lista python com o nome da indexação de linhas, ou seja, se vc não mudar ele vai
# retornar uma lista com o número das linhas

df.index

# |====================================================|

# Método .shape

# ele vai retornar uma lista python com dois valores, o número de linhas e o número de colunas, NESSA ORDEM

df.shape

# |====================================================================================================================|

# |====================================================================================================================|

# Métodos de impressão do DataFrame

# Filtragem de visualização rapida

# para fazer uma espécie de filtragem de visualização rapida basta chamar somente as colunas que quer ver quando
# chamar o DataFrame

df['Estado']

# é possivel fazer isso para varias colunas ao mesmo tempo
# P.S = lembre-se que quando fizer isso é como se vc estivesse passando a lista de colunas escolhidas
#       então usa como uma lista de colunas passadas pra ele

df[ ['Taxa Desemprego', 'Ano'] ]

# É SEMPRE BOM LEMBRAR QUE ASSIM COMO O PYTHON SE IMPORTA COM MAIUSCULO E MINUSCULO, O PANDAS TBM TA, 
# então escreve direito seu animal

# também é possivel utilizar argumentos de número de linha para visualização
# lembrando que o segundo valor é absoluto, então coloca um a mais no final
# P.S = EXCESSÃO PARA O CASO EM QUE AS LINHAS TEM NOME DE STRING, ai sim nenhum dos dois é exclusivo

df[0:3] # retorna as linhas 0,1 e 2

df['estado2' : 'estado4'] # retorna as linhas estado2, estado3, estado4

# |====================================================|

# Operadores Lógicos Para manipulação de dados

# sinal de igualdade | == |: normalmente feita entre uma coluna e algum valor especifico que é procurado
# P.S = quando for mencionar a coluna escolhida sempre utilize o .ColunaX para este tipo de filtragem

df_csv[df_csv.Segmento == 'Home Office'].head() # condição de retornar somente linhas com coluna Segmento = Home Office


# sinal de E (AND) | & |: utilizado para definir a condição AND do python, mostrar a condição X e(AND) a Y
# P.S = as condições aplicadas com AND ficam entrelaças, então as duas condicoes precisam ser verdadeiras pra ela passar

df_csv[ (df_csv.Segmento == 'Home Office') & (df_csv.Regiao == 'South')].head() # condição a mais de Regiao = South


# Sinal de OU (OR) | | |: utilizado para definir a condição de OR do python, mostrar a condição X ou a Y
# P.S = as condições podem se tratar de colunas diferentes então as duas condicoes podem ser verdadeiras

df_csv[(df_csv.Segmento == 'Home Office') | (df_csv.Regiao == 'South')].head()

# |====================================================|

# Função .sample(x) = imprimir na tela o número X de linhas selecionadas aleatoriamente

df.sample(5) # imprimir 5 linhas escolhidas aleatoriamente cada vez que o comando é executado

# |====================================================|

# Função .head() = imprimir na tela as primeiras 5 (CINCO) linhas do Dataframe escoliho

df.head()

# |====================================================|

# Função .tail() = imprimir na tela as ultimas 5 (CINCO) linhas do DataFrame escolhido

df.tail()

# Para os dois também é possivel utilizar a um número como argumento em que o número que vc colocar
# será exclusivo para o numero de colunas (ent lembra de colocar um numero a mais do que vc quer)

df.head(5)
df.tail(5)

# se vc quiser tambem é possivel utilizar números negativos, so que é como se vc tirasse da visualização
# o número de linhas que vc colocar no argumento (head = tirar de baixo / tail = tirar de cima)

df.head(-3)
df.tail(-3)

# |====================================================|

# Método .filter(items = ['linhaX'], axis = 0)

# ele retorna somente uma linha, a (linhaX) com os valores de todas as colunas

df.filter(items= [0], axis = 0)


# |====================================================================================================================|

# |====================================================================================================================|

# Métodos para manipular DataFrames

# Método .isna()

# ele vai retornar o DataFrame inteiro só que ao invés de ter os valores normais, terão valores booleanos
# dizendo se ali tem um valor ausente ou não, (Valores ausentes são buracos no DataFrame, onde não tem valor nenhum)

df.isna()

# também é possivel checar somente em uma coluna específica

df['Ano'].isna()

# mas o melhor possível é utilizar o .sum() para gerar um relatório de quantos valores ausentes tem em cada
# coluna do seu DataFrame, então se tiver problema com isso, usa o seguinte comando

df.isna().sum()

# |====================================================|

# Método .describe()

# ele retorna o seu DataFrame mas sem os valores usuais, ele realiza algumas operações com o seu DataFrame
# para demosntrar alguns outros dados tratados como, contagem de valores, média, desvio padrão, máximo, mínimo...

df.describe()

# |====================================================|

# Método de filtragem por condição

# ele retorna o seu DataFrame filtrado para somente linhas que atendam a sua condição descrita no argumento
# sempre lembrar de utilizar o nome da coluna com a origem dela junto (coluna Ano = df['Ano"])

df[ df['Taxa Desemprego'] < 2] # assim ele retorna somente as linhas que tem a taxa desemprego menor que 2

# |====================================================|

# Método .value_counts()

# ele retorna uma lista python com a quantidade de vezes que cada valor encontrado na lista aparece
# então um jeito legal de encontrar a moda de uma coluna com valores numéricos é o seguinte

df_csv['Quantidade'].value_counts().index[0] # isso retorna automaticamente o primeiro valor, logo, a moda.

# outro uso maneiro pra isso é pra colunas de string, ele lista os valores encontrados e conta quantas vezes eles foram encontrados
# P.S = pode se utilizar os dois métodos de se mencionar uma coluna específica

df_csv.Segmento.value_counts()

# |====================================================|

# Método .fillna(value = valorX, inplace = |True ou False|)

# ele vai realizar a operação de preencher todos os valores da coluna selecionada ou do DataFrame inteiro
# com o (valorX). P.S = o inplace ali no final significa que as alterações feitas no DataFrame serão alteradas
# na varíavel dele diretamente, senão o pandas cria uma cópia de visualização do resultado final, ent quase
# sempre vai ser True aquele valor

df_csv['Quantidade'].fillna(value = 'bobão', inplace = True)

# |====================================================|

# Método .query('Condição criada pelo usuário')

# ele vai gerar um novo DataFrame apenas com as linhas que atenderem a condição especificada no argumento

df_maioral = df_csv.query('229 < Valor_Venda < 10000') # assim temos um DataFrame com os valores acima de 229 e abaixo de 10000

# se soubermos atraves do comando df_maioral.describe() que a média dos valores é 766, podemos fazer um outro DataFrame

df_acima_media = df_maioral.query('Valor_Venda > 766') # assim teremos um DataFrame somente com valores acima da média (766)

# |====================================================|

# Método .isin([X,Y,Z,...])

# é um metodo de filtração do DataFrame para aplicar regras sobre valores e retornar somente os valores
# escolhidos pelo usuário

df_csv[df_csv['Quantidade'].isin([5,7,9,11])] # ele retorna somente linhas que contem 'Quantidade' igual a [5,7,9,11]

# para um efeito melhor é possivel encaixar um .shape pra ajudar a saber exatamente o numero de linhas que
# atendem o requisito

df_csv[df_csv['Quantidade'].isin([5,7,9,11])].shape

# |====================================================|

# Método .mean()

# ele retorna a média realizada com os valores de todas as linhas de cada coluna numérica do seu DataFrame

df_csv.mean()

# |====================================================|

# Método .groupby(['ColunaX', 'ColunaY'])

# ele é um metodo de filtração do DataFrame por agrupamento, normalmente utilizado com outros métodos como o .mean [Média]
# P.S = sempre lembrar de de mencionar todas as colunas necessárias para a filtração antes do comando, segue exemplo:

# esse filtro abaixo gera a média de valor_venda de acordo com a todas as regiões de cada segmento da empresa

df_csv[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()

# na agregação múltipla é possivel utilizar o método .agg(['mean', 'std', 'count']) [Média, Desvio padrão, contagem de valores]
# ele serve para adicionar métodos de visualização como a média, desvio padrao e contagem de valores

df_csv[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count'])

# |====================================================|

# Método .startswith('String')

# ele é um metodo de filtração por string, então ele filtra colunas de dado Str verificando se o dado da linha começa com os caracteres
# descritos no argumento. P.S = utilizar o .ColunaX para mencionar as colunas no comando e o .str pra editar Strings

df_csv[df_csv.Segmento.str.startswith('Con')].head() # filtro aplicado para linhas com a coluna Segmento começando com as letras Con

# |====================================================|

# Método .endswith('String')

# mesma coisa do .startswith() mas checando o final da string ao invés do começo, então basta colocar os ultimos caracteres da palavra_chave
# procurada que servirá igualmente

df_csv[df_csv.segmento.str.endswith('mer')].head() # filtro aplicado para linhas com a coluna Segmento terminando com as letras mer

# |====================================================|

# Método .split('Char')

# ele retorna uma coluna específica só que separada por algum caracter em comum em formato de lista python
# a ideia exemplo é criar uma Coluna 'Ano', utilizando a Coluna 'ID_Pedido' pois ele contém o ano só que embaralhado com o local e o ID
# então realizamos um split pelo caracter ('-') e selecionamos o item de índice 1 para coletar o ano

df_csv.ID_Pedido.str.split('-') # isso retorna uma lista python de 3 valores pra cada linha da coluna 

df_csv.ID_Pedido.str.split('-').str[1].head() # isso retorna somente o item de indice 1 da lista, ou seja, o ano da venda

df_csv['Ano'] = df_csv.ID_Pedido.str.split('-').str[1] # isso cria uma coluna chamada 'Ano' com a filtração para o ano retirado da coluna ID_Pedido


# Método .lstrip() ou .rstrip()

# Método utilizado para realmente retirar informações de DataFrames que não sejam mais uteis a partir do lado esquerdo ou direito das linhas em 
# strings em colunas especificas como o caso que iremos usar de exemplo, pois como ja criamos a coluna ano, podemos deixar a data do pedido
# com o ano em somente 2 caracteres, então precisamos remover essa informação da coluna Data_Pedido

df_csv['Data_Pedido'].str.lstrip('20', inplace = True) # isso procura na coluna Data_Pedido a partir do lado esquerdo o valor 20 e retira ele

# |====================================================|

# Método .replace('Antes', 'Depois')

# ele retorna um DataFrame de visualização com a alteração feita com base na nomeclatura acima, então sempre lembrar de fazer uma substituição
# das colunas como descrito no comando abaixo

df_csv['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX') # isso substitui a coluna ID_Cliente antiga pela nova com a substituicao feita

# |====================================================|

# Método .cat(Local da informação, sep = 'Char')

# método utilizado para criar uma nova coluna a base da concatenação de informações de diferentes colunas como segue o exemplo abaixo
# em que serão utilizadas as colunas ID_Pedido e Segmento para criar Pedido_Segmento

df_csv['Pedido_Segmento'] = df_csv['ID_Pedido'].str.cat(df_csv['Segmento'], sep = '-') # sep é de separador, o que vai ter entre as duas informações


# |====================================================================================================================|