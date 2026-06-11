def apto(i, g):
    if i >= 18 and g == "MASCULINO":
        print("apto a se alistar")
    else:
        print("não apto")   

idade = int(input("Digite sua idade: "))
gen = input("Digite o seu gênero: ").upper() 

apt = apto(idade, gen)