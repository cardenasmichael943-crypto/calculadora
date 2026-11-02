
def calcular_suma (numero1, numero2):
    suma = numero1 + numero2
    return suma 

def calcular_resta (numero1, numero2):
    resta = numero1 - numero2
    return resta

def calcular_multiplicacion (numero1, numero2):
    multiplicacion = numero1 * numero2
    return multiplicacion

def calcular_division (numero1, numero2):
    division = numero1 / numero2
    return division

def calcular_raiz(numero):
    raiz = numero ** 0.5
    return raiz

def calcular_divisor_comun(numero1, numero2):
    numero1 = abs(numero1)
    numero2 = abs(numero2)
    while numero2 != 0:
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto
    return numero1


def sumar_fracciones(num1, den1, num2, den2):
    numerador = num1 * den2 + num2 * den1
    denominador = den1 * den2

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor
    denominador = denominador // divisor

    return numerador, denominador