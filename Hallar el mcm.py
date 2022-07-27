#hallar el mcm

x=float(input("por favor digitar el numero "))
y=float(input("por favor digitar el numero "))



def mcm(x,y):
    z=max(x,y)


    while True:
        if(z%x==0)and(z%y==0):
            return z

        z+=1


print('el minimo comun multiplo es ', mcm (x,y))









