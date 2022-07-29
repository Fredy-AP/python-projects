#porcentaje de reserva corporales, circunferencia de cintura, interpretacion de circunferencia de cintura asociada con el riesgo de enfermedad cardiovascular.
while True:
    CincunferenciaCintura=float(input("por favor digitar la talla en centimetros, digitar 0 para finalizar el programa "))
    sexo=input("ingrese su sexo[M,F]:")

    if sexo=='M':
        if 94 <= CincunferenciaCintura <=101:
            print("Riesgo alto ")
        if CincunferenciaCintura>=102:
            print("Riesgo muy Alto")
        if CincunferenciaCintura<=94:
            print("no aplica")
        if CincunferenciaCintura<=0:
            print("no aplica")
            break

    if sexo=='F':
        if 80 <= CincunferenciaCintura<=87:
            print("Riesgo alto ")
        if CincunferenciaCintura>=88:
            print("Riesgo muy Alto")
        if CincunferenciaCintura<=79:
            print("no aplica")
        if CincunferenciaCintura<=0:
            print("no aplica")
            break
    






