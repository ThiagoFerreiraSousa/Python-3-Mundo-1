l = float(input('Largura da parede '))
a = float(input('Altura da parede '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(l, a, area))
print('Para pintar esta parede você vai precisar de {}l de tinta'.format(tinta))
