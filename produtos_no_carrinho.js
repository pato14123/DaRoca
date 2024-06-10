var produtos_no_carrinho = []
var soma = 0

function colocar_produto(produto){
    let identificador = produto.getAttribute("id")
    let quantidade = Number(produto.querySelector(".Adicionar_Retirar").querySelector("p").innerHTML)
    let achou = false
    if(produtos_no_carrinho.length != 0){
        for(let i = 0; i < produtos_no_carrinho.length; i++){
            if(produtos_no_carrinho[i].id == identificador){
                let quantidade_no_carrinho = produtos_no_carrinho[i].quantidade
                quantidade_no_carrinho += quantidade
                produtos_no_carrinho[i].quantidade = quantidade_no_carrinho
                i = produtos_no_carrinho.length
                achou = true
            }
        }
        if(achou == false){
            let obj = {"id": identificador, "quantidade": quantidade}
            produtos_no_carrinho.push(obj)
        }
    }

    else{
        let obj = {"id": identificador, "quantidade": quantidade}
        produtos_no_carrinho.push(obj)
    }
}

function salvar_produtos_colocados(){
    localStorage.clear()
    var lista_produtos_guardados = JSON.parse(localStorage.getItem('produtos') || '[]')
    let achou = false

    for(let i = 0; i < produtos_no_carrinho.length; i++){
        for(let indice = 0; indice < lista_produtos_guardados.length; indice++){
            if(produtos_no_carrinho[i].id == lista_produtos_guardados[indice].id){
                lista_produtos_guardados[indice].quantidade += produtos_no_carrinho[i].quantidade
                achou = true
                indice = lista_produtos_guardados.length
            }
        }
        if(achou == false){
            lista_produtos_guardados.push(produtos_no_carrinho[i])
        }
    }
    localStorage.setItem("produtos", JSON.stringify(lista_produtos_guardados))
}

function mostrar_produtos_dialog(){
    dialog = document.querySelector("dialog")
    dialog.querySelector("#produtos").innerHTML = ""
    dialog.querySelector("#valor").innerHTML = ""
    fetch('http://localhost:3000/produtos')
    .then(response => response.json())
    .then(data => {
        const todos_os_produtos = data
        let produtos_salvos = JSON.parse(localStorage.getItem('produtos') || '[]')
        soma = 0
        if(produtos_salvos.length != 0){
            for(let i = 0; i < produtos_salvos.length; i++){
                for(let indice = 0; indice < todos_os_produtos.length; indice++){
                    if(produtos_salvos[i].id == todos_os_produtos[indice].id){

                        let div = document.createElement("div")
                        div.setAttribute("id",todos_os_produtos[indice].id)
                        div.setAttribute("class", "produtos_no_carrinho")
                        document.querySelector('dialog').querySelector("#produtos").appendChild(div)

                        let imagem = document.createElement("img")
                        imagem.setAttribute("src","daroca-api/imagens_de_produtos/"+todos_os_produtos[indice].imagem)
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).appendChild(imagem)

                        let nome = document.createElement("p")
                        nome.innerHTML = "Nome: "+todos_os_produtos[indice].nome
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).appendChild(nome)

                        let quantidade = document.createElement("p")
                        quantidade.setAttribute("id", "quantidade_carrinho")
                        quantidade.innerHTML = produtos_salvos[i].quantidade
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).appendChild(quantidade)

                        let valor = document.createElement("p")
                        valor.innerHTML = "valor unitário: R$"+todos_os_produtos[indice].valor
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).appendChild(valor)

                        let valor_total_produto = document.createElement("p")
                        valor_total_produto.innerHTML = "valor total produto: R$"+Number(todos_os_produtos[indice].valor)*Number(produtos_salvos[i].quantidade)
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).appendChild(valor_total_produto)

                        let div_botoes = document.createElement("div")
                        div_botoes.setAttribute("class", "botoes_carrinho")
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).appendChild(div_botoes)

                        let diminuir = document.createElement("button")
                        diminuir.innerHTML = "-"
                        diminuir.setAttribute("onclick", "diminuir_quantidade_carrinho("+todos_os_produtos[indice].id+")")
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).querySelector(".botoes_carrinho").appendChild(diminuir)

                        let aumentar = document.createElement("button")
                        aumentar.innerHTML = "+"
                        aumentar.setAttribute("onclick", "aumentar_quantidade_carrinho("+todos_os_produtos[indice].id+")")
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).querySelector(".botoes_carrinho").appendChild(aumentar)

                        let remover = document.createElement("button")
                        remover.innerHTML = "X"
                        remover.setAttribute("onclick", "remover_do_carrinho("+todos_os_produtos[indice].id+")")
                        document.querySelector('dialog').querySelector('#'+todos_os_produtos[indice].id).querySelector(".botoes_carrinho").appendChild(remover)

                        var valor_total_compra = document.createElement("p")
                        soma += (Number(todos_os_produtos[indice].valor)*Number(produtos_salvos[i].quantidade))
                        valor_total_compra.innerHTML = "Valor total da compra: R$"+soma
                        
                    }
                }
            }
            document.querySelector('dialog').querySelector("#valor").appendChild(valor_total_compra)
        }
    })
}

function diminuir_quantidade_carrinho(produto){
    let produto_diminuir_quantidade = produto[1]
    for(let i = 0; i < produtos_no_carrinho.length; i++){
        if(produtos_no_carrinho[i].id == produto_diminuir_quantidade.getAttribute("id")){
            if(produtos_no_carrinho[i].quantidade != 1){
                produtos_no_carrinho[i].quantidade -= 1
            }
        }
    }
    salvar_produtos_colocados()
    mostrar_produtos_dialog()
}

function aumentar_quantidade_carrinho(produto){
    let produto_aumentar_quantidade = produto[1]
    for(let i = 0; i < produtos_no_carrinho.length; i++){
        if(produtos_no_carrinho[i].id == produto_aumentar_quantidade.getAttribute("id")){
            produtos_no_carrinho[i].quantidade += 1
        }
    }
    salvar_produtos_colocados()
    mostrar_produtos_dialog()
}

function remover_do_carrinho(produto){
    let produto_remover_carrinho = produto[1]
    for(let i = 0; i < produtos_no_carrinho.length; i++){
        if(produtos_no_carrinho[i].id == produto_remover_carrinho.getAttribute("id")){
            produtos_no_carrinho.splice(i, 1)
            i = produtos_no_carrinho.length
        }
    }
    salvar_produtos_colocados()
    mostrar_produtos_dialog()
}

function fechar_carrinho(){
    dialog = document.querySelector("dialog")
    dialog.close()
}

function tirar_todos_carrinho(){
    produtos_no_carrinho = []
    salvar_produtos_colocados()
    mostrar_produtos_dialog()
}

function ir_para_pagamento(){
    if(produtos_no_carrinho.length != 0){
        localStorage.setItem("valor_total", soma)
        location.href = "pagamento.html"
    }
    else{
        alert("CARRINHO VAZIO!")
    }
}

function mostrar_total(){
    let valor_total_compra = JSON.parse(localStorage.getItem('valor_total') || '[]')
    document.querySelector("#total").innerHTML = "total a pagar: R$"+valor_total_compra
}