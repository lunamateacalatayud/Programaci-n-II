# Ejercicio 3: Ecuacion cuadratica
# Calatayud Luna Mariana
import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        return (self.__b * self.__b) - (4 * self.__a * self.__c)
    def getRaiz1(self):
        discr = self.getDiscriminante()
        if discr >= 0:
            num = -self.__b + math.sqrt(discr)
            den = 2 * self.__a
            return num / den
        else:
            return 0
    def getRaiz2(self):
        discr = self.getDiscriminante()
        if discr >= 0:
            num = -self.__b - math.sqrt(discr)
            den = 2 * self.__a
            return num / den
        else:
            return 0
# programa de prueba      
a, b, c = map(float, input("ingrese a,b,c: ").split())
ec = EcuacionCuadratica(a, b, c)
discr = ec.getDiscriminante()
if discr > 0:
    r1 = round(ec.getRaiz1(), 1)
    r2 = round(ec.getRaiz2(), 1)
    print("la ecuacion tiene dos raices", r1, "y", r2)
elif discr == 0:
    r = round(ec.getRaiz1(), 1)
    print("La ecuacion tiene una raiz", r)
else:
    print("La ecuacion no tiene raices reales")