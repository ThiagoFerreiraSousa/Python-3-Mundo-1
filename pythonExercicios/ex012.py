preco = float(input('Digite o preço do produto R$ '))
desconto = preco - (preco * 5 / 100)
print('O produto custava R${:.2f} reais, na promoção com desonto de 5% vai custar R${:.2f} reais, voce economizou R${} reais'.format(preco, desconto, preco - desconto))
