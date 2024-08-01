# Criar uma lista com 5 países e suas capitais, input país, se o país tiver na lista imprmir o pais e a capital

paises = {
    'Brasil': 'Brasilia',
    'Mexico': 'Ciudad de mexico',
    'Estados Unidos': 'Washington',
    'Canada': 'Ottawa',
    'Australia': 'Camberra'
}

pergunta = input("Digite o nome de um país\n").title()

if pergunta in paises:
    print(f'O pais escolhido é {pergunta}, e sua capital {paises[pergunta]}.')
else:
    print('Não temos dados desse país.')