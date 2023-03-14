from time import sleep
first_value = int(input('Primeiro valor: '))
second_value = int(input('Segundo valor: '))
option = 0
while option != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    option = int(input('Qual é a sua opçao? '))
    if option == 1:
        sum = first_value + second_value
        print('\33[1;36mA soma entre {} e {} é {}\33[m'.format(first_value, second_value, sum))
    elif option == 2:
        multiplication = first_value * second_value
        print('\33[1;36mO resultado de {} x {} é igual a {}\33[m'.format(first_value, second_value, multiplication))
    elif option == 3:
        if first_value > second_value:
            bigger = first_value
        else:
            bigger = second_value
        print('\33[1;36mEntre {} e {} o maior é {}\33[m'.format(first_value, second_value, bigger))
    elif option == 4:
        print('\33[1;36mInforme os números novamente:\33[m ')
        first_value = int(input('Primeiro valor: '))
        second_value = int(input('Segundo valor: '))
    elif option == 5:
        print('\33[1;36mFinalizando...\33[m')
    else:
        print('\33[1;36mOpção inválida. Tente novamente\33[m')
    print('=-='*10)
    sleep(2)
print('\33[1;36mFim do programa! Volte sempre!\33[m ')