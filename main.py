"""

Calculadora para compras em mercado! # Sem interface gráfica, por enquanto :)

"""


resposta = 's'
soma = 0.0
total = 0.0

while resposta == 's':  # Repete até que o usuário digite [n] em resposta!
    operador = input('[+] para Somar [-] para Subtrair: ')
    preco = input('Qual preço do produto? ')
    try:  # tenta converter a string em um float
        preco = float(preco)
    except ValueError:  # Se der erro o programa para
        print('O programa parou, digite preços!')
        break
    quantidade = input('Quantas vezes? ')
    if quantidade.isdigit():  # verifica se o quantidade é um digito/número
        quantidade = int(quantidade)
        if operador == '+':  # condicional de soma
            total += preco * quantidade
            print(f'{preco * quantidade} adicionado ao Total')
        if operador == '-':  # condicional de subtração
            total -= preco * quantidade
            print(f'{preco * quantidade} subtraido do Total')
    else:
        print('Digite números')
    print(f'Seu total até agora é {total} R$')
    resposta = input(f'Deseja continuar? [s] para continuar [n] para sair ')
else:
    print(f'O total da suas compras é de {total} R$')
