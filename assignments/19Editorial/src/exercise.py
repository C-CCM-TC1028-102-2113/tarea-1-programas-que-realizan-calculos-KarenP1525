def main():
    #escribe tu código abajo de esta línea
    import math
    palabras=int(input("Dame el número de palabras: "))
    pags=palabras/475
    costo=60*.9
    tot=costo*math.trunc(pags)
    if math.fmod(60*.9,pags)>0:
        tot=tot+costo

    print("El costo de la publicación es: ",tot)
    pass


if __name__ == '__main__':
    main()
