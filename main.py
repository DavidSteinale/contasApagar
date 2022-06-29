import fornecedor

class principal():
    print('FINANCEIRO')

    print('Menu:')
    menu = int(input('1 - Fornecedores \n2 - lançar titulos \n'))

    if(menu==1):
        fornecedor.cadastro()