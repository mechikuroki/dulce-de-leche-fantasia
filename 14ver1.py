usuarios = ["ídolo", "máquina", "capo", "admin", "pepe"]

if usuarios == []:
    print("¡Necesitamos encontrar algunos usuarios!")
for i in usuarios:
    if i != "admin":
        print(f"Hola {i}, gracias por volver a iniciar sesión.")
    else:
        print("Hola admin, ¿querés ver un informe de estado?")

