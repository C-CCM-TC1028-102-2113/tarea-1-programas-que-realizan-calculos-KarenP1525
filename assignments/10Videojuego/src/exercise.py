def main():
    #escribe tu código abajo de esta línea
    nuevos=int(input("Dame la cantidad de juegos nuevos: "))
    usados=int(input("Dame la cantidad de juegos usados: "))

    tot=(nuevos*1000)+(usados*350)
    print("El total de la es: ",tot)
    pass



if __name__ == '__main__':
    main()
