# Verificar ponto da carne
ponto_carne = int(input("Digite aqui a temperatura da sua carne em graus celsius.\n"))
if ponto_carne < 48:
    print("Cozinhar mais")
elif ponto_carne in range(48, 54):
    print("Carne selada/selando")
elif ponto_carne in range(54, 60):
    print("Ao ponto para mal passada")
elif ponto_carne in range(60, 65):
    print("Ao ponto")
elif ponto_carne in range(65, 71):
    print("Ao ponto para bem passada")
elif ponto_carne in range(71, 76):
    print("Bem passada/torra")
else:
    print("Sua carne virou carvão")