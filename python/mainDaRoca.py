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
    id_produto = "-"
    while id_produto != "0":
        id_produto = input("id do Produto (0 para terminar): ")
        if id_produto != "0":       # usuário não quer terminar o cadastro
            nome_produto = input("Nome do Produto:")
            valor_produto = float(input("Digite o Valor do Produto:"))
            imagem_produto = input("Imagem do Produto: ")
            tipo_produto = input("Descrição do produto: ")

    
        # criamos uma string com o comando Insert para inserir os novos 
            
        sComando = "insert into daroca.produtos " +\
        " VALUES "+\
        f"('{id_produto}', '{nome_produto}','{valor_produto}','{imagem_produto}','{tipo_produto}')"


        try: # tente executar o comando abaixo:
            meuCursor.execute(sComando)

        except: # em caso de erro
            print("Não foi possível incluir. Pode haver produto repetido.")
 
        meuCursor.commit() # enviar as mudanças para o BD

def alterar():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    id_produto = "-"
    while id_produto != "0":
        id_produto = input("id do Produto (0 para terminar): ")
        if id_produto != "0": # usuário não quer terminar o cadastro
            result = meuCursor.execute('SELECT * '+\
                                      ' FROM daroca.produtos '+\
                                      ' WHERE id = ?', id_produto)
            registros = result.fetchall()      # fetchall recupera os dados e os armazena na variavel registros
            if len(registros) == 0:
                print("Produto não encontrado.")
            else:
                print("Produto encontrado:\n")
                id = registros[0][0]
                nome = registros[0][1]
                valor = registros[0][2]
                imagem = registros[0][3]
                tipo = registros[0][4]

                if id != None:
                    print("id do produto: " + id)
                else:
                    print("id não informado")

                if nome != None:
                    print("nome do produto:" + nome)
                else:
                    print("nome Não informado")

                if valor != None:
                    print("valor:" + valor)
                else:
                    print("Valor não informado")

                if imagem != None:
                    print("imagem:" + imagem)
                else:
                    print("Imagem Não informada")

                if tipo != None:
                    print("tipo:" + tipo)
                else:
                    print("tipo Não informado\n")

                print("\nabaixo digite [enter] para manter a informação atual\n")

                id = input("Novo nome do Produto: ")
                nome = input("Novo Valor do Produto:")
                valor = float(input("Nova imagem do Produto: "))
                imagem = input("Nova descrição do Produto: ")
                tipo = input("Nova Categoria do Produto: ")
 
                if id == "": # usuário digitou [Enter]
                    id = registros[0][0] # nome original do BD

                if nome == "": # usuário digitou [Enter]
                    nome = registros[0][1] # gerente original do BD

                if valor == "": # usuário digitou [Enter]
                    valor = registros[0][2] # data original do BD

                if imagem == "": # usuário digitou [Enter]
                    imagem = registros[0][3] # data original do BD

                if tipo == "": # usuário digitou [Enter]
                    tipo = registros[0][4] # data original do BD
 
                # criamos uma string com o comando Update para atualizar os novos dados

                sComando = "Update daroca.produtos " +\
                " set id = ?, nome = ?, valor = ?, imagem = ?,"+\
                " tipo = ? "+\
                " where id = ? "
 
                # fazemos o cursor executar a string com o comando Update que criamos

                try: # tente executar o comando abaixo:
                    meuCursor.execute(sComando, id, imagem, valor, imagem, tipo)
                except: # em caso de erro
                    print("Não foi possível incluir. Pode haver depto repetido.")

                meuCursor.commit() # enviar as mudanças para o BD 

def excluir():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    id_produto = "-"
    while id_produto != "0":
        id_produto = input("id (0 para terminar): ")
        if id_produto != "0": 
            result = meuCursor.execute('SELECT * '+\
                                      ' FROM daroca.produtos '+\
                                      ' WHERE id = ?', id_produto)
            registros = result.fetchall()
            if len(registros) == 0:
                print("Produto não encontrado.")
            else:
                print("Produto encontrado:")
                id = registros[0][0]
                nome = registros[0][1]
                valor = registros[0][2]
                imagem = registros[0][3]
                tipo = registros[0][4]
                if id != None:
                    print("id do produto: " + id)
                else:
                    print("id não informado")
                if nome != None:
                    print("nome do produto:" + nome)
                else:
                    print("nome Não informado")
                if valor != None:
                    print("valor:" + valor)
                else:
                    print("Valor não informado")
                if imagem != None:
                    print("imagem:" + imagem)
                else:
                    print("imagem Não informada")
                if tipo != None:
                    print("tipo:" + tipo)
                else:
                    print("tipo Não informado\n")
 
                resposta = input("Deseja realmente excluir (s/n)?")
                if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                    sComando = "Delete from daroca.produtos " +\
                    " where id = ? "
                    try: # tente executar o comando abaixo:
                        meuCursor.execute(sComando, id)
                    except: # em caso de erro
                        print("Não foi possível excluir. Deve ser um departamento em uso.")
 
                    meuCursor.commit() # enviar as mudanças para o BD 

def listar():
    meuCursor = conexao.cursor() # objeto de manipulação de dados
    try: 
        result = meuCursor.execute('SELECT *'+\
                                   'FROM daroca.produtos') 
        registros = result.fetchall()
    except:
            print("Erro na busca dos dados\n")

    for dados in registros:
        print(f"id: {dados[0]}\t nome:{dados[1]}\t valor:{dados[2]}\t imagem:{dados[3]}\t tipo:{dados[4]}")
 
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