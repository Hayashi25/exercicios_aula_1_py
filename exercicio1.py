nome_funcionario = input ('Digite seu nome: ')
horas = input ('Numero de horas trabalhadas: ')
recebe_por_hora = input('valor do salario por hora: ')

calculo_salario = float (horas)*float(recebe_por_hora)

print(f'{nome_funcionario} esse é o seu salario do mês de acorod com seu numero de horas {calculo_salario}')