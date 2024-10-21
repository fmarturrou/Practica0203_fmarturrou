guardada = "password"
contraseña = str(input("Escribe una de tus contraseñas\n"))
if contraseña.lower() == guardada.lower():
    print("La contraseña introducida es correcta")
elif contraseña != guardada:
    print("La contraseña introducida no es correcta")