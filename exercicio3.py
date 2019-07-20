import random

n = []
impar = []
par = []

i = 0

while i <= 10:
    n.append(random.randrange(1,100))
    i+=1

print(f'Essa é a lista: {n}' ) 

# def pares (n):
#     while i % 2 == 0
# //range(0,len(n)-1):
# print(f'Esses são os numeros pares: {n}') 

for i in n:
    if i % 2 == 0:
        par.append(i)                
    elif i % 2 != 0:
        impar.append(i)
        
print(f'Esses são os numeros pares: {par}')
print(f'Esses são os numeros impares: {impar}')
        