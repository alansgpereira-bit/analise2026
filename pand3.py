import pandas as pd

dados = {
    "cargos": ["assistente","analista", "gerente","diretor"],
    "salarios": [1000, 2000, 3000, 4000]}
dados_bi = pd.DataFrame(dados)
print(dados_bi)
dados_bi.to_csv("salarios_cargos.csv" , index=False , encoding="utf-8")