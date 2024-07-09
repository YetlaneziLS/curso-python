
ingreso_mensual = 10000

if ingreso_mensual > 100000:
    print("Tú ingreso mensual alcanza perfectamente para vivir en cualquier parte del mundo")

elif ingreso_mensual <= 10000:
    print("Tú ingreso mensual alcanza perfectamente para vivir en latinoamérica")

else:
    print("Eres muy pobre")

# Se pueden usar if anidado

mi_ingreso_mensual = 90000
mi_gasto_mensual = 80000

if mi_ingreso_mensual > 10000:
    if mi_ingreso_mensual - mi_gasto_mensual < 0:
        print("Debemos mucho dinero")
    elif mi_ingreso_mensual - mi_gasto_mensual > 3000:
        print("Debemos dejar de gastar en cosas innecesarias")
    else:
        print("Podemos seguir gastando a lo desgraciado") 