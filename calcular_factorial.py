#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Para simpleza de la entrada, todas las formas que veremos,
# las probaremos calculando el factorial del número 6,
# Obviamente el procedimiento será el mismo para cualquier número.

numACalcular = 6

# Haciendolo de forma "sucia"
print("Calculo de forma sucia: {}".format(6 * 5 * 4 * 3 * 2 * 1))


# Utilizando la función "built-in" de Python
# Lo principal en este caso es importar la librería.
from math import factorial
print(u"Calculo utilizando función built-in: {}".format(factorial(numACalcular)))

# Utilizando una versión "nuestra" que trabaja con un "while loop"
def fact_while(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

print("Calculo utilizando while: {}".format(fact_while(numACalcular)))

# Utilizando recursividad
# Para este ejemplo es necesario entender como funciona la recursividad.
def fact_recursividad(n):
    if n > 1:
        return n * fact_recursividad(n - 1)
    else:
        return 1

print("Calculo utilizando recursividad: {}".format(fact_recursividad(numACalcular)))

# Utilizando recursividad y valiendonos del operador ternario :D
# Esta únicamente es una versión (mejorada?) de la versión anterior.
def fact_ternario(n):
    return n * fact_ternario(n - 1) if n > 1 else 1

print("Calculo utilizando recursividad y el operador ternario: {}".format(fact_ternario(numACalcular)))