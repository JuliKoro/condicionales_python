# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2: 
    print(f'{numero_1} es mayor a {numero_2}')
elif numero_2 > numero_1:
    print(f'{numero_2} es mayor a {numero_1}')
else:
    print(f'{numero_1} y {numero_2} son iguales')

# Verifique si el numero_1 es positivo, negativo o cero
# Imprima el resultado en cada caso

if numero_1 > 0:
    print(f'{numero_1} es un número positivo.')
elif numero_1 < 0:
    print(f'{numero_1} es un número negativo.')
else:
    print(f'{numero_1} es cero.')

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if 0 < numero_1 < 100:
    print(f'{numero_1} está incluido en el interbalo abierto entre 0 y 100.')
else:
    print(f'{numero_1} está fuera del interbalo abierto entre 0 y 100.')

# Verifique si el numero_1 es menor a 10 o el numero_2 es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if numero_1 < 10 or numero_2 > -2:
    print(f'{numero_1} es menor a 10 o {numero_2} es mayor a -2.')
else:
    print(f'{numero_1} no es menor a 10 ni {numero_2} es mayor a -2.')