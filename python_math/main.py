# Escrever um programa python que gere dois números aleatórios e solicite a resposta ao usuário

from random import randint

while True:
    numero_maquina_um = randint(0, 1000)
    numero_maquina_dois = randint(0, 1000)
    resposta_maquina = numero_maquina_um + numero_maquina_dois

    print("Qual a soma desses dois números?")
    print(f'{numero_maquina_um} + {numero_maquina_dois}')
    input_usuario = input("Resposta: (Tecle Q caso queira sair.) ")

    if input_usuario.upper() == 'Q':
        print("Você saiu do jogo.")
        break

    try:
        input_usuario = int(resposta_maquina)
        if input_usuario == resposta_maquina:
            print("Você acertou!")
        else:
            print(f"Você errou, a resposta era {resposta_maquina}")
    except ValueError:
        print("Insira um número ou digite Q para sair.")