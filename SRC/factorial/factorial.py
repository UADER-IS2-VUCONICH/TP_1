#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función que calcula el factorial de un número dado
def factorial(num): 
    # Comprueba si el número es negativo
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    # Si el número es 0, el factorial es 1
    elif num == 0: 
        return 1
    else: 
        fact = 1
        # Calcula el factorial usando un bucle while
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Función que calcula y muestra los factoriales en un rango dado
def factorial_rango(num_inicial, num_final):
    # Si el número inicial es menor o igual a 0, se ajusta a 1
    if num_inicial <= 0:
        num_inicial = 1
    # Si el número final es mayor a 60, se ajusta a 60
    if num_final > 60:
        num_final = 60

    # Comprueba si el número final es menor que el inicial
    if num_final < num_inicial:
        print("El número final debe ser mayor o igual al número inicial.")
        print("El número final debe ser mayor o igual que 1.")
        return

    # Muestra el rango de factoriales que se calcularán
    print("Factoriales desde", num_inicial, "hasta", num_final, ":")
    # Calcula y muestra los factoriales para cada número en el rango
    for i in range(num_inicial, num_final + 1):
        print("Factorial de", i, "es", factorial(i))

# Verifica si se proporciona un rango como argumento de línea de comandos
if len(sys.argv) < 2:
    print("Debe ingresar un rango para calcular los factoriales.")
    sys.exit()

# Obtiene el rango desde la línea de comandos
rango = sys.argv[1]

# Procesa el rango según el formato proporcionado
if rango.startswith('-'):
    # Si el rango comienza con "-", calcula los factoriales desde 1 hasta el número final
    num_final = int(rango[1:])
    factorial_rango(1, num_final)
elif rango.endswith('-'):
    # Si el rango termina con "-", calcula los factoriales desde el número inicial hasta 60
    num_inicial = int(rango[:-1])
    factorial_rango(num_inicial, 60)
else:
    # Si el formato del rango es incorrecto, muestra un mensaje de error
    print("El formato del rango es incorrecto. Debe ser '-numero' o 'numero-'.")
