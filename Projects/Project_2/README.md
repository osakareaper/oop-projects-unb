# Universo de Objs. Bidimensionais Orientados à Objeto em Python

##### OBS: Este repositório apresenta os seguintes arquivos:

- <b>`testbench_1.0.py`</b>: testbench onde foram utilizados todas as funções presentes no projeto, com todos os passos explicados por comentários no código!
- <b>`my_libraries/cartesianplane.py`</b>: classe que nos gera um Plano Cartesiano, onde é possível inserir e remover objetos do plano e também mostrá-los na tela!
- <b>`my_libraries/shapes.py`</b>: classe onde temos 4 formas que poderemos manusear da forma que quisermos com base nas funções presentes!

#### Classes:

- [Point](#na-classe-point-temos)
- [Circle](#na-classe-circle-temos)
- [Square](#na-classe-square-temos)
- [Line](#na-classe-line-temos)

#

#### Na classe Point temos:

#### Métodos:

- <b>`__init__`</b>: construtor da classe. Requer um Id (identificador do ponto) e as coordenadas X e Y.
- <b>`getType()`</b>: retorna o tipo do objeto.
- <b>`getId()`</b>: retorna o Id do objeto.
- <b>`getCoord()`</b>: printa na tela as coordenadas `(X, Y)` do ponto.
- <b>`setCoord()`</b>: permite que o usuário possa alterar as coordenas `(X, Y)` do ponto.
- <b>`getQuad()`</b>: printa na tela em qual quadrante o ponto se encontra, ou se o mesmo está na origem.
- <b>`moveToOrigin()`</b>: seta os valores de `'X'` e `'Y'` para 0, assim, movendo o ponto para a origem.

#

#### Na classe Circle temos:

#### Métodos:

- <b>`__init__`</b>: construtor da classe. Requer um Id (identificador do círculo), um ponto (origem do círculo) e o raio do círculo.
- <b>`getType()`</b>: retorna o tipo do objeto.
- <b>`getId()`</b>: retorna o Id do objeto.
- <b>`getOrigin()`</b>: printa na tela a origem do círculo.
- <b>`setCoord()`</b>: permite que o usuário possa alterar a origem do círculo.
- <b>`getRadius()`</b>: printa na tela o raio do círculo em cm.
- <b>`getDiameter()`</b>: printa na tela o diametro do círculo em cm.
- <b>`getArea()`</b>: printa na tela a área do círculo em cm².
- <b>`getCircumference()`</b>: printa na tela a circunferência do círculo em cm.

#

#### Na classe Square temos:

#### Métodos:

- <b>`__init__`</b>: construtor da classe. Requer um Id (identificador do quadrado) e o comprimento do lado.
- <b>`getType()`</b>: retorna o tipo do objeto.
- <b>`getId()`</b>: retorna o Id do objeto.
- <b>`getSide()`</b>: printa na tela o comprimeto do lado do quadrado em cm.
- <b>`getArea()`</b>: printa na tela a área do quadrado em cm².
- <b>`getPerimeter()`</b>: printa na tela o perímetro do quadrado em cm.
- <b>`getDiagonal()`</b>: printa na tela o comprimento da diagonal do quadrado em cm.

#

#### Na classe Line temos:

#### Métodos:

- <b>`__init__`</b>: construtor da classe. Requer um Id (identificador da linha) e 2 pontos (início e final da linha).
- <b>`getType()`</b>: retorna o tipo do objeto.
- <b>`getId()`</b>: retorna o Id do objeto.
- <b>`getPoints()`</b>: printa na tela as coordenadas `(X, Y)` dos pontos e quais pontos formam a linha.
- <b>`getLength()`</b>: printa na tela o tamanho da linha em cm (distância entre o ponto inicial e o ponto final), utilizando o Teorema de Pitágoras.

#
