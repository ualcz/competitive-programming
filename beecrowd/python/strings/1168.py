casos=int(input())

for i in range(casos):
    qtd=0
    palavra=input()
    for numero in palavra:
        match int(numero):
            case 0:
                qtd+=6
            case 1:
                qtd+=2
            case 2:
                qtd+=5
            case 3:
                qtd+=5
            case 4:
                qtd+=4
            case 5:
                qtd+=5
            case 6:
                qtd+=6
            case 7 :
                qtd+=3 
            case 8:
                qtd+=7
            case 9:
                qtd+=6
    print(f'{qtd} leds')