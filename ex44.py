def soma(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multi(a,b):
    return a * b
def divi(a,b):
    return a / b
#else:
   # print("Valor inválido")

escolha = ""
while escolha != "0":
    escolha = input("digite uma opção: 1-somar, 2-subtrair, 3-multiplicar, 4-dividir ")
    num1 = int(input("digite o primeiro número "))
    num2 = int(input("digite o segundo número "))
    if escolha == "1":
        x = soma(num1,num2)
    elif escolha == "2":
        x = subtrair(num1,num2)
    elif escolha =="3":
        x = multi(num1,num2)
    elif escolha == "4" :
        x = div(num1,num2)
    print(f"O resultado da operação é {x}")    
else:
    print("operação terminada")    





