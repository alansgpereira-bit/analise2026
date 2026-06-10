def ir(x):
    return x * 0.275

s = float(input("Digite seu salário: "))
y = ir(s)
print(f"Seu desconto de imposto de renda é: {y:.2f}")