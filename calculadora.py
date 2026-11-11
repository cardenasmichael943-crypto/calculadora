
#Aqui en este archivo se guardan todas las funciones que hacen los calculos 



# Funcion: calcular_suma
# Que hace: suma dos numeros.
# Recibe:   numero1 y numero2 (los dos numeros que se van a sumar).
# Devuelve: el resultado de la suma.
# Ejemplo:  calcular_suma(2, 3)  da  5

def calcular_suma (numero1, numero2):
    suma = numero1 + numero2        # suma los dos numeros y guarda el resultado en "suma"
    return suma                     # entrega el resultado a quien llamo la funcion



# Funcion: calcular_resta
# Que hace: resta dos numeros (al primero le quita el segundo).
# Recibe:   numero1 y numero2.
# Devuelve: el resultado de la resta.
# Ejemplo:  calcular_resta(5, 3)  da  2

def calcular_resta (numero1, numero2):
    resta = numero1 - numero2       # resta los dos numeros y guarda el resultado en "resta"
    return resta                    # entrega el resultado

# Funcion: calcular_multiplicacion
# Que hace: multiplica dos numeros.
# Recibe:   numero1 y numero2.
# Devuelve: el resultado de la multiplicacion.
# Ejemplo:  calcular_multiplicacion(4, 3)  da  12

def calcular_multiplicacion (numero1, numero2):
    multiplicacion = numero1 * numero2      # se multiplican los dos numeros
    return multiplicacion                   #entrega el resultado


# Funcion: calcular_division
# Que hace: divide el primer numero entre el segundo.
# Recibe:   numero1 y numero2.
# Devuelve: el resultado de la division (siempre con decimal, ej: 5.0).
# Ejemplo:  calcular_division(10, 2)  da  5.0
# OJO: no se puede dividir entre 0. Por eso la consola revisa que
#      numero2 no sea 0 antes de usar esta funcion.

def calcular_division (numero1, numero2):
    division = numero1 / numero2    # se dividen los dos numeros        
    return division                 #entrega el resultado



#Funcuion: calcular raiz
# Por que se usa  ** 0.5 ?
#   Sacar la raiz cuadrada es buscar el numero que, multiplicado
#   por si mismo, da el numero que tenemos.
#   Ejemplo: la raiz de 25 es 5, porque 5 x 5 = 25.
#
#   En Python, elevar un numero a 2 es multiplicarlo por si mismo:
#       5 ** 2  da  25
#   Y elevar a 0.5 (que es la mitad de 1) hace lo contrario,
#   devuelve el numero de antes:
#       25 ** 0.5  da  5

def calcular_raiz(numero):
    raiz = numero ** 0.5    # ** significa "elevado a"; elevar a 0.5 es sacar la raiz cuadrada
    return raiz             # entrega el resultado


#Fracciones
# Una fraccion tiene dos partes:
#   numerador   (el numero de arriba)
#   denominador (el numero de abajo)
# En las funciones, num1/den1 es la primera fraccion
# y num2/den2 es la segunda fraccion.


# Funcion: calcular_divisor_comun
# Que hace: busca el numero MAS GRANDE que divide exacto a otros dos.
#           Sirve para simplificar fracciones.
# Recibe:   numero1 y numero2.
#busca el número más grande que puede dividir exactamente al numerador y al denominador. En este caso es 5.
# Devuelve: el divisor comun mas grande.
# Ejemplo:  con 8 y 16 da 8, porque 8 divide exacto a los dos.
#           Asi, la fraccion 8/16 se simplifica a 1/2 (dividiendo
#           arriba y abajo entre 8).
def calcular_divisor_comun(numero1, numero2):
    numero1 = abs(numero1)                   # abs quita el signo negativo (-8 pasa a 8)
    numero2 = abs(numero2)                   # lo mismo para el segundo numero
    while numero2 != 0:                     # repite mientras numero2 no sea 0
        resto = numero1 % numero2    # el simbolo % da lo que sobra al dividir
        numero1 = numero2            # numero1 ahora vale lo que valia numero2
        numero2 = resto              # numero2 ahora vale lo que sobro
    return numero1                   # cuando numero2 llega a 0, numero1 es la respuesta
 

