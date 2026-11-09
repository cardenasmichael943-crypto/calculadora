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
        print("15.operaciones con polinomios (suma, resta y multiplicacion)")
       
    
        print("--------------------------------------------")

    # Pide la opcion. Se guarda como texto, por eso mas abajo
    # se compara con comillas: operacion == "1"
        operacion = input("ingresa el numero de la operacion que deseas: ")


        print("-------------------------------------------")


        #Bloqueo: si lo que escribio el usuario No esta en la lista de oopciones
        #Valida, avisa y cierra el programa 
        if operacion not in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9","10","11","12","13","14","15"]:
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
            while numero2 == 0:
                print("no se puede dividir entre cero")
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
            while num2 == 0:
                print("no se puede dividir entre una fraccion que vale 0")
                num2 = int(input("numerador: "))
            den2 = int(input("denominador: "))
            while den2 == 0:
                print("el denominador no puede ser 0")
                den2 = int(input("denominador: "))

            numerador, denominador = division_fracciones(num1, den1, num2, den2)
            print("el resultado es:", numerador, "/", denominador)

        elif operacion == "10":
        
            base = int(input("ingresa la base: "))
            exponente = int(input("ingresa el exponente: "))

            while base == 0 and exponente < 0:
                print("0 no se puede elevar a un exponente negativo")
                exponente = int(input("ingresa el exponente: "))

            resultado = calcular_potencia(base, exponente)
            print(resultado)
                

        elif operacion == "11":

            binario = input("ingresa el numero binario: ")
            while es_binario(binario) == False:
                print("un numero binario solo tiene 0 y 1")
                binario = input("ingresa el numero binario: ")

            decimal = binario_a_decimal(binario)
            print("el numero en decimal es:", decimal)
            

       
        elif operacion == "12":

            numero = int(input("ingresa el numero decimal: "))
            while numero < 0:
                print("el numero no puede ser negativo")
                numero = int(input("ingresa el numero decimal: "))

            binario = decimal_a_binario(numero)
            print("el numero en binario es:", binario)
            

        elif operacion == "13":

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
            

        elif operacion == "14":
        
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



        #POLINOMIOS

        elif operacion == "15":

            print("primer polinomio (ax^2 + bx + c)")
            a1 = float(input("a: "))
            b1 = float(input("b: "))
            c1 = float(input("c: "))

            print("segundo polinomio (ax^2 + bx + c)")
            a2 = float(input("a: "))
            b2 = float(input("b: "))
            c2 = float(input("c: "))

            print("-------------------------------------------")
            print("primer polinomio:  ", polinomio_a_texto(a1, b1, c1))
            print("segundo polinomio: ", polinomio_a_texto(a2, b2, c2))

            a, b, c = sumar_polinomios(a1, b1, c1, a2, b2, c2)
            print("suma:  ", polinomio_a_texto(a, b, c))

            a, b, c = restar_polinomios(a1, b1, c1, a2, b2, c2)
            print("resta: ", polinomio_a_texto(a, b, c))

            a, b, c, d, e = multiplicar_polinomios(a1, b1, c1, a2, b2, c2)
            print("multiplicacion: ", polinomio4_a_texto(a, b, c, d, e))


    

        elif operacion == "0":
            print("proceso finalizado")
            break
            
        if operacion == "1" or operacion == "2" or operacion == "3" or operacion == "4":


            while True:

                print("----------------------------------------------")
                otro_numero = input("deseas ingresar otro numero (presiona enter para continuar y escribe no para terminar): ")
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


