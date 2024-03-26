# Programa de python para mostrar todos los numeros primos dentro de un intervalo

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
# todos los numeros primos son mayores que 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)