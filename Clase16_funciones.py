def conversacion (opcion):
    print("Hola")
    print("Como estas? ")
    print("Elegiste la opción "+str(opcion))
    print("Adiós")


opcion = int(input("Elige una opción (1, 2, 3): "))

if opcion == 1:
    conversacion(opcion)
elif opcion == 2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print("Elige una opción correcta por favor :::")