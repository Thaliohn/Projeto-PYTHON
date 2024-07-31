def soma():
    numero = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    res = numero + numero2
    print(res)


def sub():
    numero = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    res = numero - numero2
    print(res)


def div():
    numero = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    res = numero / numero2
    print(res)


def mult():
    numero = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    res = numero * numero2
    print(res)

print("Escolha uma das opções: 1 - Soma, 2 - Subtração, 3 - Divisão, 4 - Multiplicação.")
pergunta = int(input("Escolha a opção: "))
if pergunta == 1:
    print("A opção escolhida foi: soma.")
    soma()
elif pergunta == 2:
    print("A opção escolhida foi: subtração.")
    sub()
elif pergunta == 3:
    print("A opção escolhida foi: divisão.")
    div()
elif pergunta == 4:
    print("A opção escolhida foi: multiplicação.")
    mult()
else:
    print("Essa função não está definida!")