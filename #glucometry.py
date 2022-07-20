resultadoGlucometria=float(input(" digital el resultado de la glucometria  "  ))
print(resultadoGlucometria)

if(resultadoGlucometria>100):
   print("hiperglicemia")


elif(resultadoGlucometria<70):
    print("hipoglicemia")


elif(70 <= resultadoGlucometria <=100):
   print("normal")