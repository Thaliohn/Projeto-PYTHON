# Um novo index é criado quando uma lista dentro de outra é criada. - EXERCÍCIO
'''items = [['i1', 'i2'], ['i3', 'i4']]
#             0      1,      0     1
#             0              1
print(items[0][1])
'''

#Crie um programa que leia quanto de dinheiro a pessoa tem e quantos doláres ela pode comprar, U$ 5,50 - CONCLUÍDO

'''carteira = int(input("Digite a quantia disponível na sua carteira: "))
dolar = carteira / 5.5
print(f'A quantia de dólar que você poderá comprar seria: U${dolar:.2f}')'''

#Crie um programa que dê desconto - CONCLUÍDO
'''valor_produto = int(input("Qual o valor do produto desejado?\n "))
desconto_produto = valor_produto - (valor_produto * (15/100))
print(f'O valor do produto é {valor_produto}, seu valor juntamente com um desconto seria {desconto_produto}.')'''

#Crie um programa que leia o salário de algúem e dê um aumento de 15%. - CONCLUÍDO
'''salario_atual = int(input("Qual seu salário atual?\n"))
print('Você está apto a receber um aumento salarial.')
aumento_salario = salario_atual + (salario_atual * 15/100)
print(f'Seu salário a partir de agora será de: {aumento_salario}')'''

#Crie um programa para transformar temperaturas Celsius em Fahrenheit. - CONCLUÍDO
'''temp_celsius = float(input('Qual a temperatura atual em Cº?\n'))
temp_fahrenheit = (temp_celsius * 1.8) + 32
print(f'A temperatura em Celsius(Cº) é {temp_celsius}, a temperatura convertida a Fahrenheit(Fº) é {temp_fahrenheit:.2f}.')'''

# R$60 ao dia, R$0,15 por KM - CONCLUÍDO
'''dias_usados = int(input('Digite aqui quantos dias você andou com o carro: '))
dias_preco = dias_usados * 60
km_rodados = float(input('Digite aqui os km rodados: '))
km_preco = km_rodados * 0.15
total = dias_preco + km_preco
print(f'Os dias rodados foram {dias_usados}, totalizando {dias_preco}, os KM rodados foram {km_rodados}, totalizando {km_preco}, o total é {total}.')'''

# Seno, Cosseno e Tangente. - CONCLUÍDO
'''from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'o Seno é {seno:.2f}, o Cosseno é {cosseno:.2f}, a Tangente é {tangente:.2f}.')'''

# Catetos e Hipotenusa. - CONCLUÍDO
'''from math import hypot
cateto_oposto = float(input('Digite o tamanho do cateto oposto: '))
cateto_adjacente = float(input('Digite o tamanho do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'Hipotenusa: {hipotenusa:.2f}')'''