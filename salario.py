class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo


class CalculadoraSalario:
    def calcular_salario(self, funcionario: Funcionario):
        if funcionario.cargo == "DESENVOLVEDOR":
            if funcionario.salario_base >= 3000:
                return funcionario.salario_base * 0.8
            else:
                return funcionario.salario_base * 0.9
        elif funcionario.cargo == "DBA" or funcionario.cargo == "TESTADOR":
            if funcionario.salario_base >= 2000:
                return funcionario.salario_base * 0.75
            else:
                return funcionario.salario_base * 0.85
        elif funcionario.cargo == "GERENTE":
            if funcionario.salario_base >= 5000:
                return funcionario.salario_base * 0.7
            else:
                return funcionario.salario_base * 0.8
        else:
            raise ValueError("Cargo inválido")
