a,b,c,d=map(float,input().split())

media=(a*2+b*3+c*4+d*1)/10

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
else:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame=float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final=(media+exame)/2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")