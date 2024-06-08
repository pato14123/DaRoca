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
    nome_produto = "1"
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