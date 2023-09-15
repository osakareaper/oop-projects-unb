# Universo de Objs. Bidimensionais Orientados à Objeto

##### OBS: Este repositório apresenta um arquivo .txt que contém um pseudocódigo orientado à objetos.

#### Classes:

- [Point](#na-classe-point-temos)
- [Line](#na-classe-line-temos)
- [Circle](#na-classe-circle-temos)
- [Square](#na-classe-square-temos)

#

#### Na classe Point temos:

#### Atributos:

- <b>`X`</b>: é o X da coordenada do ponto. Um valor inteiro.
- <b>`Y`</b>: é o Y da coordenada do ponto. Um valor inteiro.

#### Métodos:

- <b>`constructor()`</b>: construtor da classe. Requer que sejam passados dois inteiros `'a'` e `'b'`, que serão as atribuições das coordenadas `'X'` e `'Y'` do ponto.
- <b>`getPoint()`</b>: retorna para o usuário as coordenadas `(X, Y)` do ponto.
- <b>`quad()`</b>: retorna para o usuário o número do quadrante em que o ponto se encontra ou se o mesmo se encontra na origem (0).
- <b>`moveToOrigin()`</b>: seta os valores de `'X'` e `'Y'` para 0, assim, movendo o ponto para a origem.
- <b>`isOnOrigin()`</b>: compara se os valores `'X'` e `'Y'` são iguais à 0 e, se sim retorna `True (1)` e, se não, `False (0)`.

#

#### Na classe Line temos:

#### Atributos:

- <b>`start`</b>: ponto inicial da linha. É criado um novo point para ser o início da linha.
- <b>`end`</b>: ponto final da linha. É criado um novo point para ser o fim da linha.

#### Métodos:

- <b>`constructor()`</b>: construtor da classe. Requer que sejam passados `'a'` (início da linha, um novo Point) e `'b'` (fim da linha, um novo Point).
- <b>`arePointsEqual()`</b>: verifica se os pontos fornecidos são iguais, retornando `True (1)` caso forem, ou `False (0)` caso não forem.
- <b>`length()`</b>: retorna para o usuário o tamanho da linha (distância entre o ponto inicial e o ponto final), utilizando o Teorema de Pitágoras.

#

#### Na classe Circle temos:

#### Atributos:

- <b>`center`</b>: centro do círculo. É criado um novo Point para ser o centro do círculo.
- <b>`R`</b>: raio do círculo. Um valor de ponto flutuante.

#### Métodos:

- <b>`constructor()`</b>: construtor da classe. Requer que sejam passados `'a'` (centro do círculo, um novo Point) e `'b'` (raio do círculo).
- <b>`area()`</b>: retorna para o usuário a área do círculo.
- <b>`circumference()`</b>: retorna para o usuário a circunferência do círculo.
- <b>`diameter()`</b>: retorna para o usuário o diâmetro do círculo.

#

#### Na classe Square temos:

#### Atributos:

- <b>`origin`</b>: ponto de origem do quadrado, para saber onde o mesmo deverá ser criado no plano. É criado um novo Point para ser a origem do quadrado.
- <b>`side`</b>: lado do quadrado. Um valor de ponto flutuante.

#### Métodos:

- <b>`constructor()`</b>: construtor da classe. Requer que sejam passados `'a'` (origem do quadrado, um novo Point) e `'b'` (lado do quadrado).
- <b>`area()`</b>: retorna para o usuário a área do quadrado.
- <b>`perimeter()`</b>: retorna para o usuário o perímetro do quadrado.
- <b>`diagonal()`</b>: retorna para o usuário a diagonal do quadrado.

#
