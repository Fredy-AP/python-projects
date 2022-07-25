

from pickle import TRUE


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print("el numero es:", es_par (20))
print("el numero es:", es_par (70))
