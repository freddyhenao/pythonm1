print("Este algoritmo determina de N cantidades, cuantas son mayores o igueles a cero,")
print("cuantas son menores o igueles a cero")
def main():
    print("NÚMEROS NEGATIVOS")
    numero = int(input("¿Cuántos valores va a introducir? "))

    if numero < 0:
        print("¡Imposible!")
    else:
        contador = 0
        Pcontador = 0
        for i in range(1, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            if valor <= 0:
                contador = contador + 1
            if valor >= 0:
                Pcontador=Pcontador+1

            print(f"Ha escrito {contador} números menores o iguales a cero.")
            print(f"Ha escrito {Pcontador} números mayores o iguales a cero.")

if __name__ == "__main__":
    main()
