# API Filmes
Uma API no qual lê um csv de filmes e insere todos esses filmes do csv dentro do banco de dados, e é possível procurar esses dados através de um endpoint ``/filme?name=toy%20story ``.

# Ambiente
Para preparar o ambiente, é recomendando criar um ambiente virtual e realizar os downloads via pip das dependências, que são flask, driver mysqlconnector, panda e requests. Para executar o ambiente será necessário acessar o endpoint: ``/apagar``, e após isso o ``/criar``.

# MySQL
Para tornar o ambiente funcional, será necessário executar esta seguinte query:
````sql
CREATE DATABASE IF NOT EXISTS banco_filmes;
````