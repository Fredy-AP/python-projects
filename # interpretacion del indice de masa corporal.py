# interpretacion del indice de masa corporal tomado de heal books editorial manual de nutricion , realizado por Fredy  A pelaez.
#nota para parar el programa insertar los dos valores en cero.

while True:

    peso=float(input('por favor digite su peso en kilogramos '))
    talla=float(input('por favor digite su talla en centimetros  '))
    formula= peso/talla**2
    formula2= formula*10000
    print(formula2)

    if(formula2<=16):
        print("deficit energetico grado 3 muy severo")

    elif(16 <= formula2 <=16.9):
        print("deficit energetico grado 2 severo")

    elif(17 <= formula2 <=18.4):
        print("deficit energetico grado 1 ")

    elif(18.5 <= formula2 <=20):
        print("normal o bajo")

    elif(20 <= formula2 <=24.9):
        print("normal")

    elif(25 <= formula2 <=26.9):
        print("sobrepeso")

    elif(27 <= formula2 <=29.9):
        print("preobesidad")

    elif(30 <= formula2 <=34.9):
        ("obesidad grado uno ")  

    elif(35 <= formula2 <=39.9):
        print("obesidad grado dos severo ") 

    elif(40 <= formula2 <=49.9):
        print("obesidad grado 3 morbida") 

    elif(formula2 >=50.0):
        print("obesidad grado 4 extrema") 

    elif(formula2==0):
        break










