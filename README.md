# SOTEC BACKEND

## Requisitos do projeto
  
  Para rodar e testar o projeto é necessário Python3.12, django, django-restframework,
  para instalar o django e django-restframework, realizar o comando **pip install -r requirements.txt** em um terminal.

## Como rodar o projeto

  Para rodar o projeto primeiro é necessário executar as migrations, usando o comando
  **python3 manage.py migrate**

  Após isso rodar o comando
  **python3 manage.py runserver**

  o servidor estará disponível na porta 8000 do endereço local ou em formato de link acessar
  [http://localhost:8000]

  Para adicionar dados usando fixtures usar o comando
  **python3 manage.py loaddata fixtures/items.json --app base.item**

## Rotas do projeto

  Para acessar as rotas do projeto siga esses endereços(Nas rotas com id, substituir por um número).

  ### Rota GET all
    Essa rota retorna todos os registros cadastrados no banco.
    [http://localhost:8000/]
  
  ### Rota POST
    Essa rota cadastra um novo registro no banco.
    [http://localhost:8000/add/]

  ### Rota PUT
    Essa rota altera todos os campos de um registro cadastrado no banco.
    [http://localhost:8000/put/id/]

  ### Rota PATCH
    Essa rota altera alguns dos campos de um registro cadastrado no banco.
    [http://localhost:8000/patch/id/]

  ### Rota DELETE
    Essa rota deleta um registro do banco.
    [http://localhost:8000/delete/id/]

  ### Rota Swagger
    Essa rota contém a documentação swagger da API.
    [http://localhost:8000/swagger/]