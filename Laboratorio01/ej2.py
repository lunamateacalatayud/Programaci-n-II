class EcuacionLineal:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def tieneSolucion(self):
        determinante = (self.__a * self.__d) - (self.__b * self.__c)
        if determinante != 0:
            return True
        else:
            return False
    def getX(self):
        deter = (self.__a * self.__d) - (self.__b * self.__c)
        num = (self.__e * self.__d) - (self.__b * self.__f)
        return num / deter
    def getY(self):
        deter = (self.__a * self.__d) - (self.__b * self.__c)
        num = (self.__a * self.__f) - (self.__e * self.__c)
        return num / deter
    
# programa de prueba
print("ngrese a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())
ec = EcuacionLineal(a, b, c, d, e, f)
if ec.tieneSolucion():
    x = ec.getX()
    y = ec.getY()
    print("x =", x, ", y =", y)
else:
    print("la ecuacion no tiene solucion")