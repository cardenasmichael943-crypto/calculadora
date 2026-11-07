#este es nuestro archivo pincipal para ejecutar la calculadora

#¿que haces este archivo?
#este arcchivo hace tres cosas cuando se ejecuta las cuales son:
#   1. muestra el menu de opciones
#   2.Pide al usuario los datos (numeros, fraciones, binarios, etc...)
#   3. Llama a las funciones de calculadora.py para hacer la cuenta
#      y muestra el resultado.




from calculadora import *      #Importamos el archvivo calculadora.py, para traer
                               #traer todas las funciones y poder usarlas aqui
                                                  


def ejecutar_calculadora():   #la funcion principal para ejecutar todo el programa

# CICLO PRINCIPAL
    # Como es "while True", se repite una y otra vez: muestra el menu,
    # hace una operacion y vuelve a mostrar el menu.
    # Solo se detiene con un "break" (opcion 0 u opcion que no existe).
    while True:

        resultado = 0   #aqui se guarda el resultado de cada  operacion y en cada
                        #vuelta vuelve a empezar en 0


                        #Menu 

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

    # Pide la opcion. Se guarda como texto, por eso mas abajo
    # se compara con comillas: operacion == "1"
        operacion = input("ingresa el numero de la operacion que deseas: ")


        print("-------------------------------------------")


        #Bloqueo: si lo que escribio el usuario No esta en la lista de oopciones
        #Valida, avisa y cierra el programa 
        if operacion not in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9","10","11","12","13","14"]:
            print("esta opcion no esta")
            break  #sale del ciclo principal  y termina el programa


            #Opciones 1 al 4: Operaciones Basicas
            #Las cuatro hacen lo mismo: piden dos numeros, llaman a la
            #funcion que corresponda y muestran el resultado

        if operacion == "1":
#operacion 1 suma 
            numero1 = float(input("ingresa el primer numero: "))
        #pide el primer numero, esta con float para poder ingresar numeros enteros 
        #y decimales
            numero2 = float(input("ingresa el segundo numero: "))
        #pide el segundo numero
            resultado = calcular_suma(numero1, numero2)
        #llama a a la funcion suma 
            print(resultado)


        elif operacion == "2":
#operacion 2 resta

            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_resta(numero1, numero2)
            print(resultado)

        elif operacion == "3":
#operacion 3 multiplicacion 

            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_multiplicacion(numero1, numero2)
            print(resultado)

        elif operacion == "4":
#operacion 4 division
        
            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_division(numero1, numero2)
            print(resultado)
            #aca si el numero2 vale 0, el programa se cae ya que no se
            #puede dividir entre cero


                        #operacion 5: Raiz cuadrada
        elif operacion == "5":
            
            numero = int(input("ingresa el numero: ")) 
            #pide un numero entero
            if numero < 0:
                print("no existe raiz cuadrada real de un numero negativo")
                #si es negativo no hay raiz 

            else:           #si no es negativo calcula la raiz cuadrada y da el resultado
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


