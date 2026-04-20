while True:
    try:
        resutado=""
        ponteiroX=0
        ponteiroY=0
        palavra=input()
        
        if not palavra and palavra != "": 
            break

        for caractere in palavra:
            if caractere == '_':
                if ponteiroX==1:
                    resutado+='</i>'
                    ponteiroX=0
                else:
                    resutado+='<i>'
                    ponteiroX=1

            elif caractere == '*':
                if ponteiroY==1:
                    resutado+='</b>'
                    ponteiroY=0
                else:
                    resutado+='<b>'
                    ponteiroY=1
            else:
                resutado+=caractere

        print(resutado)
    except EOFError:
        break