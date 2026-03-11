usuarios_actuales = ["ídolo", "máquina", "capo", "admin", "pepe"]
usuarios_nuevos = ["ídolo", "máquina", "Toto Fernández", "Facundo Cambeses", "Ezequiel Cannavo"]
usuarios_actuales_lower = [user.lower() for user in usuarios_actuales]
for i in usuarios_nuevos:
    if i.lower() in usuarios_actuales_lower:
        print(i, "no está disponible")
    else:
        print(i, "está disponible")


