def password_check(passwd):
    
    SpecialSym=["$","@","#","%"]
    val=True
    
    if len(passwd)<6:
        print("El password debe tener al menos seis caracteres")
        val=False
    elif len(passwd)>20:
        print("EL password no debe ser mayor de 8 caracteres")
        val=False
    elif not any(char.isdigit()for char in passwd):
        print("Password debe tener al menos un Numeral")
        val=False
    
    elif not any (char.isupper()for char in passwd):
        print ("debe tener al menos una letra en mayuscula ") 
        val=False
    elif not any (char.islower()for char in passwd):
        print ("Debe tener al menos una letra en minuscula ") 
        val=False
    elif not any (char in SpecialSym for char in passwd):
        print ("password debe tener alguno de esto simbolos $@#") 
        val=False
    elif val:
        return val
     
   
def main():
    passwd=input("Digita El Password \t")
    
                
    if (password_check(passwd)):
        print("Password es valido ")
    else:
        print("Password es invalido !!")
    
                
if __name__ == "__main__":
        main()   

