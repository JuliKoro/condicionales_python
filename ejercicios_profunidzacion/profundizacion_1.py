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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# Ingreso de datos
num_1 = int(input('Ingrese un número:\n'))
num_2 = int(input('Ingrese otro número:\n'))

resta = num_1 - num_2
print('La diferencia entre {} y {} es {}'.format(num_1, num_2, resta))

if resta > 0:
    print('El resultado {} es positivo.'.format(resta))
elif resta < 0:
    print('El resultado {} es negativo.'.format(resta))
else:
    print('El resultado {} es nulo (cero).'.format(resta))