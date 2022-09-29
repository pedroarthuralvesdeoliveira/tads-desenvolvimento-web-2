peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
quadrado = 2

def calcularIMC(peso, altura):
    return peso / (altura**quadrado)

imc = calcularIMC(peso, altura)
print(f"O teu imc e: {imc}")