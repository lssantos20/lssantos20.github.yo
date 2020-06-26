import UIKit
//variaveis e contantes
var idade = 26
idade = 27
print(idade)

let nome: String = "lucas"
print(nome)

var (rg,cpf) = ("54564445",8678878777)





//variaveis opcionais

var nota:Int?
nota = 6
var media = nota! / 2
print(media)

//deslumbrando variaveis opcionais
//1 maneira "!"
//var media = nota! +2

// 2 maneira "if let"
var nota1: Int?
nota = 10
if let nota1 = nota{
    var media = nota1 + 2
    print(media)
    
}

//casting
var numeroString = "200"
var numero = 100
var soma = numero + Int(numeroString)! //converte de string para int
print(soma)



//operadores aritmeticos
// +,-,*,/ e %

//operadores compostos

var meunumero = 1
meunumero += 2
print(meunumero)


