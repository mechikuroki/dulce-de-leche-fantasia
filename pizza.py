pizza = ["Muzzarella", "Salame", "Jamón"]
for i in pizza:
    print(f"Me gusta la pizza de {i}")

pizzastr = "Me gusta la pizza :) que buena comida increible aguante ugis no a la droga si a la pizza"
print(pizzastr)

pizza_amigo = pizza.copy()

pizza.append("Verdura")
pizza_amigo.append("Cebolla")

print("Mis pizzas favoritas son:")
for i in pizza:
    print(i)
print("Las pizzas favoritas de mi amigo son:")
for i in pizza_amigo:
    print(i)
