#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def factorial(self, num):
        #Función que calcula el factorial de un número
        if num < 0:
            print("Factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        #Método que calcula el factorial entre min_num y max_num
        results = []
        for num in range(min_num, max_num + 1):
            results.append(self.factorial(num))
        return results

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Debe ingresar dos números para calcular los factoriales!")
        sys.exit()

    min_num = int(sys.argv[1])
    max_num = int(sys.argv[2])

    factorial_calc = Factorial()
    factorial_resultados = factorial_calc.run(min_num, max_num)

    for i, resultado in enumerate(factorial_resultados):
        print(f"Factorial de {min_num + i} es {resultado}")