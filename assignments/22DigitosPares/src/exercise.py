def main():
    #escribe tu código abajo de esta línea
    import math
    numero=(input("Dame un número"))

    
    x=0
    count=0
    lista=[int(i)for i in numero]
    if len(lista)==4 and lista.count(0)==0:
        while x<len(lista):
            if (math.fmod(lista[x],2))==0:
                    count=count+1
            x=x+1    

        print("El número de pares es: ",count)
    else:
        print("lo siento, ingresa un número de 4 dígitos y que no empiece con 0")



    pass


if __name__ == '__main__':
    main()
