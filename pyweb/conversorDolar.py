cotacao = float(input("Digite o valor da cotacao atual: "))
valorEmDolar = float(input("Digite o valor que deseja converter para real: "))

def converterDolarParaReal(cotacao, valorEmDolar):
    return cotacao * valorEmDolar

valorEmReal = converterDolarParaReal(cotacao, valorEmDolar)

print(f"${valorEmDolar} equivale a R${valorEmReal}")