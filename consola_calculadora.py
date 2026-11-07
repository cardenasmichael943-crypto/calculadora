#este es nuestro archivo pincipal para ejecutar la calculadora



from calculadora import *      #importamos el archivo calculadora.py que es donde tenemos la funciones 
                                 #de nuestra calculadora
                                                  


def ejecutar_calculadora():   #la funcion principal para ejecutar todo el programa

    while True:

        resultado = 0

        print("----------CALCULADORA EN PYTHON--------------------")

        print("---------------------------------------------------")

        print("0.salir")
        print("1.suma")
        print("2.resta")
        print("3.multiplicacion")
        print("4.division")
        print("5.raiz cuadrada")
        print("6.suma de fracciones")
        print("7.resta de fracciones")
        print("8.multiplicacion de fracciones")
        print("9.division de fracciones")
        print("10.comvertir binario a dedimal")
        print("11.potenciacion")
        print("12.decimal a binario")
        print("13.suma de binarios")
        print("14.resta de binarios")


        print("--------------------------------------------")

        operacion = input("ingresa el numero de la operacion que deseas: ")


        print("-------------------------------------------")

        if operacion not in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9","10","11","12","13","14"]:
            print("esta opcion no esta")
            break 


        if operacion == "1":
            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_suma(numero1, numero2)
            print(resultado)

        elif operacion == "2":
            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_resta(numero1, numero2)
            print(resultado)

        elif operacion == "3":

            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_multiplicacion(numero1, numero2)
            print(resultado)

        elif operacion == "4":
            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_division(numero1, numero2)
            print(resultado)
       
        elif operacion == "5":
            
            numero = int(input("ingresa el numero: "))
            if numero < 0:
                print("no existe raiz cuadrada real de un numero negativo")
            else:
                resultado = calcular_raiz(numero)
                print(resultado)
                

        elif operacion == "6":

            print("primera fraccion")
            num1 = int(input("numerador: "))
            den1 = int(input("denominador: "))
            print("------------------------------------------------")
            while den1 == 0:
                print("el denominador no puede ser 0")
                den1 = int(input("denominador: "))

            print("segunda fraccion")
            num2 = int(input("numerador: "))
            den2 = int(input("denominador: "))
            while den2 == 0:
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))

            numerador, denominador = sumar_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)
            

        elif operacion == "7":
            
            print("primera fraccion")
            num1 = int(input("numerador: "))
            den1 = int(input("denominador: "))
            print("----------------------------------------------")
            while den1 == 0:
                print("el denominador no puede ser 0")
                den1 = int(input("denominador: "))
            
            print("segunda fraccion")
            num2 = int(input("numerador: "))
            den2 = int(input("denominador: "))
            while den2 == 0:
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))
            
            numerador, denominador = restar_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)
            
                
        elif operacion == "8":
            
            print("primera fraccion")
            num1 = int(input("numerador: "))
            den1 = int(input("denominador: "))
            print("--------------------------------------")
            while den1 == 0:
                print("el denominador no puede ser 0")
                den1 = int(input("denominador: "))
            
            print("segunda fraccion")
            num2 = int(input("numerador: "))
            den2 = int(input("denominador: "))
            while den2 == 0:
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))
            
            numerador, denominador = multiplicar_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)
            


        elif operacion == "9":
                    
            print("primera fraccion")
            num1 = int(input("numerador: "))
            den1 = int(input("denominador: "))
            print("---------------------------------------")
            while den1 == 0:
                print("el denominador no puede ser 0")
                den1 = int(input("denominador: "))
            
            print("segunda fraccion")
            num2 = int(input("numerador: "))
            den2 = int(input("denominador: "))
            while den2 == 0:
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))
            
            numerador, denominador = division_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)
            


        elif operacion == "10":

            binario = input("ingresa el numero binario: ")
            while es_binario(binario) == False:
                print("un numero binario solo tiene 0 y 1")
                binario = input("ingresa el numero binario: ")

            decimal = binario_a_decimal(binario)
            print("el numero en decimal es:", decimal)
            

        elif operacion == "11":

            base = int(input("ingresa la base: "))
            exponente = int(input("ingresa el exponente: "))

            while base == 0 and exponente < 0:
                print("0 no se puede elevar a un exponente negativo")
                exponente = int(input("ingresa el exponente: "))

            resultado = calcular_potencia(base, exponente)
            print(resultado)
            

        elif operacion == "12":

            numero = int(input("ingresa el numero decimal: "))
            while numero < 0:
                print("el numero no puede ser negativo")
                numero = int(input("ingresa el numero decimal: "))

            binario = decimal_a_binario(numero)
            print("el numero en binario es:", binario)
            

        if operacion == "13":

            binario1 = input("ingresa el primer numero binario: ")
            while es_binario(binario1) == False:
                print("un numero binario solo tiene 0 y 1")
                binario1 = input("ingresa el primer numero binario: ")

            binario2 = input("ingresa el segundo numero binario: ")
            while es_binario(binario2) == False:
                print("un numero binario solo tiene 0 y 1")
                binario2 = input("ingresa el segundo numero binario: ")

            resultado = sumar_binarios(binario1, binario2)
            print("la suma en binario es:", resultado)
            

        if operacion == "14":
        
            binario1 = input("ingresa el primer numero binario: ")
            while es_binario(binario1) == False:
                print("un numero binario solo tiene 0 y 1")
                binario1 = input("ingresa el primer numero binario: ")

            binario2 = input("ingresa el segundo numero binario: ")
            while es_binario(binario2) == False:
                print("un numero binario solo tiene 0 y 1")
                binario2 = input("ingresa el segundo numero binario: ")

            resultado = resta_binarios(binario1, binario2)
            print("la resta en binario es:", resultado)

        elif operacion == "0":
            print("proceso finalizado")
            break
            
        if operacion == "1" or operacion == "2" or operacion == "3" or operacion == "4":


            while True:

                print("----------------------------------------------")
                otro_numero = input("deseas ingresar otro numero (presiona cualquier tecla para continuar y para terminar escribe no): ")
                if otro_numero == "no":
                    print("el resultado total es:", resultado)
                    break

                numero3 = float(input("ingresar otro numero: "))

                if operacion == "1":
                    resultado = calcular_suma(resultado, numero3)

                elif operacion == "2":
                    resultado = calcular_resta(resultado, numero3)

                elif operacion == "3":
                    resultado = calcular_multiplicacion(resultado, numero3)

                elif operacion == "4":
                    resultado = calcular_division(resultado, numero3)

                print(resultado)

                

        


ejecutar_calculadora()



#decimal a hexadecimal
#binario a hexadecimal
#hexadecimal a decimal
#suma y resta de binarios
#raiz cubica


