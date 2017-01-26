print ("Estas son las tablas de multiplicar")
print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for i in range(1,11):
    print(" ")
    print("Tabla del " + str(i))
    print("====================")
    for j in range(1,11):
        print(str(i) + " por " + str(j) + " es " + str(i*j))
