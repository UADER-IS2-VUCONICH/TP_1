import matplotlib.pyplot as plt

def collatz(n): #Calcula la secuencia de Collatz para un número dado n
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Calcula el número de iteraciones para los números entre 1 y 10000
convergences = []
for n in range(1, 10001):
    sequence = collatz(n)
    convergences.append(len(sequence) - 1)  # Restamos 1 para excluir el último elemento (que es 1)

# Gráfico del número de iteraciones en función del número inicial n
plt.figure(figsize=(10, 6))
plt.plot(range(1, 10001), convergences, marker='o', linestyle='None', color='b', markersize=2)
plt.title('Conjetura de Collatz')
plt.xlabel('Número inicial (n)')
plt.ylabel('Número de iteraciones para converger')
plt.grid(True)
plt.show()