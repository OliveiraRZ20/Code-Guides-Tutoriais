# imports utilizados na produção desse CodeGUIDE
import pandas as pd # gerenciamento de tabelas
import matplotlib.pyplot as plt # gráficos
import seaborn as sns # gráficos
import statsmodels.api as sm # modelos estatísticos

# carregando dataset
path = "C:\LUCCA\Codigos VSCode\Vscode\DSA ARCHIVES\Cap14 analise estatistica com statsmodels\dataset.csv"
df_dsa = pd.read_csv(path)

# P.S: TUDO COMEÇA COM O PROBLEMA DE NEGÓCIO.
# tudo que eu fizer a partir de agora, 
# vai ser em função do problema de negócio.

# Problema em questão:
# Existe alguma relação entre a área de imóveis (em m^2) 
# e o valor do aluguel em uma determinada cidade?
# Caso exista relação, como podemos mensurá-la?

# Resumo:
# Analisar alguma relação entre área do imóvel e o aluguel dela.

# Olhando pela primeira vez o dataset:
df_dsa.head()

# Gerando informações cruciais do dataset:
df_dsa.info()

# ANÁLISE EXPLORATÓRIA - Resumo estatístico

# valores ausentes
df_dsa.isnull().sum()

# Gerando resumo estatístico do dataset:
df_dsa.describe()

# depois de analisar que temos alguns valores que não precisam de cálculos estatísticos,
# então devemos fazer ter no=ção do tipo de variável antes de analisar as tabelas.

# gerando resumo estatístico da variável alvo com base no problema de negócio.
df_dsa["valor_aluguel"].describe()

# histograma da varíavel alvo
sns.histplot(data = df_dsa, x="valor_aluguel", kde=True)

# Correlação entre variáveis
df_dsa.corr()

# histograma entre a variável de entrada e a variavel explicativa
sns.scatterplot(data = df_dsa, x="area_m2", y="valor_aluguel")

# Criando o modelo

# definir variavel dependente (Variavel de saida)
y = df_dsa["valor_aluguel"]

# definir variavel indepentende (Variável de entrada)
X = df_dsa["area_m2"]

# adição de constante a variavel independente (REQUERIDO PELO STATSMODELS)
X = sm.add_constant(X)

# Criacao do modelo
modelo = sm.OLS(y,X)

# Treinamento do modelo
resultado = modelo.fit()

print(resultado.summary())

df_dsa.head()

# plot
plt.figure(figsize= (12,8))
plt.xlabel("area_m2", size=16)
plt.ylabel("valor_aluguel", size = 16)
plt.plot(X["area_m2"], y, "o", label= "Dados Reais")
plt.plot(X["area_m2"], resultado.fittedvalues, "r-", label="Linha de Regressão (Previsoes do Modelo)")
plt.legend(loc="best")
plt.show()