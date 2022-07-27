from re import M


sexo=input("ingrese su sexo[M,F]:")
edad=int(input('ingrese su edad: '))

if sexo=='F':
    if(edad>18):
        print("usted es mujer y mayor de edad")

    else:
        print('eres menor de edad')    

elif sexo=='M':
    if(edad>65):
        print('Eres un adulto mayor')
    else:
        print('te falta para pensionar')