# Funcion: sumar_fracciones
# Que hace: suma dos fracciones y deja el resultado simplificado.
# Recibe:   num1, den1 (primera fraccion) y num2, den2 (segunda).
# Devuelve: dos valores: el numerador y el denominador del resultado.
# Ejemplo:  1/2 + 1/3  da  5/6
# Regla:    a/b + c/d = (a*d + c*b) / (b*d)

def sumar_fracciones(num1, den1, num2, den2):
    numerador = num1 * den2 + num2 * den1   # calcula el numerador de la suma
    denominador = den1 * den2                # el nuevo denominador es denominador por denominador

    divisor = calcular_divisor_comun(numerador, denominador)      # paso 1: busca el numero mas grande que divide exacto al numerador y al denominador
    numerador = numerador // divisor              # paso 2: divide el numerador entre ese numero (// es una division sin decimales). Ej: 8 // 8 = 1
    denominador = denominador // divisor          # paso 3: divide el denominador entre el mismo numero. Ej: 16 // 8 = 2, y 8/16 queda 1/2

    return numerador, denominador       #devuelve los dos valores el numerador y el denominador



# Funcion: restar_fracciones
# Que hace: resta dos fracciones y deja el resultado simplificado.
# Recibe:   num1, den1 (primera fraccion) y num2, den2 (segunda).
# Devuelve: el numerador y el denominador del resultado.
# Ejemplo:  1/2 - 1/3  da  1/6
# Regla:    a/b - c/d = (a*d - c*b) / (b*d)

def restar_fracciones(num1, den1, num2, den2):
    numerador = num1 * den2 - num2 * den1   # igual que la suma, pero restando
    denominador = den1 * den2               # denominador por denominador

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor                        #se hace los mismos pasos de la suma 
    denominador = denominador // divisor

    return numerador, denominador           #devuelve los dos valores



# Funcion: multiplicar_fracciones
# Que hace: multiplica dos fracciones y simplifica el resultado.
# Recibe:   num1, den1 (primera fraccion) y num2, den2 (segunda).
# Devuelve: el numerador y el denominador del resultado.
# Ejemplo:  2/3 x 3/4  da  1/2
# Regla:    a/b x c/d = (a*c) / (b*d)   (arriba con arriba, abajo con abajo)

def multiplicar_fracciones(num1, den1, num2, den2):
    numerador = num1 * num2          # multiplica los numeradores entre si
    denominador = den1 * den2        # multiplica los denominadores entre si

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor
    denominador = denominador // divisor

    return numerador, denominador     # devuelve los dos valores


# Funcion: division_fracciones
# Que hace: divide la primera fraccion entre la segunda y simplifica.
# Recibe:   num1, den1 (primera fraccion) y num2, den2 (segunda).
# Devuelve: el numerador y el denominador del resultado.
# Ejemplo:  1/2 dividido 1/4  da  2/1
# Regla:    a/b dividido c/d = (a*d) / (c*b)   (se multiplica en cruz)
# OJO:      num2 no puede ser 0 (no se puede dividir entre una fraccion
#           que vale 0). La consola lo revisa antes de llamar esta funcion.

def division_fracciones(num1, den1, num2, den2):
    numerador = num1 * den2                   # numerador de la primera por denominador de la segunda
    denominador = num2 * den1                 # numerador de la segunda por denominador de la primera

    divisor = calcular_divisor_comun(numerador, denominador)
    numerador = numerador // divisor
    denominador = denominador // divisor

    return numerador, denominador           #devuelve los dos valores

# Funcion: calcular_potencia
# Que hace: eleva un numero a una potencia.
# Recibe:   base (el numero que se multiplica) y
#           exponente (cuantas veces se multiplica).
# Devuelve: el resultado de la potencia.
# Ejemplo:  calcular_potencia(2, 3)  da  8   (porque 2 x 2 x 2 = 8)
# OJO:      0 elevado a un exponente negativo da error; la consola
#           revisa ese caso antes de llamar a esta funcion.

def calcular_potencia(base, exponente):
    potencia = base ** exponente  # los dos asteriscos ** significan "elevado a"
    return potencia               # entrega el resultado




