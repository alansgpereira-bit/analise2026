def imc(x, y):
    return x / (y*y)

p = float(input("Digite seu peso: "))
a = float(input("Digite a sua altura: "))
i = imc(p, a)
print(f"Seu Imc é  {i:.2f}")

