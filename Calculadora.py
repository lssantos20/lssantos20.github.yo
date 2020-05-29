class Calculadora: #define o nome da class
    #_init_() é o metodo inicializador de classe recebendo
    # 2 parametros operando 1 e operando 2
    def  __init__(self, num1, num2): # self faz referencias ao proprio objeto
        self.resultado = 0 # então estamos definindo o atributos
        self.operando1 = num1 # do proprio obj estanciado e os tornando
        self.operando2 = num2 # acessiveis para outros metodos (def)

    def somar(self): # definição do metodo somar
        self.resultado = self.operando1 + self.operando2

    def subtrair(self): # definiçao do metodo subtrair
        self.resultado = self.operando1 - self.operando2

    def multiplicar(self): # definição do metodo multiplicar
        self.resultado = self.operando1 * self.operando2

    def dividir(self): #definição do metodo dividir
        self.resultado = self.operando1 / self.operando2
