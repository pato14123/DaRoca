import pyodbc as bd
import os

def ConectouAoBancoDeDados() -> bool: # informará se conseguiu (True) ou não (False) conectar
    global conexao
    os.system('cls') or None
    # conectar este programa ao servidor de banco de dados
    try:
        conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD24528",
                            uid="BD24528",
                            pwd=f"BD24528")                 
        
        print("Conexão bem sucedida!")
        return True
    except:
        print("Não foi possível conectar ao banco de dados")
        return False

def inserir():
    meuCursor = conexao.cursor() # cursor: objeto de manipulação de dados
    nome_produto = "-"
    while nome_produto != "0":
        nome_produto = input("Nome do Produto (0 para terminar): ")
        if nome_produto != "0":       # usuário não quer terminar o cadastro
            imagem_produto = input("Imagem do Produto: ")
            valor_produto = int(input("Digite o Valor do Produto:"))
            descrição_produto = input("Descrição do produto: ")
            categoria_produto = int(input("Digite a categoria deste produto:"))

    
        # criamos uma string com o comando Insert para inserir os novos 
            
        sComando = "insert into daroca.produtos " +\
        "           (nome, imagem, valor, descricao, categoria)"+\
        " VALUES "+\
        f"('{nome_produto}', '{imagem_produto}','{valor_produto}','{descrição_produto}','{categoria_produto}')"


        try: # tente executar o comando abaixo:
            meuCursor.execute(sComando)

        except: # em caso de erro
            print("Não foi possível incluir. Pode haver depto repetido.")
 
        meuCursor.commit() # enviar as mudanças para o BD

def alterar():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    nome_produto = "-"
    while nome_produto != "0":
        nome_produto = input("Nome do Produto (0 para terminar): ")
        if nome_produto != "0": # usuário não quer terminar o cadastro
            result = meuCursor.execute('SELECT nome, imagem, valor, descricao, categoria '+\
                                      ' FROM daroca.produtos '+\
                                      ' WHERE nome = ?', nome_produto)
            registros = result.fetchall()      # fetchall recupera os dados e os armazena na variavel registros
            if len(registros) == 0:
                print("Produto não encontrado.")
            else:
                print("Produto encontrado:\n")
                nome = registros[0][0]
                imagem = registros[0][1]
                valor = registros[0][2]
                descricao = registros[0][3]
                categoria = registros[0][4]

                if nome != None:
                    print("Nome do departamento: " + nome)
                else:
                    print("Nome não informado")

                if imagem != None:
                    print("imagem:" + imagem)
                else:
                    print("Imagem Não informada")

                if valor != None:
                    print("valor:" + valor)
                else:
                    print("Valor não informado")

                if descricao != None:
                    print("descição:" + descricao)
                else:
                    print("descrição Não informado")

                if categoria != None:
                    print("Categoria:" + categoria)
                else:
                    print("Categoria Não informada\n")

                print("\nabaixo digite [enter] para manter a informação atual\n")
                nome = input("Novo nome do Produto: ")
                valor = input("Novo Valor do Produto:")
                imagem = input("Nova imagem do Produto: ")
                descricao = input("Nova descrição do Produto: ")
                categoria = input("Nova Categoria do Produto: ")
 
                if nome == "": # usuário digitou [Enter]
                    nome = registros[0][0] # nome original do BD

                if imagem == "": # usuário digitou [Enter]
                    imagem = registros[0][1] # gerente original do BD

                if valor == "": # usuário digitou [Enter]
                    valor = registros[0][2] # data original do BD

                if descricao == "": # usuário digitou [Enter]
                    descricao = registros[0][3] # data original do BD

                if categoria == "": # usuário digitou [Enter]
                    categoria = registros[0][4] # data original do BD
 
                # criamos uma string com o comando Update para atualizar os novos dados

                sComando = "Update daroca.produtos " +\
                " set nome = ?, imagem = ?, valor = ?, descricao = ?,"+\
                " categoria = ? "+\
                " where nome = ? "
 
                # fazemos o cursor executar a string com o comando Update que criamos

                try: # tente executar o comando abaixo:
                    meuCursor.execute(sComando, nome, imagem, valor, descricao, categoria)
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver depto repetido.")

                meuCursor.commit() # enviar as mudanças para o BD 

def excluir():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    nome_produto = "-"
    while nome_produto != "0":
        nome_produto = input("Nome do Produto (0 para terminar): ")
        if nome_produto != "0": 
            result = meuCursor.execute('SELECT nome, imagem, valor, descricao, categoria '+\
                                      ' FROM daroca.produtos '+\
                                      ' WHERE nome = ?', nome_produto)
            registros = result.fetchall()
            if len(registros) == 0:
                print("Produto não encontrado.")
            else:
                print("Produto encontrado:")
                nome = registros[0][0]
                imagem = registros[0][1]
                valor = registros[0][2]
                descricao = registros[0][3]
                categoria = registros[0][4]
                if nome != None:
                    print("Nome do departamento: " + nome)
                else:
                    print("Nome não informado")
                if imagem != None:
                    print("imagem:" + imagem)
                else:
                    print("Imagem Não informada")
                if valor != None:
                    print("valor:" + valor)
                else:
                    print("Valor não informado")
                if descricao != None:
                    print("descição:" + descricao)
                else:
                    print("descrição Não informado")
                if categoria != None:
                    print("Categoria:" + categoria)
                else:
                    print("Categoria Não informada\n")
 
                resposta = input("Deseja realmente excluir (s/n)?")
                if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                    sComando = "Delete from daroca.produtos " +\
                    " where nome = ? "
                    try: # tente executar o comando abaixo:
                        meuCursor.execute(sComando, nome)
                    except: # em caso de erro
                        print("Não foi possível excluir. Deve ser um departamento em uso.")
 
                    meuCursor.commit() # enviar as mudanças para o BD 

def listar():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    try: 
        result = meuCursor.execute('SELECT nome, imagem, valor, descricao, categoria'+\
                                   'FROM daroca.produtos') 
        registros = result.fetchall()
    except:
            print("Erro na busca dos dados\n")

    print("Nome. valor. Descrição, imagem. Categoria.")
    print(registros)

    for dados in registros:
        print(f"{dados[0]}\t {dados[1]}\t {dados[2]}\t {dados[3]}\t {dados[4]}")
 
    input("Tecle [enter] para terminar:")
    
def seletor(): # CRUD: Create Retrieve Update Delete
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("Operações disponíveis")
        print("========= ===========\n")
        print("0 - Terminar este programa")
        print("1 - Adicionar Produtos")
        print("2 - Alterar Produtos") 
        print("3 - Excluir Produtos")
        print("4 - Listar Produtos")
        opcao = int(input("\nDigite o número da opção desejada:"))
        match opcao:
            case 1: inserir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()
    
if __name__ == "__main__":
    if ConectouAoBancoDeDados() :
        seletor()
        conexao.close()

print("Programa encerrado!")