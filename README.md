# Desafio 1 - Um programa para popular um banco de dados com milhares de filmes

# API Filmes
Uma API no qual lê um csv de filmes e insere todos esses filmes do csv dentro do banco de dados, e é possível procurar esses dados através de um endpoint ``/filme?name=toy%20story ``.

# Ambiente
Para preparar o ambiente, é recomendando criar um ambiente virtual e realizar os downloads via pip das dependências, que são flask, driver mysqlconnector, panda e requests. Para executar o ambiente será necessário acessar o endpoint: ``/apagar``, e após isso o ``/criar``.

# MySQL
Para tornar o ambiente funcional, será necessário executar esta seguinte query:
````sql
CREATE DATABASE IF NOT EXISTS banco_filmes;
````

---

# Desafio 2 - Implemente uma Documentação

O código é uma classe chamada ``MyClass1``, que no qual possui 5 métodos: ``method1``, ``method2``, ``method3``, ``method4`` e ``method5``.
A classe também possui 2 variáveis: ``__var1`` e ``__var2``, porém a ``__var1`` é uma lista de inteiros, já a ``__var2`` é uma string.
Começamos com o ``__init__``, que inicializa 2 atributos (``__var1`` e ``__var2``) com valores passados.
Logo após o ``get_var1`` retorna o valor da ``__var1``, logo em seguida, o ``set_var1`` atualiza o valor da ``__var1``. As mesmas funcionalidades também são aplicadas para a ``__var2``, porém, com o prefixo alterado com ``var2``.
Em seguida começam os métodos, inicializando pelo ``method1``, que verifica se há valores duplicados na lista de inteiros, e retorna ``True``, caso contrário ``False``.
Já no ``method2``, ele recebe um valor inteiro do ``target`` e retorna uma lista com dois índices que correspondem a dois valores na lista de inteiros, cuja a soma seja igual a ``target``.
Consequentemente, temos o ``method3``, que recebe um valor inteiro ``k`` e rotaciona a lista de inteiros ``__var1`` à direita ``k`` vezes.
No ``method4``, ele inverte a string ``__var2`` e retorna o resultado.
No final, o ``method5`` que é um método estático, recebe duas listas de inteiros ``x`` e ``y``, logo após, ele concatena essas listas, ordena e retorna a mediana.

# Alterações no código

Primeiramente, para um iniciante que vê este código de longe, não entende muito bem, pois o nome das funções e das variáveis não são auto-explicativas, então o que faltou inicialmente no código, foi a falta de comentários e a nomenclatura das variáveis e das funções.
Temos métodos com muitas responsabilidades também, como o ``method1`` e ``method5``, que possuem mais de uma responsabilidade. Esses métodos podem ser divididos em métodos menores, cada um com uma responsabilidade única.
Uso desnecessário de métodos estáticos, como o ``method5``, porém não há a necessidade de que ele seja desta maneira.
Ocorre também a falta de testes unitários, e isso torna difícil de saber se o código está funcionando corretamente.