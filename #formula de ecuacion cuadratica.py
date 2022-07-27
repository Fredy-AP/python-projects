
import math


def e2g(a,b,c):
    dis= (math.pow(b,2) - 4*a*c)

    if a == 0:
        print("el valor de a debe ser diferente a 0")
    elif dis< 0:
        print("solucion solo en numeros complejos")
    else :
        x1=(-b + math.sqrt(dis))/(2*a)
        x2=(-b - math.sqrt(dis)) / (2*a)
        print(f"x1:{x1}, x2:{x2}")
    #programa principal

a=float (input("ingresa valor de a: "))
b=float (input("ingresa valor de b: "))
c=float (input("ingresa valor de c: "))
resul=e2g(a,b,c)
    