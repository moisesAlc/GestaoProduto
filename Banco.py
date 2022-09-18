import mysql.connector

conexao = mysql.connector.connect(
    host='192.168.0.16',
    user='root',
    password='admin123',
    database='infinity',
    port='3308'  # a padrão é a 3306
)

cursor = conexao.cursor()
'''
#CRUD
#Create
nome = "Maria"
telefone = "2345688"
cpf = "00025632564"

comando = f'INSERT INTO aluno (nome, telefone, cpf) VALUES ("{nome}","{telefone}", "{cpf}")'

cursor.execute(comando)
conexao.commit()

#Read
comando = f'SELECT * FROM aluno'

cursor.execute(comando)

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

#Update
nome = "Maria"
telefone = "2345688"
cpf = "00025632564"
idade = 40

comando = f'UPDATE aluno SET idade = {idade} WHERE nome ="{nome}"'

cursor.execute(comando)
conexao.commit()

#Delete

nome = "Maria"
telefone = "2345688"
cpf = "00025632564"
idade = 40

comando = f'DELETE FROM aluno WHERE nome ="{nome}"'

cursor.execute(comando)
conexao.commit()
'''


def insere_usuario_senha(login, senha, nome):
    comando = f'SELECT * FROM usuarios WHERE login = {login} AND senha = {senha}'

    cursor.execute(comando)

    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)

def verifica_login_senha(login, senha):
    conexao = mysql.connector.connect(
        host='192.168.0.16',
        user='root',
        password='admin123',
        database='infinity',
        port='3308'  # a padrão é a 3306
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM usuarios WHERE login = "{login}" AND senha = "{senha}"'

    cursor.execute(comando)

    return cursor.fetchall()

cursor.close()
conexao.close()
