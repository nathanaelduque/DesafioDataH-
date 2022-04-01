

![Imagem Data H](https://github.com/nathanaelduque/DesafioDataH-/blob/main/Images/datah.jpeg)
<h1 align="center"> Desafio Data H </h1>

 
<p align="center"> Desafio proposto pela Data H, que consiste em compararmos duas mãos de um jogo de pôquer e dizer qual jogador vence </p>

Esse arquivo aborda temas tais como:
 * Contexto;
 * Pré-requisitos;
 * Dicas
 * Como implementar.

*Além disso, em caso de dúvida,também existem arquivos README.MD dentro de cada pasta explicando a lógica utilizada em cada uma das etapas correspondentes*

## Contexto 

Um famoso casino de repente enfrenta um grande declínio de sua receita. Então eles decidem oferecer uma versão online do jogo de Poker. Pode ajudá-los escrevendo um algoritmo para ranquear as mãos de Poker?

## Pré-requisitos 

Os pré-requisitos dados são que:

* O código deve ser todo escrito em Python 
* Deverá ser criado um programa chamado PokerHand para representar uma mão de Poker
* PokerHand deverá ter um construtor que aceite uma string contendo 5 cartas 
* O digito espaço devera ser usado para separar cada carta.
* Cada Carta deverá consistir de dois caracteres, um deles sendo o primeiro o valor  da carta e o segundo o naipe da carta.A tabela 01 apresenta os códigos do primeiro caractere(referente ao valor), já a tabela 02 apresenta os códigos do segundo caractere(referente ao naipe de cada carta

 Tabela 01: Códigos do primeiro caractere de cada carta 
  | 1-9  | T  | Q | K | A |  
 | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | 
  |  Digito Correspondente |  10 | 11 | 12 | 13 | 

Tabela 02: Codigos do segundo caractere de cada carta 
| S  | H  | D | C |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  Espadas  |  Copas | Ouro | Paus |

*Ex: Pokerhand("KS 2H 5C JD TD") corresponde a uma mão com um 13 de Espadas, 2 de Copas, 5 de Paus , 11 de Ouro e 10 de Ouro*

* O programa deverá ter a função *compare_with*, que deverá comparar duas mãos de poker e retornar um enumerado com os resulados: WIN ou LOSS
* Existe uma série de testes a serem feitos para garantir o bom funcionamento do programa, todos eles se encontram descritos na pasta **testes**, além disso, foi anexado adicionalmente a essa mesma página um arquivo README.md, explicando o código dos testes.
* O fonte do desafio deverá estar em um repositório como o GitHub ou o GitLab. Com acesso público 
* Deve haver um README.md que explica como executar seu programa 
* Todos os testes devem estar rodando e com os resultados esperados 

## Dicas 

Algumas dicas técnicas dadas, e que foram seguidas na contrução do código desse desafio foram:

### Utilizar de Orientação a Objeto e SOLID

Nesse código foi utilizado programação orientada a objeto e os principios de SOLID foram seguidos 

#### S: Single Responsibility principle 

Resumidamente, o "Princípio da Responsabilidade Única" dita que cada classe deve ter somente uma responsabilidade dentro do código e cada responsabilidade deve ser uma classe.Isso evita que criemos uma classe com várias ou até mesmo todas as funções do código, trazendo assim complexidade e baixa eficácia ao código.
No projeto, foi criado um construtor, uma classe para pontuar cada um dos tipos de mão de poker, uma classe responsável por contabilizar os pontos de cada jogador, uma para comparar as mão e dier qual vence, e por fim, outra que implementa os critérios de desempate , caso dois jogadores possuam o mesm tipo de mão ( como o critério de desempate é o mesmo para todas as mãos, não houve necessidade de criarmos uma classe diferente para cada tipo de desempate. A figura a seguir mostra alguas classes bem separadas e definidas dento do código.


#### O: Open Closed Principle 
 O Open Closed Principle diz que um código deve ser fechado para modificações, porém deve ser aberto para ter seu comportamento estendido, isso significa que, se for necessário implementar um novo comportamento no código e sim criar uma nova classe, que estenda o comportamento do código e integrá-la ao mesmo,ou seja, não iremos modificar a estrutura basica do código, o que poderia trazer complexidade e diversos tipos de problema. 
 Um exemplo que pode ser citado nesse trabalho é um caso hipotético onde há a necessidade de criar um novo tipo de mão de Poker, nesse casos somente necessitaríamos criar uma nova classe que correspondesse a esse novo tipo de mão e integrar essa nova parte ao código original, sem haver a necessidade de modificar qualquer outra parte do código.
 Outro exemplo está na implementação dos critérios de desempate, inicialmente, o código foi criado sem nenhum critério de desempate, porém, ao notar-se a necessidade de criar esse critério, simplemente foram adicionadas ao código mais duas funções: a decimals( que trasforma em pontos decimais o valor da carta observada no critério de desempate) e a untie(que designa qual carta das mãos dos jogadores será utilizada no critério de desempate).Essa duas classes foram criadas e integradas ao código sem ter a necessidade de modificar o restante dele.


#### L: Liskov Substitution Principle


#### I: Interface Segregation Principle 


#### D: Dependency Invertion Principle


