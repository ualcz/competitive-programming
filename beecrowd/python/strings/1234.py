while True:
    try:
        sentence = input()
        if not sentence and sentence != "": 
            break

        contador = 0
        resultado = ''
        
        for letra in sentence:
            if letra == ' ':
                resultado += letra
            else:
                contador += 1
                if contador % 2 == 0:
                    resultado += letra.lower()
                else:
                    resultado += letra.upper()

        print(resultado)
        
    except EOFError:
        break