# O codigo naturalmente ja vai dar uma pontuaçao maior para um straight flush
# mas tem que ver o royal flush 

from collections import Counter
from scripts.compare_hands import punctuation,compare






class PokerHand(compare,punctuation):
    '''
    Esse eh o construtor utilizado para separar as cartas da mao, e ler
    cada uma delas da devida maneira
    '''
    def __init__(self,Hand):
        
        self.points=0
        
#Vai dividir a mao em 5 cartas usando o caractere "espaço" como separador
        self.cards=Hand.split(" ")
        

# Vai criar uma lista de tamanho = 2 para cada carta, a posiçao 0 dessa lista
# Contera o valor numerico da carta, a posiçao 1, o tipo da carta 

#Ex: 2H(dois de copas) --> [2,H]

#Ele vai repetir esse processo ate ter salvado toda a mao na lista 
#"sep_characters"
        self.sep_characters=list()
        for card in self.cards:
            sep_card=list(card)
            self.sep_characters.append(sep_card)
            
# Nessa parte,e ele ira reconhecer o primeiro digito da seguinte maneira:
# Se for numerico (funçao isdigit()),mantem como estah 
# se for uma letra, substitui pelo seu correpondente numerico 
#Ex: TH -- > [10,H]

        for i in range(0,len(self.sep_characters)):
            first=self.sep_characters[i][0]
            test_first=first.isdigit()
            if(test_first==True):
                self.sep_characters[i][0]=int(self.sep_characters[i][0])
            else:
                if(self.sep_characters[i][0]=='T'):
                    self.sep_characters[i][0]=10
                elif(self.sep_characters[i][0]=='J'):
                    self.sep_characters[i][0]=11
                elif(self.sep_characters[i][0]=='Q'):
                    self.sep_characters[i][0]=12
                elif(self.sep_characters[i][0]=='K'):
                    self.sep_characters[i][0]=13
                elif(self.sep_characters[i][0]=='A'):
                    self.sep_characters[i][0]=14

# Criamos uma lista com todos os primeiros caracteres de todas as cartas 
# Esses caracteres correspondem aos números e serao usados para determinar
# se eh flush, _ of a kind, full house ou mesmo high card

        self.first_characters=list() 
        for cards in (self.sep_characters):
            self.first_characters.append(cards[0])
        self.first_characters.sort()

 # Criamos a variavel equals, que vai nos retornar um dicionario contando
 # quantos primeiros caracteres iguais tem em cada mao, foi colocada aqui para 
 # evitar desperdi­cio de custo computacional, ja que sera usada pelas classes 
 # four_kind, full_house, three_kind, two_pair, 
 # one_pair e high_card     
        
        self.equals = Counter(self.first_characters) 

            
# Counts_dict retorna um dicionario mostrando uma lista de quais cartas 
# foram contadas 2 vezes,3 vezes e assim por diante 
        
        #Ex: 5D 5S 3C 3H KS --> counts_dict = {2: [5, 3], 1: [13]}
        self.counts_dict=dict()
        for value in self.equals.values():
            counts_list=list()
            for key in self.equals.keys():
                count=self.equals[key]
                if (count ==value  and key not in counts_list):
                    counts_list.append(key)
                    
            self.counts_dict[value]=counts_list
