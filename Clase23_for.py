def run():
    for i in range(11):
        print(str(i) + " * 11"+" = "+str((i*11)))

    lineas =16
    for numero_linea in range(lineas): 
        espacios = lineas - numero_linea - 1 
        asteriscos = 1 + numero_linea * 2
        print (" " * espacios + "*" * asteriscos)

    for i in range(15):
        print("*" * i)

    
    n_valor = 16
    print("")
    for i in range(16):
        print("*"*(n_valor-i))

        
if __name__ == '__main__':
    run()