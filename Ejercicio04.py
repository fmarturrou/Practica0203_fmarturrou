edad = int(input("¿Cúal es tu edad?\n"))    
ingresos = int(input("¿Cúal es tu salario bruto mensual?\n"))
if edad >= 16 and ingresos >= 1000:
     print("Según los datos introducidos, debes tributar.")
else:
     print("No tienes la edad mínima para trabajar por lo que no puedes tributar.")