# primeiro de tudo, importar a ferramenta que atua com a linguagem SQL, o "sqlite3"
import sqlite3

# depois, podemos importar também o gerenciador de DataFrames, "pandas"
import pandas as pd

#|==============================================================================================================|

# Conectar no Banco de dados "cap12_dsa.db"
con = sqlite3.connect("C:\LUCCA\PythonDSA\Vscode\DSA ARCHIVES\Cap12 Linguagem SQL\cap12_dsa.db")

# abrir um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# Fazer um Query SQL para extrair os nomes das colunas no banco de dados
# P.S: é praticamente uma variável com o comando que vai ser executado dentro da linguagem SQL
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Agora nós executamos a Query para realmente realizar a ação descrita no "sql_query"
cursor.execute(sql_query)

# Agora visualizamos o resultado 
print(cursor.fetchall())

# isso aí é so pra saber qual o nome da tabela dentro do arquivo SQL

#|==============================================================================================================|

# Criar uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

# Executa a instrução
cursor.execute(query1)

# Cria a variável "dados"
dados = cursor.fetchall()

#Visualiza os dados
dados

#|==============================================================================================================|

# retorna somente os nomes das colunas
cursor.description

# Cria a lista "nomes_colunas"
nomes_colunas = [description[0] for description in cursor.description]

# Visualiza o resultado
print(nomes_colunas)

#|==============================================================================================================|

# Criar instrução SQL
# P.S: Essa intrução calcula a média (AVG = average) de unidades vendidas em todas as linhas
query2 = "SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa"

# Executa a query
cursor.execute(query2)

# Visualiza o resultado
cursor.fetchall()

#|==============================================================================================================|

# Criar instrução SQL
# P.S: Essa instrução seleciona a coluna "Nome_Produto", calcula a média da coluna "Unidades_Vendidas" 
# e agrupa por "Nome_Produto"
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

# Executa a query
cursor.execute(query3)

# Visualiza o resultado
cursor.fetchall()

#|==============================================================================================================|

# Criar instrução SQL
# P.S: Essa instrução seleciona a coluna "Nome_Produto", Calcula a media da coluna "Unidades_Vendidas" 
# Somente para as linhas que tiverem a Coluna "Valor_Unitario" Maior (>) que 199
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""

# Executa a query
cursor.execute(query4)

# Visualiza o resultado
cursor.fetchall()