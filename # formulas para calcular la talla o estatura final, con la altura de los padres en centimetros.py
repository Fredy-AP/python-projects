# formulas para calcular la talla o estatura final
#https://www.mayoclinic.org/es-es/healthy-lifestyle/childrens-health/expert-answers/child-growth/faq-20057990#:~:text=Suma%20la%20estatura%20de%20la,13%20cent%C3%ADmetros)%20para%20las%20ni%C3%B1as.

tallaDelPadre=float(input("por favor digitar la talla del padre "))

tallaDeLaMadre=float(input("por favor digitar la talla de la madre  "))


formulaNinos1=(tallaDelPadre+tallaDeLaMadre+13)
formulaNinos=formulaNinos1/2

formulaDos=formulaNinos+6.5

print('el nino puede llegar a medir', formulaDos)

formulaNinas1=(tallaDeLaMadre + tallaDelPadre-13)
formulaNinas=formulaNinas1/2

formulaTres=formulaNinas-6.5

print('la nina puede llegar a medir', formulaTres)




