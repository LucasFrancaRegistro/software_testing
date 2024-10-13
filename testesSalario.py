import unittest
import pandas

from salario import Funcionario, CalculadoraSalario

class TestCalculadoraSalario(unittest.TestCase):
    def test_salario_desenvolvedor_acima_3000(self):
        funcionario = Funcionario("João", "joao@example.com", 4000.0, "DESENVOLVEDOR")
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario(funcionario)
        self.assertEqual(salario_liquido, 4000.0 * 0.8)
    
    def test_salario_desenvolvedor_abaixo_3000(self):
        funcionario = Funcionario("Ana", "ana@example.com", 2500.0, "DESENVOLVEDOR")
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario(funcionario)
        self.assertEqual(salario_liquido, 2500.0 * 0.9)
    
    def test_salario_dba_acima_2000(self):
        funcionario = Funcionario("Carlos", "carlos@example.com", 2500.0, "DBA")
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario(funcionario)
        self.assertEqual(salario_liquido, 2500.0 * 0.75)
    
    def test_salario_dba_abaixo_2000(self):
        funcionario = Funcionario("Bia", "bia@example.com", 1500.0, "DBA")
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario(funcionario)
        self.assertEqual(salario_liquido, 1500.0 * 0.85)
    
    def test_salario_gerente_acima_5000(self):
        funcionario = Funcionario("Lucas", "lucas@example.com", 6000.0, "GERENTE")
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario(funcionario)
        self.assertEqual(salario_liquido, 6000.0 * 0.7)
    
    def test_salario_gerente_abaixo_5000(self):
        funcionario = Funcionario("Maria", "maria@example.com", 4000.0, "GERENTE")
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario(funcionario)
        self.assertEqual(salario_liquido, 4000.0 * 0.8)

if __name__ == '__main__':
    unittest.main()
