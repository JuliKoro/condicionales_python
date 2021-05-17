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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra)

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

# Ingreso de datos
texto_1 = input('Ingrese la primera palabra: ')
texto_2 = input('Ingrese la segunda palabra: ')
texto_3 = input('Ingrese la tercera palabra: ')

texto = [texto_1, texto_2, texto_3]

# Menú
print('\nElija la opción que desee:')
print('1 - Ordenar por orden alfabético.')
print('2 - Ordenar por cantidad de letras.\n')
menu = int(input())

# Ordenado alfabético
if menu == 1:
    for x in [0, 2, 3]:
        if texto[0] > texto[1]:
            if texto [1] < texto[2]:
                temp = texto[1] # Variable temporal
                texto[1] = texto[2] # Intercambio de posiciones
                texto[2] = temp # Rescato dato del temporal
        else:
            temp = texto[0]
            texto[0] = texto[1]
            texto[1] = temp 
    print('Palabras ordenadas alfabéticamente: ', texto)

# Ordenado por longitud
elif menu == 2:
   for x in [0, 2, 3]:
        if len(texto[0]) > len(texto[1]):
            if len(texto [1]) < len(texto[2]):
                temp = texto[1] 
                texto[1] = texto[2]
                texto[2] = temp
        else:
            temp = texto[0]
            texto[0] = texto[1]
            texto[1] = temp 
   print('Palabras ordenadas por longitud: ', texto)

else:
    print('\nError de menú.')