
x=float(input('por favor digitar el numero   '))
y=float(input('por favor digitar el numero   '))



def mcd(x,y):
    mcd=1

    if x%y==0:
        return y 

    for k in range(int(y/2),0,-1):
        if x % k ==0 and y % k== 0:
            mcd=k
            break

    return mcd

print('el maximo comun divisor es ',  mcd (x,y))   


