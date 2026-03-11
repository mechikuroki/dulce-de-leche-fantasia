edad = int(input("escriba edad: "))

if edad < 2:
    print("sos un bebé")
elif edad < 4:    
    print("sos un nene chiquito")
elif edad < 13:
    print("sos un nene")
elif edad < 20:
    print("sos un adolescente")
elif edad < 65:
    print("sos un adulto")
else:
    print("sos un adulto mayor")

