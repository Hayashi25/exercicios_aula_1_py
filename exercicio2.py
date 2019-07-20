import random

n = []
i = 1

while i <= 20:
    n.append(random.randrange(1,100))
    i+=1

print(f'Essa é a lista: {n}' ) 

def maior_numero(n):
    return max(n , key=int)

print(f'esse é o maior numero da lista: {maior_numero(n)}' )