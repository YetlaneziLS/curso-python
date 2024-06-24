# Variable se declara = su valor
# Las variables pueden ser modificadas
nombre = "Yetlanezi"
print(nombre)

nombre = "Linares"  # Esto redefine la variable
numero = 40 + 20

print(nombre)  # Imprime el valor de la segunda línea de la variable nombre
print(numero)  # Imprime el resultado de la variable numero

# Definiendo una variable con camelCase
nombreCompleto = "Yetlanezi Linares"

# Definiendo una variable con snake_case
nombre_completo = "Yetlanezi Linares"

# Concatenar con +
bienvenida = "Hola" + "¿Cómo estas?"

# Concatenar con f-strings
bienvenida = f"Hola {nombre_completo} ¿Cómo estas?"

# Operadores de pertenencia (in/not in)
print("Yetlanezi" in bienvenida)  # Esto arroja True
print("Yetlanezi" not in bienvenida)  # Esto arroja False
