from math import radians, cos, tan, sin
angulo = float(input('Digite o ângulo que você dejesa: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem Seno de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O ângulo de {} tem Cosseno de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {} tem Tangente de {:.2f}'.format(angulo, tan))

