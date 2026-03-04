# Ejercicio 4 Modular
# Calatayud Luna Mariana
import math
def promedio(lista):
    suma = 0
    n = len(lista)
    for i in range(0, n):
        suma = suma + lista[i]
    return suma / n
def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    n = len(lista)
    for i in range(0, n):
        diferencia = lista[i] - prom
        suma = suma + (diferencia**2)
    return math.sqrt(suma / (n - 1))

numeros = list(map(float, input("ingrese 10 numeros: ").split()))
prom = promedio(numeros)
desv = desviacion(numeros)
print("promedio: ", round(prom, 2))
print("desviacion estandar: ", round(desv, 2))