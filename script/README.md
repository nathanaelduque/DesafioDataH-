# Observações Importantes 

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
 




## Diferenciação de cada mão

A imagem a seguir mostra o número de clusters que vai ter em cada tipo de mão e o maior número de vezes em que determinada carta foi contada, a partir 
desse número de cluster, vê-se o tamanho do dicionário *equals*, e o numero máximo do dicionário *count_dict*, e, a partir dessas duas variáveis(*len(equals) e max(count_dict)*
consegue-se diferenciar cada tipo de mão. 


Adicionalmente, para diferenciar um flush, foi implementada uma lógica que verifica se o todos os naipes de 
todas as cartas de uma mão tem o mesmo naipe. o mesmo aconteceu para o straight, cada um possui uma variável booleana *is_flush* e *is_straight*, quando 
as duas váriaveis são true, tem-se um straight flush, a partir disso, o código checa se o maior número na mão do jogador corresponde ao A(14), se sim,
tem-se um straight royal flush.

## Critério de desempate

