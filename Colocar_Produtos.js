//Não funcionando
$.getscript("produtos.js", function(){
    todosprodutos();
})
function colocar_produtos(tipo){
            let produtos = todosprodutos(tipo)
            console.log(produtos)
            document.querySelector('#Selecionar_Produtos').innerHTML = ""
            for(let indice = 0; indice < produtos.length; indice++){

                //cria as divs
                let div1 = document.createElement('div')
                div1.setAttribute("class", "Produto",)
                div1.setAttribute("id", produtos[indice].id)
                document.querySelector('#Selecionar_Produtos').appendChild(div1)

                //adcionar informações
                //nome
                let nome = document.createElement('p')
                let node = document.createTextNode(produtos[indice].nome)
                nome.appendChild(node)
                document.getElementById(produtos[indice].id).appendChild(nome)

                //preço
                let preco = document.createElement('p')
                node = document.createTextNode('R$' + produtos[indice].valor)
                preco.appendChild(node)
                document.getElementById(produtos[indice].id).appendChild(preco)

                //imagem
                let imagem = document.createElement('img')
                imagem.setAttribute("src", "Imagens/Produtos/" + produtos[indice].imagem)
                document.getElementById(produtos[indice].id).appendChild(imagem)

                //botões
                let a = document.querySelector('.Selecionar_Produtos')
                let div_Botoes = document.createElement('div')
                div_Botoes.setAttribute('class', "Adicionar_Retirar")
                document.getElementById(produtos[indice].id).appendChild(div_Botoes)
                let botao_adicionar = document.createElement('button')
                botao_adicionar.setAttribute('class', "Adicionar")
                botao_adicionar.setAttribute('onclick', 'adicionar('+produtos[indice].id+')')
                let botao_retirar = document.createElement('button')
                botao_retirar.setAttribute('class', 'Retirar')
                botao_retirar.setAttribute('onclick', 'retirar('+produtos[indice].id+')')
                let quant = document.createElement('p')
                quant.innerHTML = "0"
                botao_adicionar.innerHTML = "+"
                botao_retirar.innerHTML = "-"
                document.getElementById(produtos[indice].id).querySelector('.Adicionar_Retirar').appendChild(botao_retirar)
                document.getElementById(produtos[indice].id).querySelector('.Adicionar_Retirar').appendChild(quant)
                document.getElementById(produtos[indice].id).querySelector('.Adicionar_Retirar').appendChild(botao_adicionar)
                window.location.href = "#Selecionar_Produtos"
            }
        }
alert("a")