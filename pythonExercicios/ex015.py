dias = int(input('Quantidade de dias '))
km = float(input('Digite a quantidade de quilômetros percorrida '))
preco = dias * 60.00 + km * 0.15
print('O valor a pagar será de R${:.2f} reais'.format(preco))
