def ingresar_frase():
    while True:
        frase = input("Por favor, ingrese una frase: ")
        if frase==" ":
            print ("Debe ingresar una frase.")
        else:
            return frase

def ingresar_letra():
    while True:
        letra = input("Por favor, ingrese una letra: ")
        if letra.isalpha() and len(letra) == 1:
            return letra.lower()
        else:
            print("Debe ingresar una letra.")

frase = ingresar_frase()
letra = ingresar_letra()