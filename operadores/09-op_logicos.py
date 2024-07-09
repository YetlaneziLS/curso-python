# AND y se expresa con "&" Es un operador lógico que compara uno con otro por lo que con este operador las dos tienen que ser True
resultado1 = True & True # Arrojará un bool True
resultado2 = True & False # Arrojará un bool False
resultado3 = False & True # Arrojará un bool False
resultado4 = False & False # Arrojará un bool False

#OR se expresa con una barra diagonal, con este operador lógico solamente si las dos false arrojará un false, las demás siempre serán True
resultado5 = True | True # Arrojará un bool True
resultado6 = True | False # Arrojará un bool True
resultado7 = False | True # Arrojará un bool True
resultado8 = False | False # Arrojará un bool False

#NOT con este operador lógico se invertirá el resultado
resultado9 = not True # Arrojará un bool False
resultado10 = not False # Arrojará un bool True

print(resultado9)

