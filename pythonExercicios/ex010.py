real = float(input('Quanto você tem na carteira? '))
dolar = real / 3.27
print('Você tem R${} reais e pode comprar US${:.2f} dólares'.format(real, dolar))
