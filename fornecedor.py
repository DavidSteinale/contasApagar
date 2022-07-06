import conexao

def cadastro():
    print('************************')
    print('*CADASTRO DE FORNECEDOR*')
    print('************************')
    menu=0
    while(menu!=5):
        menu = int(input('Informe uma das opções: \n 1 - Cadastrar\n 2 - Listar\n 3 - Atualizar\n 4 - Excluir'))

        if(menu==1):
            inserir()
        elif(menu==2):
            listar()
        elif(menu == 3):
            update()
        elif(menu == 4):
            delete()

def inserir():
        try:
           print()
           nome = input('Digite o nome do novo fornecedor; ')
           sql = f"INSERT INTO tb_fornecedor(nome_forn) VALUES('{nome}');"
           conexao.cursor.execute(sql)
           conexao.conn.commit()
           conexao.cursor.close()
           conexao.conn.close()
        except NameError as erro:
            print('Erro', erro)

def listar():
    sql = "SELECT * FROM tb_fornecedor;"
    conexao.cursor.execute(sql)
    rows = conexao.cursor.fetchall()

    for row in rows:
        print('Cógido:', row[0], '- fornecedor: ', row[1])

def update():
    try:
        id_forn = int(input('Informe o código do fornecedor: '))
        args = input('Informe o novo nome do fornecedor:')
        sql = f"UPDATE tb_fornecedor SET nome_forn='{args}' WHERE id_forn={id_forn};"
        conexao.cursor.execute(sql)
        conexao.conn.commit()
        conexao.cursor.close()
        conexao.conn.close()
    except NameError as erro:
        print('Erro', erro)

def delete():
    try:
        id = int(input('Informe o codigo do fornecedor a ser excluido:'))
        sql1 = f"SELECT * FROM tb_fornecedor WHERE id_forn={id};"
        conexao.cursor.execute(sql1)
        rows = conexao.cursor.fetchall()

        for row in rows:
            print('Fornecedor:', row[0],'-', row[1])

        opcao = input('Deseja realmente excluir? S - sim | N - não :')

        if(opcao.lower()=='s'):
            sql = f"DELETE FROM tb_fornecedor WHERE id_forn={id};"
            conexao.cursor.execute(sql)
            conexao.conn.commit()
            conexao.cursor.close()
            conexao.conn.close()
            print('Excluido com sucesso.')
        else:
            print('Registro não excluido.')
    except NameError as erro:
        print('Erro', erro)

#
# if(__name__=='__main__'):
#     cadastro()
