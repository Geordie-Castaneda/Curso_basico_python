menu = """
    ***Bienvenido a conversor de monedas :D***

    1. Quetazales a dolares
    2. Pesos Colombianos a dolares
    3. Pesos Argentinos a dolares

"""
input(menu)
opcion = int(input("Ingresa una opción: "))

if opcion == 1:
    quetzales = float(input("¿Cuantos quetzales tienes? Q"))
    valor_dolar = 7.72
    total = quetzales/valor_dolar
    total=round(total,2)
    input("Tienes $"+str(total)+" dólares")
elif opcion == 2:
    pesos_colombianos = float(input("Cuantos pesos colombianos tienes? $ "))
    valor_dolar = 4065.33
    total = pesos_colombianos/valor_dolar
    total=round(total,2)
    input("Tienes $"+str(total)+" dólares")
elif opcion == 3:
    pesos_argentinos = float(input("Cuantos pesos argentinos tienes? $ "))
    valor_dolar = 102.69
    total = pesos_argentinos / valor_dolar
    total= round(total,2)
    input("Tienes $"+str(total)+" dólares")
else:
    input("Elige un opción correcta por favor :D")