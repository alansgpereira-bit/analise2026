v1 = float(input( "digite um valor ")) 
v2 = float(input( "digite outro valor ")) 
md = (v1 + v2)/2
if md > 5:
    print(F"Aluno aprovado com média {md}")
else:
    print(f'Aluno em recuperação com média {md}')