#Numeros Binarios 
# El sistema binario solo usa dos digitos: 0 y 1.
# Los numeros binarios se manejan como TEXTO (por ejemplo "1011"),
# porque hay que mirar cada digito por separado.
# Como se lee un numero binario?
#   Cada lugar del numero vale el DOBLE que el lugar que esta a su
#   derecha. De derecha a izquierda los lugares valen: 1, 2, 4, 8, 16...
#   Se suman solo los lugares que tienen un 1.
#
#   Ejemplo con 1011:
#       lugar:    8     4     2     1
#       digito:   1     0     1     1
#       vale:     8  +  0  +  2  +  1   =  11
#   Entonces el binario 1011 es el decimal 11.
# POR QUE LOS BINARIOS SE MANEJAN COMO TEXTO?
#   Se guardan como TEXTO, entre comillas, por ejemplo "1011".
#   Asi se puede mirar cada digito por separado.
#
# COMO SE SACA UN DIGITO DE UN TEXTO?
#   Con corchetes y la posicion. La posicion empieza a contar desde 0:
#       texto = "1011"
#       texto[0]  es  "1"    (el primer digito)
#       texto[1]  es  "0"    (el segundo)
#       texto[2]  es  "1"    (el tercero)
#       texto[3]  es  "1"    (el cuarto y ultimo)
#   Y len(texto) dice cuantos caracteres tiene:  len("1011") es 4.


# Funcion: es_binario
# Que hace: revisa si un texto es un numero binario valido,
#           es decir, que solo tenga ceros y unos.
# Recibe:   texto (lo que escribio el usuario).
# Devuelve: True (verdadero) si es binario, False (falso) si no lo es.
# Ejemplos: es_binario("1011")  da  True
#           es_binario("1021")  da  False   (tiene un 2)
#           es_binario("")      da  False   (no escribio nada)
def es_binario(texto):
    if texto == "":             # si el texto esta vacio
        return False             #no es un binario

    posicion = 0                     # "posicion" es el lugar del caracter que se va a revisar (0 = el primero)
    while posicion < len(texto):     # len() cuenta cuantos caracteres tiene el texto; repite hasta revisar todos
        if texto[posicion] != "0" and texto[posicion] != "1":   # texto[posicion] es el caracter que esta en ese lugar
            return False     # si hay algo distinto de 0 y 1, no es binario
        posicion = posicion + 1     # pasa al siguiente caracter

    return True  # si reviso todo y no encontro nada raro, si es binario 



# Funcion: binario_a_decimal
# Que hace: convierte un numero binario a un numero normal (decimal).
# Recibe:   binario (texto con ceros y unos, por ejemplo "1011").
# Devuelve: el numero en decimal.
# Ejemplo:  binario_a_decimal("1011")  da  11
#
# Como funciona:
#   Lee los digitos de izquierda a derecha. En cada vuelta hace dos cosas:
#       1) DUPLICA lo que llevaba acumulado
#       2) le SUMA el digito nuevo
#   Duplicar es como correr todo un lugar hacia la izquierda: por eso
#   los primeros digitos terminan valiendo mas (8, 4, 2...).
#
#   Paso a paso con "1011":
#   (la variable "decimal" guarda lo que se lleva acumulado; empieza en 0)
#
#       vuelta  digito  llevaba   cuenta (llevaba x 2 + digito)   queda
#         1       1       0       0 x 2 + 1  =  0 + 1  =  1         1
#         2       0       1       1 x 2 + 0  =  2 + 0  =  2         2
#         3       1       2       2 x 2 + 1  =  4 + 1  =  5         5
#         4       1       5       5 x 2 + 1  = 10 + 1  = 11        11

def binario_a_decimal(binario):
    decimal = 0         # aqui se va acumulando el resultado; empieza en 0

    posicion = 0         # empieza por el primer digito (posicion 0)
    while posicion < len(binario):      # repite hasta recorrer todos los digitos
        decimal = decimal * 2 + int(binario[posicion])  # duplica lo acumulado y suma el digito nuevo.
                                                        # binario[posicion] es un texto ("1" o "0"); int() lo convierte en numero para poder sumarlo
        posicion = posicion + 1      # paso al siguiente digito

    return decimal             # entrega el numero ya convertido a decimal



