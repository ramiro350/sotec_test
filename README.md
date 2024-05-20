# SOTEC BACKEND

## Requisitos do projeto
  
  Para rodar e testar o projeto é necessário Python3.12, django, django-restframework,
  para instalar o django, django-restframework, drf-yasg e Docker.

## Instalar dependências

  Clonar o projeto com git clone https://github.com/ramiro350/sotec_test.git

  Para instalar as depedências você pode tanto realizar um **pip install -r requirements.txt** ou
  fazer o build do projeto com o comando **docker compose build --no-cache**.

## Como rodar o projeto(Com Docker)

  Para rodar o projeto utilizando Docker,usar o comando **docker compose up**

  Para entrar no container gerado após esse comando, usar **docker exec -it project-app-1 bash**

  Rodar o comando dentro do container, **python3 manage.py loaddata fixtures/items.json --app base.item** 

## Como rodar o projeto(Sem Docker)

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