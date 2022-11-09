def somar(num1, num2):
    resultado = num1 + num2
    return resultado

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

soma = somar(10, 5) #15
subtracao = subtrair(30, 5) #5
mult = multiplicar(2, 4) #8
div = dividir(10, 2) #5

resultado = somar(5, 5) + subtrair(8, 4) #14

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
print(f"Resultado: {resultado}")