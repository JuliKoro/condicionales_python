# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# Ingreso de datos
num_1 = int(input('Ingrese el primer número: '))
num_2 = int(input('Ingrese el segundo número: '))
num_3 = int(input('Ingrese el tercer número: '))

if num_1 % 2 == 0:
    print('El número {} es par.'.format(num_1))
else:
    print('El número {} es impar.'.format(num_1))

if num_2 % 2 == 0:
    print('El número {} es par.'.format(num_2))
else:
    print('El número {} es impar.'.format(num_2))

if num_3 % 2 == 0:
    print('El número {} es par.'.format(num_3))
else:
    print('El número {} es impar.'.format(num_3))