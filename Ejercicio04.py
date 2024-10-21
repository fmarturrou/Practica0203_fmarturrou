edad = int(input("¿Cúal es tu edad?\n"))
if edad < 16:
    print("No tienes la edad mínima para trabajar por lo que no puedes tributar.")
ingresos = int(input("¿Cúal es tu salario bruto mensual?\n"))
if edad >= 16:
    if ingresos >= 1000:
        print("Según los datos introducidos, debes tributar.")
if ingresos < 1000:
    print("No recibes los ingresos mínimos para tributar")