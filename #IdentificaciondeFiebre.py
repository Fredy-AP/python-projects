#temperatura

SitioCorporal=input("ingrese el sitio [Axilar,Sublingual,Rectal]:")
Temperatura=float(input('ingrese el dato de la temperatura: '))

if SitioCorporal=='Axilar':
    if(35.3 <= Temperatura <=37.1):
        print("Normal")
if SitioCorporal=='Axilar':
     if(Temperatura >=37.2):
        print("fiebre")

if SitioCorporal=='Sublingual':
    if(35.9 <= Temperatura <=37.5):
        print("Normal")
if SitioCorporal=='Sublingual':
    if(Temperatura >=37.6):
         print("fiebre")


if SitioCorporal=='Rectal':
    if(36.0 <= Temperatura <=37.9):
        print("Normal")
if SitioCorporal=='Rectal':
    if(Temperatura >=38.0):
        print("fiebre")
   

