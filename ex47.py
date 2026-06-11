def imc(p, a):
   x=  p / (a*a)
   if x < 18.5:
    print("Magreza")
   elif x >=18.5 and x <= 24.9 :
    print("Normal")
   elif x >= 25 and x <= 29.9 :
    print("Sobrepeso")
   elif x >= 30 and x <= 34.9 :
    print("Obesidade grau I")
   elif x >= 35 and x <= 39.9 : 
    print("Obesidade grau II")
   elif x >= 40  : 
    print("Obesidade grau III")
peso = float(input(" Digite o seu peso: "))
altura = float(input("Digite a sua altura"))
y = imc(peso, altura)