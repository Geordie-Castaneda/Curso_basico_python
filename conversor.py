quetzales = input("¿Cuantos quetzales tienes?: ")
quetzales = float(quetzales)
dolares = 7.72
conversion = quetzales / dolares
conversion = round(conversion,2)
print("Su cantidad en dolares es: $"+str(conversion)+" dólares")
print("")
print("¿Tiene dolares que quiera cambiar a quetzales?")
print("1. SI")
print("2. NO")
decision = input("Ingrese un digito: ")
decision = int(decision)
if decision == 1:
    dolares_reales = input("¿Cuantos dólares tienes?: ")
    dolares_reales = float(dolares_reales)
    valor_quetzal = 0.13
    conversion = dolares_reales / valor_quetzal
    conversion = round(conversion,2)
    print("Su cantidad en quetzales es: Q"+str(conversion)+" quetzales")
else:
    print("Gracias por utilizar nuestro sercivio de conversión :D")