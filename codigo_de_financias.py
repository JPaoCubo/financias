#agora vou fazer usando pandas

import pandas as pd

categoria1=input("digite a categoria: ")
valor1=input("digite o valor: ")
categoria2=input("digite a categoria: ")
valor2=input("digite o valor: ")

despesas={
    "categoria":[categoria1,categoria2],
    "valor":[valor1,valor2]
}

df = pd.DataFrame(despesas)

print(df)

df.to_excel('meu_controle.xlsx', index=False)