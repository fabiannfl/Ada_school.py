# Define variables de diferentes tipos de datos
entero = 42
flotante = 3.14
cadena = "Hola, soy una pinche cadena"

# Concatena la cadena con las otras variables aplicando conversión
resultado_concatenacion = cadena + " - Entero: " + \
    str(entero) + ", Flotante: " + str(flotante)

# Imprime el resultado de la concatenación
print("Resultado de la concatenación:", resultado_concatenacion)

# Límites de los enteros en Python
limite_enteros = 2**63 - 1  # El límite superior de enteros en sistemas de 64 bits
print("Límite superior de enteros en Python:", limite_enteros)

# Límites de los flotantes en Python
limite_flotantes = 1.8e308  # Límite superior de flotantes en Python
print("Límite superior de flotantes en Python:", limite_flotantes)

# Pide al usuario que ingrese un número entero n
n = int(input("Ingresa un número entero n: "))

# Calcula la suma de los primeros n números pares
# Utilizamos la división entera para asegurar un resultado entero
suma_pares = (n * (n + 1)) // 2

# Imprime el resultado
print("La suma de los primeros", n, "números pares es:", suma_pares)
