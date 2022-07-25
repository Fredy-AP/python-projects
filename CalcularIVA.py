def CalcularTotalConIVA(valor,Iva):
    conIVA=valor+valor*Iva
    #conIVA=valor*(1+Iva)
    return conIVA

valor=int(input("ingrese el valor a facturar "))
Iva=float(input("ingrese el valor el IVA "))

ValorTotal=CalcularTotalConIVA(valor,Iva)
print(ValorTotal)