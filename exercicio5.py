import math
raio = input ('Digite o raio da sua circunferencia: ')
math.pi = float(math.pi)
raio = float(raio)

area = ((math.pi)*(raio**2))

print(f'Essa é a area da sua circunferencia {area:.2f}')
    
comprimento = ((2)*(math.pi)*(raio))

print(f'Esse é o comprimento da sua circunferencia {comprimento:.2f}')