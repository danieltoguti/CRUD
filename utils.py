import MySQLdb


def conectar():
    try:
        conn = MySQLdb.connect(
            db='loja',
            host='localhost',
            user='daniel',
            passwd='1234'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySql Server {e}')


def desconectar(conn):
    if conn:
        conn.close()


def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos....')
        print('.....................')
        for produto in produtos:
            print(f'Id: {produto[0]}')
            print(f'Nome: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Quantidade: {produto[3]}')
    else:
        print('Não existem produtos cadastrados')
    desconectar(conn)


def inserir():
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    quantidade = int(input('Informe a quantidade: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {quantidade})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto {nome} inserido com sucesso.')
    else:
        print('Não foi possível inserir o produto.')

    desconectar(conn)


def atualizar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preço do produto: '))
    quantidade = int(input('Informe a quantidade: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={quantidade} WHERE idProduto={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto {nome} atualizado com sucesso.')
    else:
        print('Não foi possível atualizar o produto.')

    desconectar(conn)



def deletar():

    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f'DELETE FROM produtos WHERE idProduto={codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto excluído com sucesso.')
    else:
        print('Não foi possível excluir o produto.')
    desconectar(conn)

def menu():

    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    print('5 - Sair.')
    opcao = int(input())

    while True:
        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
                menu()
            elif opcao == 2:
                inserir()
                menu()
            elif opcao == 3:
                atualizar()
                menu()
            elif opcao == 4:
                deletar()
                menu()
        else:
            print('Opção inválida')
        if opcao == 5:
            print('sair')
        return False

    

