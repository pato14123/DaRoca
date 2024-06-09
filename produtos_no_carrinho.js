var produtos_no_carrinho = []

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

function ir_ao_carrinho(){
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
        console.log(lista_produtos_guardados)
    }
    localStorage.setItem("produtos", JSON.stringify(lista_produtos_guardados))
    window.location.href = 'teste.html'
}

function Aparecer(){
    console.log(localStorage)
    var produtos = JSON.parse(localStorage.getItem('produtos') || '[]')
    console.log(produtos)
}

function Voltar(){
    window.location.href = 'Mercado.html'
}

function limpar(){
    localStorage.clear()
    console.log(localStorage)
}