# Desafio com 'Sets'

'''Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = Funcionários que não tem carro
'''

funcionarios = ['Pedro', 'Mateus', 'João', 'José', 'Sofia', 'Bruno', 'Melissa', 'Ana', 'Marcos', 'Alice']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sofia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


lista1 = set(tem_carro).intersection(turno_dia)
print(lista1)

lista2 = set(tem_carro).intersection(turno_noite)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
