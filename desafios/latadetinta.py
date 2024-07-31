# Crie um programa que leia: Rendimento da tinta, Largura e Altura da parede a ser pintada.
rendimento_da_tinta = float(input("Digite aqui o rendimento da tinta por metro quadrado: "))
largura = int(input("Digite aqui a largura da parede a ser pintada: "))
altura = int(input("Digite aqui a altura da parede a ser pintada: "))
def calcular_tinta():
    metro_quadrado = largura * altura
    tinta = metro_quadrado / rendimento_da_tinta
    print(f"Você precisa de {tinta} latas de tinta.")

calcular_tinta()