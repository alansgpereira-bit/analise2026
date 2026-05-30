dia = input(" Digite o dia da semana ").lower()
hora = float(input("Digite o horário "))
dif = 21 - hora
if dia == "sexta" and hora == 21:
    print("Sextou!Você merece um chopp")
elif dia == "sexta" and hora == 22:
    print("Sextou! Você merece pelo menos 2 chopps")    
elif dia == "sexta" and hora <= 21:
    print(f"Ainda não sextou! Ainda falta {dif} horas. Não saia da rotina e vá estudar.")   
else:
    print(f"Espere sexta")
 

