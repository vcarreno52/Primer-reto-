# Primer-reto-
#1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

![Descrpición de la imagen](https://github.com/vcarreno52/Primer-reto-/blob/main/Imagen%20cod%201.png?raw=true)

Explicación: Este código define una función llamada operaciones. Primero pide al usuario que ingrese dos números y la operación que quiere realizar (+, -, *, /). Según la operación que elija, suma, resta, multiplica o divide los números. Al final, devuelve el resultado.

#2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

![Descrpición de la imagen](https://github.com/vcarreno52/Primer-reto-/blob/main/Imagen%20c%C3%B3digo%202.png?raw=true)

Explicación: Este código define una función llamada `palindromo` que verifica si una palabra es un palíndromo. Pide al usuario que ingrese una palabra y luego compara cada letra de la palabra con su correspondiente desde el final. Si encuentra alguna diferencia, devuelve `False`. Si todas las letras coinciden, devuelve `True`.


#3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

![Descrpición de la imagen](https://github.com/vcarreno52/Primer-reto-/blob/main/Imagen%20c%C3%B3digo%203.png?raw=true)

Explicación:Este código define dos funciones. La primera, `es_primo`, verifica si un número es primo: si el número es menor o igual a 1, devuelve `False`; si no, recorre los posibles divisores desde 2 hasta la raíz cuadrada del número. Si encuentra un divisor, devuelve `False`; de lo contrario, devuelve `True`. La segunda función, `numeros`, pide al usuario ingresar varios números separados por comas, los convierte a una lista de enteros, y luego crea una lista con los números que son primos utilizando la función `es_primo`. Finalmente, imprime la lista de números primos encontrados.


#4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

![Descrpición de la imagen](https://github.com/vcarreno52/Primer-reto-/blob/main/Imagen%20c%C3%B3digo%204.png?raw=true)


Explicaión:Este código define tres funciones. La función `numeros` solicita al usuario que ingrese números separados por comas, los convierte en una lista de enteros y la devuelve. La función `sumas` toma una lista de números y devuelve una nueva lista donde cada elemento es la suma de dos números consecutivos de la lista original. Finalmente, la función `mayor_que` recorre una lista de resultados (sumas) y devuelve el valor máximo encontrado en esa lista. Al final, el código ejecuta las tres funciones: solicita los números, calcula las sumas y muestra el resultado de las sumas y el valor máximo de las sumas.


