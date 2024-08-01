# Criar um script para calcular o fatorial

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)
    
pergunta = int(input("Digite um número: "))
print(f'O fatorial de {pergunta} é igual a: {fatorial(pergunta)}.')