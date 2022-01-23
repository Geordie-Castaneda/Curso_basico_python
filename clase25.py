def run():
    numero = int(input("Ingrese un numero, por favor : "))
    
    x = 0
    
    while x < numero:
        if x % 2 != 0:
            print(x)
            x+=1
            continue
        x+=1
        

if __name__ == '__main__':
    run()