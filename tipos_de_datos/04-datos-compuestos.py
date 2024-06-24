# Las listas pueden ser modificadas
lista = ["Yetlanezi Linares", "Soy Yet", True, 1.65]
print(lista)

# Las tuplas no se pueden modificar y van con parentésis
tupla = ("Yetlanezi Linares", "Soy Yet", True, 1.65)

# Esto es válido (cambia el valor del índice 3)
# lista[3] = "Linares"

# Esto es inválido
# tupla[3] = "Linares"

print(lista[3])


# Creando un conjunto (set) y se cierran con llaves. Su diferencia es que no accede a elementos por índice, no almacena datos duplicados, son datos desordenados.

# Para acceder a los datos de un conjunto se ocupa un bucle.

conjunto = {"Yetlanezi Linares", "Soy Yet", True, 1.65}
# print(conjunto[3])  --> No puede acceder al elemento

# Creando un diccionario (dict) su estrucutra es 'key' : value y separamos por comas.

diccionario = {
    'nombre': "Yetlanezi Linares",
    'sobrenombre': "Yet",
    'estas_emocionada': True,
    'altura': 1.65,
    'dato_duplicado': "Yet",
}

print(diccionario['altura'])
