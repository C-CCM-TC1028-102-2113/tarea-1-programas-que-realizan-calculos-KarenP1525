def main():
    #escribe tu código abajo de esta línea
    saldoAnt=float(input("Dame el saldo del mes anterior: "))
    ingresos=float(input("Dame los ingresos: "))
    egresos=float(input("Dame los egresos: "))
    cheques=int(input("Dame el número de cheques: "))

    tot=(saldoAnt*1.075)-ingresos+egresos+(cheques*13)
    print("El saldo final de la cuenta es: ",tot)
    pass

if __name__ == '__main__':
    main()
