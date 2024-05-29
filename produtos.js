//Não funcionando
function todosprodutos(tipo){
    var produtos = [{nome: "Maças(unidade)", valor: "0,99", imagem: "Maçãs.png", id: "Macas", tipo: "Frutas"},
                    {nome: "Laranjas(unidade)", valor: "0,99", imagem: "Laranjas.png", id: "Laranjas", tipo: "Frutas"},
                    {nome: "Peras(unidade)", valor: "0,99", imagem: "Peras.png", id: "Peras", tipo: "Frutas"},
                    {nome: "Mamões(unidade)", valor: "4,99", imagem: "Mamões.png", id: "Mamoes", tipo: "Frutas"},
                    {nome: "Maracujás(unidade)", valor: "1,99", imagem: "Maracujas.png", id:"Maracujas", tipo: "Frutas"},
                    {nome: "Brócolis (quantidade em kilogramas)", valor: "5,99", imagem: "brocolis.png", id: "Brocolis", tipo: "Legumes"},
                    {nome: "Alho (quantidade em kilogramas)", valor: "32,99", imagem: "alho.png", id: "Alho", tipo: "Legumes"},
                    {nome: "Cebola (quantidade em kilogramas)", valor: "R$6,59", imagem: "cebola.png", id: "Cebola", tipo: "Legumes"},
                    {nome: "Cenoura (quantidade em kilogramas)", valor: "5,99", imagem: "cenoura.png", id: "Cenoura", tipo: "Legumes"},
                    {nome: "Pimentão (quantidade em kilogramas)", valor: "24,99", imagem: "pimentao.png", id:"Pimentao", tipo: "Legumes"},
                    {nome: "Salsicha (quantidade em kilogramas)", valor: "32,99", imagem: "salsicha.png", id: "Salsicha", tipo: "Frios"},
                    {nome: "Salame (quantidade em kilogramas)", valor: "90,99", imagem: "salame.png", id: "Salame", tipo: "Frios"},
                    {nome: "Presunto (quantidade em kilogramas)", valor: "90,99", imagem: "presunto.png", id: "Presunto", tipo: "Frios"},
                    {nome: "Queijo (quantidade em kilogramas)", valor: "95,99", imagem: "queijo.png", id: "Queijo", tipo: "Frios"},
                    {nome: "Mortadela (quantidade em kilogramas)", valor: "92,99", imagem: "mortadela.png", id:"mortadela", tipo: "Frios"},
                    {nome: "Suco De Laranja (unidade de 500Ml)", valor: "5,99", imagem: "sucodelaranja.png", id: "SucoDeLaranja", tipo: "Bebidas"},
                    {nome: "Leite (unidade de 1L)", valor: "4,99", imagem: "leite.png", id: "Leite", tipo: "Bebidas"},
                    {nome: "Guarana (unidade de 2L)", valor: "8,99", imagem: "guarana.png", id: "Guarana", tipo: "Bebidas"},
                    {nome: "Fanta (unidade de 2L)", valor: "7,99", imagem: "fanta.png", id: "Fanta", tipo: "Bebidas"},
                    {nome: "Coca Cola (unidade de 2L)", valor: "10,99", imagem: "cocacola.png", id:"CocaCola", tipo: "Bebidas"},
                    {nome: "Arroz (por quilo)", valor: "5,99", imagem: "arroz.png", id: "Arroz", tipo: "Alimentos"},
                    {nome: "Azeite De Oliva (garrafa 500ml)", valor: "39,99", imagem: "azeitedeioliva.png", id: "AzeiteDeOliva", tipo: "Alimentos"},
                    {nome: "Feijão (por quilo)", valor: "8,99", imagem: "feijão.png", id: "Feijao", tipo: "Alimentos"},
                    {nome: "Macarrão (meio quilo)", valor: "4,99", imagem: "macarrão.png", id: "Macarrao", tipo: "Alimentos"},
                    {nome: "Tilápia (por quilo)", valor: "12,00", imagem: "peixe.png", id:"Tilapia", tipo: "Alimentos"}]
    let selecionado = []
    for(let i = 0; produtos.length; i++){
        if(produtos[i].tipo == tipo){
            selecionado += produtos[i]
        }
    }
    return selecionado
}