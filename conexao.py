import psycopg2

# dados de configuração
host = 'localhost'
database = 'financeiro'
user = 'postgres'
password = 'postgres'

try:
    # parametros
    conn_parametros = 'host={0} user={1} dbname={2} password={3}'.format(host, user, database, password)
    conn = psycopg2.connect(conn_parametros)
    cursor = conn.cursor()
except NameError as erro:
    print('Erro', erro)