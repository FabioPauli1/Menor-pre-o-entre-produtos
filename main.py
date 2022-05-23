prod1 = input('Produto 1: ')
num1 = int(input('Preco: '))
prod2 = input('Produto 2: ')
num2 = int(input('Preco: '))
prod3 = input('Produto 3: ')
num3 = int(input('Preco: '))

list_prod = [prod1, prod2, prod3]
list_prec = [num1, num2, num3]

min_num = None

for num in list_prec:
  if (min_num is None or num<min_num):
    min_num = num

if min_num == num1:
  print(f'Voce deve comprar o {prod1} por ', min_num)

if min_num == num2:
  print(f'Voce deve comprar o {prod2} por ', min_num)

if min_num == num3:
  print(f'Voce deve comprar o {prod3} por ', min_num)