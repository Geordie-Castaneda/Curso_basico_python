def conversor(tipo_moneda, valor_dolar):
    moneda_nacional = float(input("Cuantos "+tipo_moneda+" tienes? :"))
    dolares = float(moneda_nacional / valor_dolar)
    dolares = round(dolares,2)
    print("Tienes $"+str(dolares)+" dólares")
    
menu = """
    ***Bienvenido a conversor de monedas :D***

    1. Quetazales a dolares
    2. Pesos Colombianos a dolares
    3. Pesos Argentinos a dolares

"""
input(menu)
opcion = int(input("Ingresa una opción: "))

if opcion == 1:
    conversor("quetzales", 7.72)
elif opcion == 2:
    conversor("pesos colombianos", 4065.33)
elif opcion == 3:
    conversor("pesos argentinos", 102.69)
else:
    input("Elige una opción correcta amigo :C")