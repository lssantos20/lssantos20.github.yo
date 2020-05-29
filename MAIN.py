#arquivo principal do programa

from calculadora import Calculadora

#do arquivo calculadora importado da classe calculadora


numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))

myCalc = Calculadora(numero1,numero2) # na variavel myCalc  cria um novo objeto do tipo calculadora
#passando numero 1 e numero 2 como parametros

op = input("digite a opção matematica desejada: (+ - * / ):")