# if True:
# La acción se ejecuta

# if False:
# La acción no se ejecuta

edad = 17

if edad >= 18:
    print("Puedes pasar")
    print("Forma parte del if")
else:
    print("No puedes pasar")
    print("Este bloque de código forma parte del else")

print("No forma parte de ninguna condición")


contraseña_almacenada = "CursoPython"
constraseña_escrita = '''CursoPython'''

if contraseña_almacenada == constraseña_escrita:
    print("INICIANDO SESIÓN...")
else:
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")
