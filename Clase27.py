import random

def run():
    numero_aleatorio = random.randint(1,100)

    numero = int(input('Ingresa un numero: '))

    while numero != numero_aleatorio:
        if numero > numero_aleatorio:
            print('Ingresa un numero más pequeño')
        else:
            print('Ingresa un numero más grande')
        numero=int(input('Ingresa un numero: '))
    
    print('Has adivinado el numero :D '+str(numero_aleatorio))
    


if __name__ == '__main__':
    run()