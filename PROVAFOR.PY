print('Insira dois números inteiros, representando o início e o fim do intervalo. Serão somados somente os números pares!!!')
soma = 0

num1 = int(input('Digite o número inicial: '))
num2 = int(input('Digite o número final: '))

par = False

for i in range(num1,num2+1):
    if i % 2 == 0:
        soma+=i
        par = True
        print('A soma dos números pares é:', soma)
else:
    if par:
        print('A soma dos números pares é:', soma)
    else:
        print('Não tem números pares no intervalo inserido.')