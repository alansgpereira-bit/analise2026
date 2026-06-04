senha_correta = "python123"
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    tentativas = input(F"Digite a senha (tentativa {tentativas + 1}/{max_tentativas}):")
    if tentativas == senha_correta:
        print("Acesso concedido! Bem-vindo")
        break
    else:
        print("Senha incorreta")  
        tentativas += 1 
else:("Você excede o número máximo de tentativas")         
