def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros():
    l = input("Ingrese números separados por comas: ")
    lista = l.split(",")
    numeros = [int(x) for x in lista]

    primos = [num for num in numeros if es_primo(num)]

    print("Números primos:", primos)


numeros()
