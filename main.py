while True:
    lang = input('\nEN-US: Select a language \n'
                 'PT-BR: Selecione o idioma \n'
                 '[PT]-BR - PORTUGUESE BRAZIL | '
                 '[EN]-US - AMERICAN ENGLISH \n'
                 '>>> ')


    if lang == 'PT':
        print()
        num1 = float(input('Digite um numero: '))
        num2 = float(input('Digite um numero: '))
        ope = input('Digite o operador: ')


        if ope == "+":
            print(num1 + num2)
        elif ope == '-':
            print(num1 - num2)
        elif ope == '*':
            print(num1 * num2)
        elif ope == '/':
            print(num1 / num2)
        else:
            print('Não e operador, insira outro')
            continue

        sair = input('\nDeseja sair? [S]im ou [N]ão: ')
        if sair == 'S':
            print('OBRIGADO POR USAR MINHA CALCULADORA!!!')
            break
        elif sair == 'N':
            continue

    elif lang == 'EN':
        print()
        num1 = float(input('EN-US: Type a number: '))
        num2 = float(input('EN-US: Type a number: '))
        ope = input('EN-US: Type an operator: ')

        if ope == "+":
            print(num1 + num2)
        elif ope == '-':
            print(num1 - num2)
        elif ope == '*':
            print(num1 * num2)
        elif ope == '/':
            print(num1 / num2)
        else:
            print('EN-US: No and operator, insert another.')
            continue

        sair = input('\nEN-US: Do you want to leave? [Y]es or [N]o: ')
        if sair == 'Y':
            print('EN-US: THANKS YOU FOR USE MY CALCULATOR!!! \n')
            break
        elif sair == 'N':
            continue
