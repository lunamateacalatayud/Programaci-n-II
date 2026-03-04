# Ejercicio 1: Cronómetro
# Calatayud Luna Mariana
import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = 0
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time() * 1000
    def detener(self):
        self.__finaliza = time.time() * 1000
    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia

def ordenacionSelec(lista):
    n = len(lista)
    for i in range(0, n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        if minimo != i:
            aux = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = aux

# programa de prueba
numeros = []
cant = 5000
for i in range(0, cant):
    numero = random.randint(0, 5000)
    numeros.append(numero)
c = Cronometro()
c.inicia()
ordenacionSelec(numeros)
c.detener()
print("tiempo transcurrido:")
print(c.lapsoDeTiempo())