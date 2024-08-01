# Ler idade, se idade for menor que 13 imprimir você é uma criança, se estiver entre 13 e 19 imprimir você é um adolescente
# Se for maior ou igual a 20 imprimir você é um adulto

idade = int(input("Informe sua idade: "))
if idade < 13:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 19:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")