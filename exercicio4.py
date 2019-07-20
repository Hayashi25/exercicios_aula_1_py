import math
a = input('digite a : ')
b = input('digite b : ')
c = input('digite c : ')

print(f'sua equação é : {a}x**2 + {b}x + {c} = 0')

a = float(a)
b = float(b)
c = float(c)

delta = ((b ** 2) - ((4)*(a)*(c)))

print(f'Esse é o seu delta {delta:.2f}')

baskara1 = (( (-1*b) + (delta**(1/2)))/2*a)
baskara2 = (( (-1*b) - (delta**(1/2)))/2*a)

print(f'Esse é o resultado da Baskara sendo o X1 = {baskara1:.2f} e o X2 = {baskara2:.2f}')