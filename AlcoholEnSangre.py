#Efectos del acohol en el cuerpo
AlcoholConsumido=float(input("por favor digita el porcentaje de alcohol en la sangre, para parar el programa oprima* "))

    
if(AlcoholConsumido == 0):
    print("Normal")

elif(0.1<=AlcoholConsumido<=0.1):
    print("Estimulacion")

elif(0.2<=AlcoholConsumido<=0.2):
    print("FaltaDeCordinacion")

elif(0.3<=AlcoholConsumido<=0.3):
    print("Confusion")

elif(0.4<=AlcoholConsumido<=0.5):
    print("Coma")

elif(AlcoholConsumido>=0.6):
    print("Muerte")
    
   
    




