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

def factorial_rango(num_inicial, num_final):
    if num_inicial <= 0:
        num_inicial = 1
    if num_final > 60:
        num_final = 60

    if num_final < num_inicial:
        print("El número final debe ser mayor o igual al número inicial.")
        return

    print("Factoriales desde", num_inicial, "hasta", num_final, ":")
    for i in range(num_inicial, num_final + 1):
        print("Factorial de", i, "es", factorial(i))

if len(sys.argv) < 2:
    print("Debe ingresar un rango para calcular los factoriales.")
    sys.exit()

rango = sys.argv[1]

if rango.startswith('-'):
    num_final = int(rango[1:])
    factorial_rango(1, num_final)
elif rango.endswith('-'):
    num_inicial = int(rango[:-1])
    factorial_rango(num_inicial, 60)
else:
    print("El formato del rango es incorrecto. Debe ser '-numero' o 'numero-'.")
