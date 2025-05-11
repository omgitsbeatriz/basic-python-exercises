class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# 1. Criar e usar objetos
p1 = Pessoa("Beatriz", 22)
p1.apresentar()

# 2. Classe com método para aumentar salário
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

    def mostrar_salario(self):
        print(f"{self.nome} ganha R$ {self.salario:.2f}")

f1 = Funcionario("Carlos", 2000)
f1.aumentar_salario(10)
f1.mostrar_salario()