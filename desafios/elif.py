# Calculadora de IMC

# Pegue a entrada de um usuário e faça o cálculo de IMC

tamanho_cm = int(input("Digite sua altura em CM: "))
peso_kg = float(input("Digite seu peso aqui: "))
tamanho_mt = tamanho_cm / 100
imc = peso_kg / (tamanho_mt * tamanho_mt)

if imc < 18.5:
    print(f"Seu índice é {imc:.2f} e você está no estágio de MAGREZA")
elif 18.5 < imc < 24.9:
    print(f"Seu índice é {imc:.2f} e você está no estágio de NORMAL")
elif 25.0 < imc < 29.9:
    print(f"Seu índice é {imc:.2f} e você está no estágio de SOBREPESO")
elif 30.0 < imc < 39.9:
    print(f"Seu índice é {imc:.2f} e você está no estágio de OBESIDADE")
else:
    print(f"Seu índice é {imc:.2f} e você está no estágio de OBESIDADE GRAVE")