import random, math
nameslist = ["Juli", "Caro", "Nuria"]
def message(name):
    print(f"eu {name}, querés ir a cenar?")

for i in range(len(nameslist)):
    message(nameslist[i])

num = random.randint(0, 2)
print(f"{nameslist[num]} no puede venir")
nameslist[num] = "Trini"
print(f"ahora viene {nameslist[num]}")
message(nameslist[num])

nameslist.insert(0, "Ashton")
message(nameslist[0])
nameslist.insert(math.ceil(len(nameslist)/2), "Tomi")
message(nameslist[math.ceil(len(nameslist)/2)])
nameslist.append("Emi")
message(nameslist[-1])

for _ in range(len(nameslist) - 2):
    num = random.randint(0, len(nameslist) -1)
    print(f"{nameslist[num]} no entra!") 
    nameslist.pop(num)
print(f"Vienen {len(nameslist)} personas")
