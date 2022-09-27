#ConstanteDeProporcionalidad

#Proporcionalidad Directa Dos magnitudes son directamente
#proporcionales si al multiplicar #(dividir) una de ellas por un número,
#la otra queda multiplicada (o #dividida) por ese mismo número.
#Constante de#proporcionalidad #Si un valor a1 de la primera #magnitud le corresponde un valor
#a2 de la segunda magnitud, se #puede comprobar que el cociente o #razón entre estos dos valores es #siempre constante.


#Si un kilo de peras cuesta 2 dólares,
#¿cuál será el precio de compra según el precio?


#kilo=1
#pera=2


#Si 6 kilos de peras valen 10 dólares,
#¿cuánto costarán 12 kilos?
#Regla de 3 simple directa

kilos=6
Dolares=10
PreguntaKilos=12


formula=Dolares*PreguntaKilos/kilos


print(f"los 12 kilos valen {formula} Dollares")

#Regla de tres simple inversa
# Consiste en aprovechar la
#constante de
#proporcionalidad inversa
#para calcular el cuarto
#término.

#si 20 alumnos han pagado 10 US$ cada uno, para
#comprarle un regalo al profesor por su cumpleaños,
#¿cuánto tendrán que pagar si al final participan 24?

Alumnos=20
Condicion=24
Dolares=10

formula1=round(Alumnos*Dolares/Condicion)

print(f"los  alumnos deberan pagar {formula1}, Dollares ")



