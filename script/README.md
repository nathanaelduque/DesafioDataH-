# Observações Importantes 

Esse arquivo aborda os seguintes temas:
 * [Diferenciação de cada mão](https://github.com/nathanaelduque/DesafioDataH-/blob/main/script/README.md#diferencia%C3%A7%C3%A3o-de-cada-m%C3%A3o);
 * [Pontuação de cada mão](https://github.com/nathanaelduque/DesafioDataH-/blob/main/script/README.md#pontua%C3%A7%C3%A3o-de-cada-m%C3%A3o);
 * [Critério de desempate](https://github.com/nathanaelduque/DesafioDataH-/blob/main/script/README.md#pontua%C3%A7%C3%A3o-de-cada-m%C3%A3o);

## Diferenciação de cada mão

As imagens a seguir mostram o número de clusters que vai ter em cada tipo de mão e o maior número de vezes em que determinada carta foi contada, no código, o número de clusters é dado pelo tamanho do dicionário *equals*, e o maior número de vezes em que determinada carta é contada é dado pelo numero máximo do dicionário *count_dict*.A partir dessas duas variáveis(*len(equals) e max(count_dict)* consegue-se diferenciar cada tipo de mão. 


Adicionalmente, para diferenciar um flush, foi implementada uma lógica que verifica se o todos os naipes de 
todas as cartas de uma mão tem o mesmo naipe. o mesmo aconteceu para o straight, cada um possui uma variável booleana *is_flush* e *is_straight*, quando 
as duas váriaveis são true, tem-se um straight flush, a partir disso, o código checa se o maior número na mão do jogador corresponde ao A(14), se sim,
tem-se um straight royal flush.


<p align="center">

  <img width="800" src="https://github.com/nathanaelduque/DesafioDataH-/blob/main/Images/Pokerhand01.png" alt="Tipo de mão  01">
  
</p>


<p align="center">

  <img width="800" src="https://github.com/nathanaelduque/DesafioDataH-/blob/main/Images/Pokerhand2.png" alt="Tipo de mão  02">
  
</p>

<p align="center">

  <img width="800" src="https://github.com/nathanaelduque/DesafioDataH-/blob/main/Images/Pokerhand03.png" alt="Tipo de mão  03">
  
</p>




## Pontuação de cada mão

A tabela a seguir descreve a pontuação dada para cada tipo de mão do jogo de poker


<div align="center">


  | Tipo de Mão | Pontuação |  
 | ------------------- | ------------------- | 
 | High Card   |  Digito Correspondente | 
 | One Pair  |  15 | 
 | Two Pair |  20 |
 | Three of a Kind  |  25 | 
 | Straight  |  30 | 
 | Flush  |  40 |
 | Full House  |  50 |
 | Four of a Kind  |  55 | 
 | Straight Flush |  80 |  
 | Royal Straight Flush |  100 |  
  
 </div>
 




## Critério de desempate

O critério de desempate  foi retirado do site da [Pokerstars](https://www.pokerstars.com/pt-BR/poker/games/rules/hand-rankings/?no_redirect=1#:~:text=No%20caso%20de%20um%20empate%3A%20O%20jogador%20com%20a%20carta,crit%C3%A9rio%20de%20desempate%20no%20poker.), segundo o mesmo a regra é: vê-se qual o maior valor entre as cartas mais contadas, o maior valor vence. Caso continue sendo um empate, vamos usando a mesma regra, na ordem decrescente das cartas mais contadas. Os pontos dados pelo critério de desempate são pontos decimais, no fim, o jogado com a maior pontuação vence.

Pode-se utilizar a seguinte mão como exemplo:

Jogador 01: T♥ T♠ 5♣ 5♥  K♦ , Two Pair, Pontos Jogador 01(sem considerar o critério de desempate)=20

Jogador 02: T♦ T♣ 5♠ 5♦  A♦ , Two Pair, Pontos Jogador 02(sem considerar o critério de desempate)=20

### Primeiramente,  critério de desempate irá olhar a carta mais alta de cada Two Pair, como os dois são 10, temos:

Pontos Jogador 01 = 20,10

Pontos Jogador 02 = 20,10

Se por acaso os Pontos de um jogador fosse maior que do outro, o código pararia aqui.

O valor 10 então sai da lista que guarda o maior valor das mais contadas, para que o critério de desempate avance para o próximo número (que no caso é o 5)

### Na segunda vez, o critério de desempate irá olhar a segunda carta mais alta de cada Two Pair, como os dois são 5, teremos:

Pontos Jogador 01 = 20,15

Pontos Jogador 02 = 20,15

Se por acaso os Pontos de um jogador fosse maior que do outro, o código pararia aqui.

O valor 5 sai então da lista que guarda o maior valor das mais contadas, a lista fica vazia e é excluida do dicionário que revela quais cartas foram as mais contadas(*counts_dict*), isso acontece para que, da próxima vez que o critério de desempate acontecer, o algortimo compare as cartas que forem contadas somente uma vez.

### Na última vez, teremos que o critério de desempate irá comparar as cartas contadas somente uma vez,nesse caso, tem-se:

Pontos Jogador 01 = 20,28

Pontos Jogador 02 = 20,29

### O código retorna que Jogador 02 vence!**
