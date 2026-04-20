sentence=input()
contador=0
resultado=''
espaco=' '
for letra in sentence:
    if letra==espaco:
        resultado+=letra
    else:
        contador+=1
        if contador%2==0:
            resultado+=letra.lower()
        else:
            resultado+=letra.upper()

print(resultado)
