import math

## Función Suma: Suma dos valores enteros.
def suma (a, b):
    try:
        numA = int(a)
        numB = int(b)
        return numA + numB
    except(TypeError, ValueError):
        return None

# Función Resta: Resta dos valores enteros.
def resta(a, b):
    try:
        numA = int(a)
        numB = int(b)
        return numA - numB
    except(TypeError, ValueError):
        return None

# Función Cuadrado de un Binomio: Calcula el cuadrado de un binomio (a + b)²
def cuadrado_binomio(a, b):
    try:
        numA = int(a)
        numB = int(b)
        return math.pow(numA, 2) + 2 * numA * numB + math.pow(numB, 2)
    except(TypeError, ValueError):
        return None