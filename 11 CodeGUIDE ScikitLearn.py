# introdução ao capítulo da biblioteca de scikit-learn (machine learning)
# imports desse CodeGUIDE

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# carregamento do dataset:
df_dsa = pd.read_csv("C:\LUCCA\Codigos VSCode\Vscode\DSA ARCHIVES\Cap15 Machine learning com scikit-learn\dataset.csv")

# primeira visualização do dataset:
df_dsa.head()

# resumo das informações do dataset:
df_dsa.info()

# Definição do Problema de negócio:

# Usando dados históricos é possível prever o salário de alguém 
# com base no tempo dedicado aos estudos em horas por mês?

# treinar bot de previsão de salario com base em tempo de estudo (h)

# correlação:
df_dsa.corr()

# resumo estatístico do dataset:
df_dsa.describe()

# histograma da variavel preditora
sns.histplot(data = df_dsa, x='horas_estudo_mes', kde=True)

# separação dos dados:
X = np.array(df_dsa["horas_estudo_mes"])

# ajustando shape de X
X = X.reshape(-1,1)

# preparando variável alvo:
y = df_dsa['salario']
plt.scatter(X,y, color='blue', label="Dados reais historicos")
plt.xlabel("Horas de estudo")
plt.ylabel("Salario")
plt.legend()
plt.show()

# dvidir dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X,y, test_size = 0.2, random_state = 42)
X_treino.shape
X_teste.shape
y_treino.shape
y_teste.shape

# criação do modelo de regressão linear simples
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
plt.scatter(X,y,color='blue', label="Dados Reais históricos")
plt.plot(X, modelo.predict(X), color='red', label="Reta de regressão com as previsões do Modelo")
plt.xlabel("Horas de estudo")
plt.ylabel("Salario")
plt.legend()
plt.show()

# avaliação do modelo nos dados de teste
score = modelo.score(X_teste, y_teste)
print(f"Coeficiente R^2: {score:.2f}")

# intercepto - parâmetro w0
modelo.intercept_

# Slope - parâmetro w1
modelo.coef_

# Definir um valor para horas de estudo
horas_estudo_novo = np.array([[48]])

# prvisão com modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de {horas_estudo_novo} horas por mês, seu sslário pode ser igual a {salario_previsto}")

# Mesmo resultado anterior usando os parâmetros (coeficientes) aprendidos pelo modelo
# y_novo = w0 + w1 * X
salario = modelo.intercept_ + (modelo.coef_ * horas_estudo_novo)
print(salario)

# Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[65]]) 

# Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)
# Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[73]]) 

# Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)