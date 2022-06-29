import fornecedor

print('CONTAS A PAGAR.')

print('Menu:')
menu = int(input('1 - Cadatro de fornecedores \n2 - lançar titulos \n'))

if(menu==1):
    fornecedor.cadastro()