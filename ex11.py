num1 = float(input("digite o ano do seu nascimento "))
num2 = float(input("digite o ano atual "))
idade = num2 - num1
if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade")
else:
      print(f"Você tem {idade} anos e é menor de idade")  