while True:
        N=int(input())
        resutado=0
        if N == 0:
            break
        for i in range(1,(N)+1):
            resutado+=i**2
        print(resutado)
