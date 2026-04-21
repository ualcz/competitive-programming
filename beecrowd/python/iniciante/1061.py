dia_inicio = int(input().split()[1])
hora_inicio ,minuto_inicio, segundo_inicio=map(int, input().split(" : "))
dia_fim= int(input().split()[1])
hora_fim ,minuto_fim, segundo_fim=map(int, input().split(" : "))

print(((dia_fim-dia_inicio)*24*3600 + (hora_fim-hora_inicio)*3600 + (minuto_fim-minuto_inicio)*60 + (segundo_fim-segundo_inicio))//(24*3600), "dia(s)")
print(((dia_fim-dia_inicio)*24*3600 + (hora_fim-hora_inicio)*3600 + (minuto_fim-minuto_inicio)*60 + (segundo_fim-segundo_inicio))%(24*3600)//3600, "hora(s)")
print((((dia_fim-dia_inicio)*24*3600 + (hora_fim-hora_inicio)*3600 + (minuto_fim-minuto_inicio)*60 + (segundo_fim-segundo_inicio))%(24*3600)%3600)//60, "minuto(s)")
print((((dia_fim-dia_inicio)*24*3600 + (hora_fim-hora_inicio)*3600 + (minuto_fim-minuto_inicio)*60 + (segundo_fim-segundo_inicio))%(24*3600)%3600)%60, "segundo(s)")