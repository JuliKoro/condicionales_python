# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# Verifique cual cual de los dos textos es mayor alfabéticamente
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('"{}" es mayor alfabéticamente que "{}".'.format(texto_1, texto_2))
elif texto_1 < texto_2:
    print('"{}" es mayor alfabéticamente que "{}".'.format(texto_2, texto_1))
else:
    print('"{}" es igual que "{}".'.format(texto_1, texto_2))

# Transforma esas variables tipo texto y almacénalas
# en nuevas variables númericas (int)
# Repita el proceso, ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

num_1 = int(texto_1)
num_2 = int(texto_2)

if num_1 > num_2:
    print('El número {} es mayor que el número {}.'.format(num_1, num_2))
elif num_1 < num_2:
    print('El número {} es mayor que el número {}.'.format(num_2, num_1))
else:
    print('El número {} es igual que el número {}.'.format(num_1, num_2))

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

# Respuesta: Esto se debe a que cada caracter tiene un valor numérico asociado
# al Código ASCII, y en éste tanto los números como el alfabeto están ordenados.
