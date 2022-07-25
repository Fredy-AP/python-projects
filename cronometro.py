
min_fin=int(input("ingrese la cantidad de minutos a cronometrar "))
for min in range(min_fin):
        for segundos in range(60):
            print(f"{min:02}:{segundos:02}")
print(f"{min_fin:02}:00")