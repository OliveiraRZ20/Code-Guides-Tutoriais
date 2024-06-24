# |====================================================================================================================|

# CodeGUIDE de Seaborn

# documentação: https://seaborn.pydata.org/

import seaborn as sea

# imports que normamlmente vem junto nos projetos com seaborn

import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# criando gráficos com Seaborn

# carregando dados do seaborn

dados = sea.load_dataset("tips")
dados.head()

# função .jointplot(data = *obj*, x= *str*, y= *str*, kind = 'reg')

sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')

# função .implot(data = *obj*, x= *str*, y= *str*, col= *str*)

sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")

# função .lmplot(data = *obj*, x = *str*, y = *str*, fit_reg = bool)
# P.S = gráfico de dispersão baseado em duas variaveis com linha de regressão e intervalo de confiança

df = pd.DataFrame()
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)
df.head()

sea.lmplot(data = df, x = "idade", y = "peso")

# função .kdeplot(*DataFrame*)
# P.S: gráfico de linha baseado na coluna *str* e na densidade dos dados

sea.kdeplot(df.idade)

sea.kdeplot(df.peso)

# função .distplot(*DataFrame*)
# P.S: .kdeplot mas com um histograma atrás

sea.distplot(df.peso)

# função .rugplot(*DataFrame*)
# P.S: adicionar rugas no gráfico criado inicialmente (ex: histograma com rugas de valores exatos)

plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade)

# função .boxplot(*DataFrame*, color= *str*)
# P.S: Gráfico de Caixa

sea.boxplot(df.idade, color = 'm')

# Agregação completa 

np.random.seed(42)
n = 1000
pct_smokers = 0.2

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})

# Style
sea.set(style = "ticks")

# lmplot
sea.lmplot(x = 'altura', 
           y = 'peso', 
           data = dados, 
           hue = 'flag_fumante', 
           palette = ['tab:blue', 'tab:orange'], 
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes')

# Remove as bordas
sea.despine()

# Show
plt.show()