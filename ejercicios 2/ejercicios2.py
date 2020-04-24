
def main():
    print("Algoritmo para obtenre la suma de diez cantidades con el ciclo for")
    numero = 10

    if numero <= 0:
        print("¡Imposible!")
    else:
        suma = 0
        for i in range(1, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            suma = suma + valor
        print(f"La suma de los números que ha escrito es {suma}")


if __name__ == "__main__":
    main()