import psycopg2

# dados de configuração
host = 'localhost'
database = 'financeiro'
user = 'postgres'
password = 'postgres'
# sslmode = 'require'

try:
    # parametros
    conn_parametros = 'host={0} user={1} dbname={2} password={3}'.format(host, user, database, password)
    conn = psycopg2.connect(conn_parametros)
    cursor = conn.cursor()
except NameError as erro:
    print('Erro', erro)


# def inserir_fornecedor(*args):
#     sql = "INSERT INTO tb_fornecedor(nome_forn) VALUES(%s);"
#     cursor.execute(sql,args)
#     conn.commit()
#     cursor.close()
#     conn.close()

# def listar_fornecedor():
#     sql = "SELECT * FROM tb_fornecedor;"
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print('ID:', row[0], '- fornecedor: ', row[1])



# if (__name__ == '__main__'):
#     listar_fornecedor()