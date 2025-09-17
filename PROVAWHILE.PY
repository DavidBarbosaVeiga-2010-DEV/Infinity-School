numero = 7
limite_tentativas = 3
tentativas = 0
print('Bem-vindo ao jogo de adivinhação!!!')
print(f"Tente adivinhar o número secreto entre 1 e 10. Você tem {limite_tentativas} tentativas.")
while limite_tentativas > tentativas:
    palpite = int(input('Digite seu palpite: '))
    tentativas += 1

    if palpite == numero:
        print('Muito bem! Você acertou!')
        break
    else:
        print('Você quase consegue, tente novamente!')