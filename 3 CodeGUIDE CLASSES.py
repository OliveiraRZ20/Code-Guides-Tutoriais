# funções para a nova descoberta

# CLASSES

# tentando explicar de maneira curta e grossa da pra entender as classes do python como
# um metodo de criação de funções de . como aqueles que vc ja usou antes, ex: .capitalize,
# .upper, .lower so que dessa vez você vai criar esses métodos

# então para criar uma classe voce vai ter esse esqueleto pra começar

class teste:
    def __init__(self, x1, x2, x3):
        self.ex1 = x1
        self.ex2 = x2
        self.ex3 = x3

# Então agora vc deve estabelecer esses parametros iniciais que estão em laranja (x1,x2,x3)

exemplo = teste(1,2,3)

# agora então voce pode chamar o método que ele irá responder diretamente com o comando

exemplo.ex1
# SAÍDA: 1

# agora eu vou mostrar um exemplo mais aplicado para melhor entendimento
# P.S: FUNÇÃO DENTRO DE CLASSE É CHAMADA DE METODO

class Funcionarios:
    
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print("Funcionário(a) " + self.nome + " tem salário de R$" + str(self.salario) + " e o cargo é " + self.cargo)

# depois de criar a classe vc aplica isso tudo a um objeto

Func1 = Funcionarios("Lucca",20000, "Cientista de dados")

# agora sim voce pode chamar os metodos e funções internas dessa classe

Func1.listFunc()
# SAÍDA: Funcionário(a) Lucca tem salário de R$20000 e o cargo é Cientista de Dados

# agora abaixo deixarei alguns comandos que permitem mexer nos dados empregados a um objeto

# tem o atributo?? [TRUE/FALSE]
hasattr(Func1, "salario") 

# setar o atributo para x
setattr(Func1, "salario", 4500)

# pegar valor do atributo x [devolve o valor que representa aquele atributo]
getattr(Func1, "salario")

# deletar atributo
delattr(Func1, "salario")

# Herança de classes

# ela funciona basicamente na definicao de herança mesmo
# se voce cria uma classe filha com base na classe MÃE, essa classe filha vai ter todos os atributos da mãe
# então quando voce tem que criar algo com varios objetos, fique ligado pra poder economizar digitação
# se algo vai ser feito diversas vezes em objetos diferentes, coloque isso na superclasse

# EX: primeiramente criamos a classe ANIMAl que tem ai alguns atributos

class Animal:
    
    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")
        
    def emitir_som(self):
        pass

# depois criamos a classe cachorro que tem todos os atributos da classe animal pois foi baseada na mesma
# como pode ser visto na nomeclatura da criação da classe Cachorro(Animal)

class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au au!")

# agora eu faço a mesma coisa só que com a classe Gato(Animal)
# no fim das contas a unica diferença entre essas classes são as coisas específicas delas que nesse caso é
# o metodo de emitir_som é diferente para cada animal, logo é preciso criar uma definição do som para cada tipo
# de animal, fazendo assim necessário e mais eficiente fazer um metodo de emitr_som para cada sub_classe
# em contrapartida, o metodo de hora de comer é igual para todos os animais, logo é mais inteligente escrever
# o metodo de comer na super_classe do que ficar repetindo esse codigo em todas as sub_classes
# tamo junto, gg...

class Gato(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")
    
    def emitir_som(self):
        print("Miau!")

# agora abaixo vou deixar alguns codigos de classes que eu desenvolvi

class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.soma = num1 + num2
        self.subtracao = num1 - num2
        self.multiplicacao = num1 * num2
        self.divisao = num1 / num2
        
    def faztudo(self):
        print(f"Realizando todos os calculos com os dois numeros temos os seguintes resultados\nSoma = {self.num1} + {self.num2} = {self.soma}\nSubtracao = {self.num1} - {self.num2} = {self.subtracao}\nMultiplicacao = {self.num1} x {self.num2} = {self.multiplicacao}\nDivisao = {self.num1} / {self.num2} = {self.divisao}")

x1 = int(input("Primeiro número: "))
x2 = int(input("Segundo número: "))

numeros = Math(x1, x2)
numeros.faztudo()



class Circulo():
    pi = 3.14
    
    def __init__(self, raio = 5):
        self.raio = raio
        
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    
    def setraio(self, novo_raio):
        self.raio = novo_raio
        
    def GetRaio(self):
        return self.raio