from fractions import Fraction 

print("Fracciones") 

n1=Fraction(input("Introduce un numero fraccionario,ejemplo 4/6    "    ))
print(n1)


n2=Fraction(input("introduce otro numero fraccionario, ejemplo 7/8    "  )) 
print(n2)


print("El resultado de la suma es: " + str(n1+n2))
print("El resultado de la resta es: " + str(n1-n2))
print("El resultado de la multiplicacion  es: " + str(n1*n2))
print("EL resultado de la division es: " + str(n1/n2) )
