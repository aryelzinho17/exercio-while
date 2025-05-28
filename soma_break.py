#o break interrompe o loop

soma = 0

while True:
    x = int(input('digite um numero para ser somado: \n ou \n 0 para sair: '))
    if x == 0:
        break
    soma += x
    print(f'a soma dos numeros digitados e {soma}')