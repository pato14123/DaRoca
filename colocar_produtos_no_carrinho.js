function colocar_produtos_no_carrinho(produto){
    // fetch('http://localhost:3000/produtos')
    // .then(resposta => {
    //     return resposta.json()
    // })
    // .then( (dados) => {
    //     console.log(dados)
    //     exibeDados(dados)
    // })

    fetch('http://127.0.0.1:5500/produtos.json')
    .then(response => response.json())
    .then(data => {
        fetch('http://127.0.0.1:5500/produtos_no_carrinho.json')
        .then(response => response.json())
        .then(data =>{
            var produtos_no_carrinho = data.produtos_no_carrinho
            const produtos = data.produtos
            for(let i = 0; i < produtos.length; i++){
                if (produto.getAttribute('id') == produtos[i].id){
                    produtos_no_carrinho
                }
            }
         })
     })
}