def caracteres(palabra):
    return sorted(list(palabra))

def anagrama(palabra1, palabra2):
    return caracteres(palabra1) == caracteres(palabra2)

def filtrar_palabras_anagramas(palabras):
    resultado = []
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if anagrama(palabras[i], palabras[j]) and palabras[i] not in resultado:
                resultado.append(palabras[i])
                resultado.append(palabras[j])
    return resultado

def obtener_palabras():

    entrada = input("Ingrese palabras separadas por comas: ")
    palabras = [palabra.strip() for palabra in entrada.split(",") if palabra.strip()]

    while not palabras:
        print("No se ingresaron palabras válidas. Intenta nuevamente.")
        entrada = input("Ingrese palabras separadas por comas: ")
        palabras = [palabra.strip() for palabra in entrada.split(",") if palabra.strip()]
    return palabras

palabras = obtener_palabras()
resultado = filtrar_palabras_anagramas(palabras)
print("Palabras con los mismos caracteres:", resultado)

