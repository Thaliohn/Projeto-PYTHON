from random import randint

chute_maquina = randint(1,51)
acertou = False
while acertou == False:
    chute_pessoa = int(input("Escolha um número de 1 a 50.\n"))
    if chute_pessoa == chute_maquina:
        print("Parabéns você acertou.")
    elif chute_pessoa < chute_maquina:
        print("Você chutou muito baixo.")
    elif chute_pessoa > chute_maquina:
        print("Você chutou muito alto.")
    else:
        print("Você nem sequer tentou.")