import calculadora as calc



def ejecutar_calculadora()->None:
    suma_total = 0
    resta_total = 0
    multiplicacion_total = 1
    division_total = 0

    while True:
        operacion = input ("¿que operacion deseas realizar? \n Suma = + \n Resta = - \n Multiplicación = x \n División = ÷ \n  ")
        numero1 = float (input("ingresar numero 1: "))
        numero2 = float (input("ingresar numero 2: "))

        if operacion == "1":
            resultado = calc.calcular_suma(numero1, numero2)
            suma_total += resultado
        elif operacion == "2":
            resultado = calc.calcular_resta(numero1, numero2)
            resta_total -= resultado
        elif operacion == "3":
            resultado = calc.calcular_multiplicacion(numero1, numero2)
            multiplicacion_total *= resultado
        elif operacion == "4":
            resultado = calc.calcular_division(numero1, numero2)
            division_total /= resultado
        else:
            print("Operación no válida")

      
        continuar = input("Deseas ingresar más numeros: \n Si = 1 \n No = 2 \n")
        if continuar == "2":
            

            print(suma_total)
            print(resta_total)
            print(multiplicacion_total)
            print(division_total)
            break

ejecutar_calculadora()