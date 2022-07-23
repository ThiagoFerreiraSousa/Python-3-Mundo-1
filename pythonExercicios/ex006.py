#Crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quadrada;
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
q = n ** (1/2)
print('O numero digitado foi {} \nSeu dobro é {} \nSeu triplo é {} \nSua raiz quadrada é {:.2f}'.format(n, d, t, q))
