# Ejercicio 4 POO
# Calatayud Luna Mariana
import math
class Estadistica:
    def __init__(self, datos):
        self.__datos = datos
    def promedio(self):
        suma = 0
        n = len(self.__datos)
        for i in range(0, n):
            suma = suma + self.__datos[i]
        return suma / n
    def desviacion(self):
        prom = self.promedio()
        suma = 0
        n = len(self.__datos)
        for i in range(0, n):
            diferencia = self.__datos[i] - prom
            suma = suma + (diferencia * diferencia)
        return math.sqrt(suma / (n - 1))

datos = list(map(float, input("Ingrese 10 numeros: ").split()))
estad = Estadistica(datos)
prom = estad.promedio()
desv = estad.desviacion()
print("El promedio es", round(prom, 2))
print("La desviacion estandar es", round(desv, 2))