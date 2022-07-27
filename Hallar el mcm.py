#hallar el mcm


def mcm(x,y):
    z=max(x,y)


    while True:
        if(z%x==0)and(z%y==0):
            return z

        z+=1


print(mcm(2,4))









