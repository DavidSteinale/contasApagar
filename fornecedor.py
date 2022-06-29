import conexao

def cadastro():
    print('************************')
    print('*CADASTRO DE FORNECEDOR*')
    print('************************')

    delete()

def update(id_forn,*args):
    try:
        sql = f"UPDATE tb_fornecedor SET nome_forn=%s WHERE id_forn={id_forn};"
        conexao.cursor.execute(sql,args)
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
            print('Registro excluido.')
    except NameError as erro:
        print('Erro', erro)

def inserir(*args):
    try:
        sql = "INSERT INTO tb_fornecedor(nome_forn) VALUES(%s);"
        conexao.cursor.execute(sql, args)
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
        print('ID:', row[0], '- fornecedor: ', row[1])

if(__name__=='__main__'):
    cadastro()
