while True:
    print('\n/111/Programa para cambio de temperatura///l/\n')
    "-----Atributos-----"
    Tipo_Temperatura = 'a'
    Temperatura = 0
    Trasformacion = 'b'
    Respuesta = 0.0
    10

    "-----Metodos-----"
    def llenado( ):
        global Tipo_Temperatura, Temperatura, Trasformacion
        Tipo_Temperatura=input("""Introduce el tipo de temperatura a corde lo siguente:
        C -->Grados Celsius(°C)
        K --Grados Kelvin( °K)
        F-Grados Farenheit(°F)\n""")

    Temperatura=int( input ( 'Introduce la cantidad de la temperatura: '))

    Trasformacion=input("""\nIntroduce el tipo de temperatura al que deseas trasformarla:
    C->Grados Celsius(°C)
    K--Grados Kelvin( °K)
    F--Grados Farenheit (°F)\n""")

    def Trasformacion_A_Celsius():      
        if Tipo_Temperatura=='C':       
            print('\nNo puedes trasformarlo a la misma temperatura')
        if Tipo_Temperatura=='K':
            Respuesta=Temperatura-273
            print(f'\nLa trasformacion de °K --> °C es: {Respuesta}°C')
        elif Tipo_Temperatura=='F' :
            Respuesta=( Temperatura-32)/1.8
            print(f'\nLa trasformacion de °F --> C es: {Respuesta}°C')  

    def Trasformacion_A_Kelvin():
        if Tipo_Temperatura=='K':
            print('\nNo puedes trasformarlo a la misma temperatura')
        if Tipo_Temperatura=='C':
            Respuesta=Temperatura+273
            print(f' La trasformacion de °C --> °K es: {Respuesta}°K')
        elif Tipo_Temperatura=='F':
            Respuesta=(Temperatura-32 )/1.8
            Respuestat=273
            print(f'La trasformacion de °F -->°K es: {Respuesta}°K')

    def Trasformacion_A_Farenheit( ):
        if Tipo_Temperatura=="F":
            print( '\nNo puedes trasformarlo a la misma temperatura ')
        if Tipo_Temperatura=="C" :
            Respuesta=1.8*Temperatura+32
            print(f'La trasformacion de °C --> °F es: {Respuesta}° F')
        elif Tipo_Temperatura=='K':
            Respuesta=Temperatura-2/5
            Respuesta=1.8*Respuesta+32  
            print(f'La trasformacion de °K --> °F es: {Respuesta}°F')

    "-----Ejecucion----"
    llenado()
    if Trasformacion=='C':
        Trasformacion_A_Celsius()
    elif Trasformacion=="K":
        Trasformacion_A_Kelvin()
    elif Trasformacion=='F':
        Trasformacion_A_Farenheit()