# Funcion: decimal_a_binario
# Que hace: convierte un numero normal (decimal) a binario.
# Recibe:   numero (un entero, cero o mayor).
# Devuelve: el binario, como texto.
# Ejemplo:  decimal_a_binario(11)  da  "1011"
#
# Como funciona:
#   Divide el numero entre 2 una y otra vez, y en cada division guarda
#   lo que SOBRA (que siempre es 0 o 1). Se sigue hasta que el numero
#   llega a 0. Los sobrantes, leidos de ABAJO hacia ARRIBA, forman el
#   binario.
#
#   Paso a paso con 11:
#       division     resultado    sobra
#       11 / 2          5           1
#        5 / 2          2           1
#        2 / 2          1           0
#        1 / 2          0           1
#   Leyendo los sobrantes de abajo hacia arriba:  1 0 1 1  ->  "1011"
def decimal_a_binario(numero):
    if numero == 0:     # el 0 se escribe igual en binario...
        return "0"      # asi que lo entrega directo (sin esto, el resultado quedaria vacio)

    binario = ""         # texto vacio donde se van guardando los digitos
    while numero > 0:     # repite mientras el numero sea mayor que 0
        resto = numero % 2         # % da lo que sobra al dividir entre 2; siempre es 0 o 1
        binario = str(resto) + binario    # str() convierte el numero en texto; se pone AL PRINCIPIO del binario para que quede en el orden correcto
        numero = numero // 2         # // divide entre 2 sin decimales (11 // 2 = 5); asi el numero va bajando hasta llegar a 0

    return binario      # entrega el binario ya armado


# Funcion: sumar_binarios
# Que hace: suma dos numeros binarios.
# Recibe:   binario1 y binario2 (textos con ceros y unos).
# Devuelve: la suma, en binario (como texto).
# Ejemplo:  sumar_binarios("101", "11")  da  "1000"
#
# Como funciona (3 pasos):
#   1 pasa cada binario a decimal
#   2 suma los dos decimales
#   3 pasa el resultado otra vez a binario
#   Con "101" y "11":   5 + 3 = 8   y   8 en binario es "1000"

def sumar_binarios(binario1, binario2):
    decimal1 = binario_a_decimal(binario1)  # paso 1: el primer binario pasa a decimal ("101" -> 5)
    decimal2 = binario_a_decimal(binario2)  # paso 1: el segundo binario pasa a decimal ("11" -> 3)
    suma = decimal1 + decimal2              # paso 2: suma los dos decimales (5 + 3 = 8)
    resultado = decimal_a_binario(suma)     # paso 3: la suma pasa a binario (8 -> "1000")
    return resultado                         # entrega el resultado



# Funcion: resta_binarios
# Que hace: resta dos numeros binarios.
# Recibe:   binario1 y binario2 (textos con ceros y unos).
# Devuelve: la resta, en binario (con signo "-" si da negativa).
# Ejemplos: resta_binarios("101", "11")  da  "10"     (5 - 3 = 2)
#           resta_binarios("11", "101")  da  "-10"    (3 - 5 = -2)
#
# Como funciona (los mismos 3 pasos de la suma, pero restando):
#   1 pasa cada binario a decimal
#   2 resta los dos decimales
#   3 pasa el resultado a binario
#   Ojo: decimal_a_binario no sabe convertir numeros negativos, asi que
#   si la resta da negativa, primero se vuelve positiva, se convierte,
#   y al final se le pone el signo "-" adelante.

def resta_binarios(binario1, binario2):
    decimal1 = binario_a_decimal(binario1)     # paso 1: el primer binario pasa a decimal
    decimal2 = binario_a_decimal(binario2)     # paso 1: el segundo binario pasa a decimal
    resta = decimal1 - decimal2                # paso 2: resta los dos decimales

    if resta < 0:                      # si la resta dio un numero negativo (ej: -2)
        resultado = "-" + decimal_a_binario(resta * -1)  # lo vuelve positivo (resta * -1 da 2), lo pasa a binario ("10") y le pone el "-" adelante ("-10")
    else:                # si la resta NO es negativa
        resultado = decimal_a_binario(resta)      #la pasa a binario directamente

    return resultado          # entrega el resultado





