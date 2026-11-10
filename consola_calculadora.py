#este es nuestro archivo principal
#principal para ejecutar la calculadora
#¿que haces este archivo?
#este archivo hace tres cosas cuando se ejecuta las cuales son:
#   1. muestra el menu de opciones
#   2.Pide al usuario los datos (numeros, fraciones, binarios, etc...)
#   3. Llama a las funciones de calculadora.py para hacer la cuenta
#      y muestra el resultado.



from calculadora import *      #Importamos el archivo calculadora.py, para
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
        print("---------------------------------------------------")

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
        print("10.potenciacion")
        print("11.binario a decimal")
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
            print(f"ans: {resultado}")


        elif operacion == "2":
#operacion 2 resta

            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_resta(numero1, numero2)
            print(f"ans: {resultado}")

        elif operacion == "3":
#operacion 3 multiplicacion 

            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_multiplicacion(numero1, numero2)
            print(f"ans: {resultado}")

        elif operacion == "4":
#operacion 4 division
        
            numero1 = float(input("ingresa el primer numero: "))
            numero2 = float(input("ingresa el segundo numero: "))
            while numero2 == 0:
                print("no se puede dividir entre cero")
                numero2 = float(input("ingresa el segundo numero: "))
            resultado = calcular_division(numero1, numero2)
            print(f"ans: {resultado}")
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
                
                #Operacion 6 Suma de fracciones
        #las operaciones 6, 7, 8 y 9 piden datos de la misma forma: dos fracciones,
        #cada una con numerador y denominador

        elif operacion == "6":

            print("primera fraccion")
            num1 = int(input("numerador: "))        # numero de arriba de la primera fraccion
            den1 = int(input("denominador: "))      # numero de abajo de la primera fraccion
            print("------------------------------------------------")
            while den1 == 0:       # mientras el denominador sea 0...
                print("el denominador no puede ser 0")   # ...avisa que no se puede
                den1 = int(input("denominador: "))       # ...y lo pide otra vez
 
            print("segunda fraccion")
            num2 = int(input("numerador: "))          # numero de arriba de la segunda fraccion
            den2 = int(input("denominador: "))        # numero de abajo de la segunda fraccion
            while den2 == 0:                     # el denominador tampoco puede ser 0
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))

             # La funcion devuelve DOS valores, y aqui se guardan en dos variables
            numerador, denominador = sumar_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)    #muestra la fraccion resultado


                    #operacion 7 Resta de fracciones
            #igual que la opcion 6, pero en esta se llama la funcion restar_fracciones
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


               #operacion 8 Multiplicacion de fracciones
            #igual que la opcion 6, pero en esta se llama la funcion multiplicar_fracciones      
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
            
                #operacion 9 Division de fracciones
            #igual que la opcion 6, pero en esta se llama la funcion division_fracciones   
            # si el num2 es 0 no se puede dividir la fracion   
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
            while num2 == 0:                        # si el numerador es 0, la fraccion vale 0...
                print("no se puede dividir entre una fraccion que vale 0")  # ...y no se puede dividir entre ella
                num2 = int(input("numerador: "))        # lo pide otra vez
            den2 = int(input("denominador: "))      
            while den2 == 0:
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))

            numerador, denominador = division_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)


            #operacion 11 Potencia

        elif operacion == "10":
        
            base = int(input("ingresa la base: "))      #el numero que se va a elevar
            exponente = int(input("ingresa el exponente: ")) # a que potencia se eleva

            # 0 elevado a un exponente negativo da error, asi que se revisa:
            while base == 0 and exponente < 0:
                print("0 no se puede elevar a un exponente negativo")
                exponente = int(input("ingresa el exponente: ")) # pide otro exponente

            resultado = calcular_potencia(base, exponente) # calcula la potencia
            print(resultado)                               # muestra el resultado 


            #operacion 11 Binario a decimal     

        elif operacion == "11":
            # El binario se pide como TEXTO (sin int ni float),
            # porque hay que revisar cada digito.

            binario = input("ingresa el numero binario: ")
            while es_binario(binario) == False:              # mientras NO sea un binario valido...
                print("un numero binario solo tiene 0 y 1")  # ...avisa
                binario = input("ingresa el numero binario: ") # ...y lo pide otra vez

            decimal = binario_a_decimal(binario)         # convierte el binario a decimal, que es donde se llama la funcion binario_a_decimal
            print("el numero en decimal es:", decimal)   # muestra el resultado
            

            #operacion 12 Decimal a binario
       
        elif operacion == "12":

            numero = int(input("ingresa el numero decimal: "))      # pide un numero entero
            while numero < 0:                                       # si es negativo
                print("el numero no puede ser negativo")             # avisa
                numero = int(input("ingresa el numero decimal: "))  # y lo pide otra vez

            binario = decimal_a_binario(numero)                      # convierte a binario
            print("el numero en binario es:", binario)               # muestra el resultado


            #operacion 13 Suma de binarios

        elif operacion == "13":

            binario1 = input("ingresa el primer numero binario: ")
            while es_binario(binario1) == False:                    # revisa que solo tenga 0 y 1
                print("un numero binario solo tiene 0 y 1")         #si coloco un numero decimal avisa que solo debe tener 0 y 1
                binario1 = input("ingresa el primer numero binario: ") #vuelve a pedir el numero

            binario2 = input("ingresa el segundo numero binario: ")
            while es_binario(binario2) == False:                     # revisa que solo tenga 0 y 1
                print("un numero binario solo tiene 0 y 1")
                binario2 = input("ingresa el segundo numero binario: ")

            resultado = sumar_binarios(binario1, binario2)          # suma los dos binarios
            print("la suma en binario es:", resultado)              # muestra el resultado


            #operacion 14 Resta de binarios 
            #es igual que la suma pero en este caso se restan 

        elif operacion == "14":
        
            binario1 = input("ingresa el primer numero binario: ")
            while es_binario(binario1) == False:
                print("un numero binario solo tiene 0 y 1")
                binario1 = input("ingresa el primer numero binario: ")

            binario2 = input("ingresa el segundo numero binario: ")
            while es_binario(binario2) == False:
                print("un numero binario solo tiene 0 y 1")
                binario2 = input("ingresa el segundo numero binario: ")
 
            resultado = resta_binarios(binario1, binario2)  # resta los dos binarios
            print("la resta en binario es:", resultado)     # muestra el resultado (con "-" si es negativo)


    
            #si la opcion es 0 el proceso es finalizado y se cierrra el ciclo
        elif operacion == "0":
            print("proceso finalizado")
            break


        #pregunta si desea agregar otro numero solo a las apoeraciones del 1 al 4
        # Permite seguir operando con el resultado que ya se tenia.
        # Ejemplo con suma: 2 + 3 = 5, luego "otro numero" 4 -> 5 + 4 = 9
            
        if operacion == "1" or operacion == "2" or operacion == "3" or operacion == "4":


            while True:           # ciclo interno: se repite hasta que el usuario escriba "no"

                print("----------------------------------------------")
                otro_numero = input("deseas ingresar otro numero (presiona enter para continuar y escribe no para terminar): ")
                if otro_numero == "no":                             #si escribe no muestra el total y sale del ciclo interno y vuelve al ciclo principal
                    print("el resultado total es:", resultado)
                    break

                numero3 = float(input("ingresar otro numero: "))    #pide el otro numero 

                # Opera el resultado que ya tenia con el numero nuevo
                if operacion == "1":
                    resultado = calcular_suma(resultado, numero3)

                elif operacion == "2":
                    resultado = calcular_resta(resultado, numero3)

                elif operacion == "3":
                    resultado = calcular_multiplicacion(resultado, numero3)

                elif operacion == "4":
                    resultado = calcular_division(resultado, numero3)

                print(resultado)

    # Aqui termina el ciclo principal. Como no hay un "break" al final,
    # el programa vuelve solo al menu (la opcion 0 es la que lo cierra).
                
        
ejecutar_calculadora()          # Esta linea llama a la funcion principal: aqui empieza a correr el programa



#decimal a hexadecimal
#binario a hexadecimal
#hexadecimal a decimal
#suma y resta de binarios
#raiz cubica
#logica proposional

