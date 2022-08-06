#Calculo de terminos de la serie de finobacchi


fib0=1
fib1=2

while True:
    num_term=int(input("introduzca el numero de terminos de la sucesion"))
    if num_term>=0:
        break
if num_term==0:
    print("Termino N 0: ",fib0)
    suma=fib0
else:
    if  num_term==1:
        print("Termino N 0 :",fib0)
        print("Termino N 1 :",fib1)
        suma=fib0+fib1

    else:
        fib_n=fib0
        fib_nmas1=fib1
        print("Termino N0 : ", fib_n)
        fib_nmas1 = fib1 
        print('Término Nº 0 :', fib_n) 
        print('Término Nº 1 :', fib_nmas1) 
        suma = fib_n + fib_nmas1 
        for i in range (2, num_term+1): 
            fib_nmas2 = fib_nmas1 + fib_n 
            fib_n = fib_nmas1
            fib_nmas1 = fib_nmas2
            print('Término Nº', i,':', fib_nmas2)
            suma = suma + fib_nmas2 
            print('La suma de los ', num_term,' primeros términos es: ', suma)



    






