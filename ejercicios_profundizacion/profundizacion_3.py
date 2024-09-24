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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# Ingreso de datos
temp_1 = float(input('Ingrese temperatura nro. 1: '))
temp_2 = float(input('Ingrese temperatura nro. 2: '))
temp_3 = float(input('Ingrese temperatura nro. 3: '))

# Evaluación temperaturas
if temp_1 > temp_2 and temp_1 > temp_3:
    print(f'{temp_1}°C es la temperatura más alta.')
    if temp_2 < temp_3:
        print(f'{temp_2}°C es la temperatura más baja.')
    else:
        print(f'{temp_3}°C es la temperatura más baja.')
elif temp_2 > temp_1 and temp_2 > temp_3:
    print(f'{temp_2}°C es la temperatura más alta.')
    if temp_1 < temp_3:
        print(f'{temp_1}°C es la temperatura más baja.')
    else:
        print(f'{temp_3}°C es la temperatura más baja.')
elif temp_3 > temp_1 and temp_3 > temp_1:
    print(f'{temp_3}°C es la temperatura más alta.')
    if temp_2 < temp_1:
        print(f'{temp_2}°C es la temperatura más baja.')
    else:
        print(f'{temp_1}°C es la temperatura más baja.')

# Cálculo promedio
promedio = (temp_1 + temp_2 + temp_3) / 3
print(f'Promedio de la temperatura: {promedio}°C')