from datetime import datetime

from unicodedata import decimal

import conexao

def cadastro():
    print('************************')
    print('*LANÇAMENTOS DE TITULOS*')
    print('************************')
    menu=0
    listar()

def inserir():
    try:
        print()
        fornecedor = input('Digite o CODIGO do fornecedor? ')
        valor = float(input('Divite o valor do titulo? '))
        venc = input('Vencimento? ')
        sql = f"INSERT INTO tb_titulo(id_forn, venc, valor) VALUES('{fornecedor}','{venc}','{valor}');"
        conexao.cursor.execute(sql)
        conexao.conn.commit()
        conexao.cursor.close()
        conexao.conn.close()
    except NameError as erro:
         print('Erro', erro)

def listar():
    try:
        sql = "SELECT * FROM tb_titulo AS t INNER JOIN tb_fornecedor AS f ON t.id_forn=f.id_forn;"
        conexao.cursor.execute(sql)
        rows = conexao.cursor.fetchall()
        for row in rows:
            print('Vencimento:', row[2], '- valor: ', row[3], '- fonecedor: ', row[5])
    except NameError as erro:
        print('Erro', erro)

if(__name__=='__main__'):
     cadastro()