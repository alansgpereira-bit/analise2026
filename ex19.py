cargo = input("Digite o seu cargo ").lower()
if cargo == "caixa":
    sal = 1500 
    #print(f"{sal}")
elif cargo == "vendedor":  
    sal = 2400
   # print(f"{sal}")
elif cargo == "gerente":      
    sal = 4000
    #print(f"{sal}")
else:
    sal = 0
    print("Não trabalha aqui")
# bloco de cálculo de inss
inss = sal * 0.12
print(f"{inss}")
# bloco de cálculo de irrf
if sal > 2000:
    irrf = sal * 0.14
else:
    irrf = sal * 0.08   
print(f"{irrf}")
# bloco de cálculo final
salfim = sal - inss - irrf
print(f"{salfim}")
#bloco de impressão
print(f"{sal}")
print(f"{inss}")
print(f"{irrf}")