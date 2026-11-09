
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


def restar_fracciones(num1, den1, num2, den2):
    numerador = num1 * den2 - num2 * den1
    denominador = den1 * den2

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor
    denominador = denominador // divisor

    return numerador, denominador

def multiplicar_fracciones(num1, den1, num2, den2):
    numerador = num1 * num2 
    denominador = den1 * den2

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor
    denominador = denominador // divisor

    return numerador, denominador

def division_fracciones(num1, den1, num2, den2):
    numerador = num1 * den2 
    denominador = num2 * den1

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor
    denominador = denominador // divisor

    return numerador, denominador

def calcular_potencia(base, exponente):
    potencia = base ** exponente  
    return potencia


def es_binario(texto):
    if texto == "":
        return False

    posicion = 0
    while posicion < len(texto):
        if texto[posicion] != "0" and texto[posicion] != "1":
            return False
        posicion = posicion + 1

    return True


def binario_a_decimal(binario):
    decimal = 0

    posicion = 0
    while posicion < len(binario):
        decimal = decimal * 2 + int(binario[posicion])
        posicion = posicion + 1

    return decimal

def decimal_a_binario(numero):
    if numero == 0:
        return "0"

    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2

    return binario

def sumar_binarios(binario1, binario2):
    decimal1 = binario_a_decimal(binario1)
    decimal2 = binario_a_decimal(binario2)
    suma = decimal1 + decimal2
    resultado = decimal_a_binario(suma)
    return resultado

def resta_binarios(binario1, binario2):
    decimal1 = binario_a_decimal(binario1)
    decimal2 = binario_a_decimal(binario2)
    resta = decimal1 - decimal2

    if resta < 0:
        resultado = "-" + decimal_a_binario(resta * -1)
    else:
        resultado = decimal_a_binario(resta)

    return resultado





def agregar_termino(texto, coeficiente, variable):
    if coeficiente >= 0:
        texto = texto + " + " + str(coeficiente) + variable
    else:
        texto = texto + " - " + str(abs(coeficiente)) + variable
    return texto


def polinomio_a_texto(a, b, c):
    texto = str(a) + "x^2"
    texto = agregar_termino(texto, b, "x")
    texto = agregar_termino(texto, c, "")
    return texto


def polinomio4_a_texto(a, b, c, d, e):
    texto = str(a) + "x^4"
    texto = agregar_termino(texto, b, "x^3")
    texto = agregar_termino(texto, c, "x^2")
    texto = agregar_termino(texto, d, "x")
    texto = agregar_termino(texto, e, "")
    return texto


def sumar_polinomios(a1, b1, c1, a2, b2, c2):
    return a1 + a2, b1 + b2, c1 + c2


def restar_polinomios(a1, b1, c1, a2, b2, c2):
    return a1 - a2, b1 - b2, c1 - c2


def multiplicar_polinomios(a1, b1, c1, a2, b2, c2):
    a = a1 * a2
    b = a1 * b2 + b1 * a2
    c = a1 * c2 + b1 * b2 + c1 * a2
    d = b1 * c2 + c1 * b2
    e = c1 * c2
    return a, b, c, d, e
