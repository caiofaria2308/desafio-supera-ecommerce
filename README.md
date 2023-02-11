# desafio-supera-ecommerce


## Description
Pseudo ecommerce
## Installation
* Necessário ter Docker-Compose instalado

   ```
    $ make up
    $ make loaddata
   ```

## Load products
    
    $ make load_products


## Documentantion
  * Para acessar a documentação da api basta acessar a rota `api/swagger/` quando estiver logado como super user

## Routes
  * Só será possível ver items/pedidos ou realizar checkout do usuário que está logado !
  
|Função|Método|Rota|
|------|------|----|
|Login|POST|api/login/|
|Cadastrar/Listar produtos| POST/GET| api/store/products/|
|Dados/Atualizar produto| GET/PUT/PATCH| api/store/products/{slug}|
|Visualizar carrinho| GET| api/order/cart/|
|Adicionar item no carrinho| POST| api/order/cart-add|
|Ver/atualizar/deletar item no carrinho| GET/PUT/PATCH/DELETE| api/order/cart-add/{id}|
|Realizar checkout|POST| api/order/checkout/|j
|Lista de pedidos| GET| api/order/checkout-list/|
|Visualizar/Deletar pedido| GET/DELETE| api/order/checkout-list/{numero do pedido}|

