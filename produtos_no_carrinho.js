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

function salvar_produtos_colocados(){
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
}

function mostrar_produtos_dialog(){
        // fetch('http://localhost:3000/produtos')
        // .then(resposta => {return resposta.json()})
        // .then(dados => {
        // })
    fetch('http://127.0.0.1:5500/produtos.json')
    .then(response => response.json())
    .then(data => {
        const todos_os_produtos = data.produtos
        let produtos_salvos = JSON.parse(localStorage.getItem('produtos') || '[]')
        if(produtos_salvos.length != 0){
            for(let i = 0; i < produtos_salvos.length; i++){
                for(let indice = 0; indice < todos_os_produtos.length; indice++){
                    if(produtos_salvos[i].id == todos_os_produtos[indice].id){

                        let div = document.createElement("div")
                        div.setAttribute("id",todos_os_produtos[indice].id)
                        document.querySelector('dialog').querySelector("#produtos").appendChild(div)

                        let imagem = document.createElement("img")
                        imagem.setAttribute("src","daroca-api/imagens_de_produtos/"+todos_os_produtos[indice].imagem)
                        document.querySelector('dialog').querySelector("#produtos").appendChild(imagem)
                    }
                }
            }
        }
    })
}