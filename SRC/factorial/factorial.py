#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    print("Debe informar un número!")
    num = input("Ingrese un número para calcular el factorial: ")
    if not num.isdigit():
        print("Error: Debe ingresar un número entero.")
def factorial_rango(num_inicial, num_final):
    for i in range(num_inicial, num_final + 1):
        print("Factorial de", i, "es", factorial(i))


if len(sys.argv) < 3:
    print("Debe informar dos numeros para formar un rango! (inicial y final)")
    num_inicial = int(input("Ingrese el numero inicial del rango: "))
    num_final = int(input("Ingrese el numero final del rango: "))
    if num_final < num_inicial:
        print("El numero final debe ser mayor o igual al numero inicial.")
        sys.exit()
else:
    num = int(sys.argv[1])
    num_inicial = int(sys.argv[1])
    num_final = int(sys.argv[2])
    if num_final < num_inicial:
        print("El número final debe ser mayor o igual al número inicial.")
        sys.exit()

factorial_rango(num_inicial, num_final)
