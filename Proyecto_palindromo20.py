def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindrome = palindromo(palabra)
    if es_palindrome == True:
        print("Si es palindromo")
    else:
        print("No es palindromo :C")


if __name__ =='__main__':
    run()