# Criar lambda que aceite um número e retorne par ou impar

par_impar = lambda x: 'Par' if x % 2 == 0 else 'Impar'

pergunta = int(input('Digite um número: '))
print(f'O número {pergunta} é {par_impar(pergunta)}.')
