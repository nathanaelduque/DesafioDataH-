from .count_score import score



# Classe utilizada para pontuar caso seja uma mao do tipo one pair
class one_pair(score):

#Se houver somente um par len(self.equals)=  -- > One pair     
    def check_one_pair(self): 
        if (len(self.equals)==4):
            self.update(15)     #Pontuaçao One Pair = 15
                                #Se nao for, não pontua


# Classe utilizada para pontuar caso seja uma mao do tipo two pair
class two_pair(score):

 # se houver dois pares: duas condiçoes terao que ser satisfeitas:
 # tamanho do dicionário que retorna as contagens = 3, len(self.equals)=3
 # o maximo de vezes que iremos contar uma carta eh duas --> max(self.counts_dict)=2
    def check_two_pair(self):
        if (len(self.equals)==3 and max(self.counts_dict)==2):
            self.update(20)     #Pontuaçao Two Pair = 20
                                #Se nao for, nao pontua






# Classe utilizada para pontuar caso seja uma mao do tipo three of a kind         
class three_kind(score):
    
    def check_three_kind(self):
# se for um three of a kind, duas condiçoes devem ser satisfeitas:
# tamanho do dicionário que retorna as contagens = 3, len(self.equals)=3
# o maximo de vezes que iremos contar uma carta eh 3 --> max(self.counts_dict)=3   
        if (len(self.equals)==3 and max(self.counts_dict)==3):
            self.update(25)     #Pontuaçao Three of a Kind  = 25
                                #Se nao for, nao pontua
        

# Classe utilizada para pontuar caso seja uma mao do tipo full house      
class full_house(score):

# se for um full house, duas condiçoes tambem devem ser satisfeitas:
# tamanho do dicionario que retorna as contagens = 2, len(self.equals)=2
# o maximo de vezes que iremos contar uma carta eh 3 --> max(self.counts_dict)=3     
    def check_full_house(self):

        if (len(self.equals)==2 and max(self.counts_dict)==3):
            self.update(50)     #Pontuaçao Full House = 50
                                #Se nao for, nao pontua



# Classe utilizada para pontuar caso seja uma mao do tipo full house      
class four_kind(score):

# se for um four of a kind, duas condiçoes tambem devem ser satisfeitas:
# tamanho do dicionario que retorna as contagens = 2, len(self.equals)=2
# o maximo de vezes que iremos contar uma carta eh quatro --> max(self.counts_dict)=4     
    def check_four_kind(self):

        if (len(self.equals)==2 and max(self.counts_dict)==4):
            self.update(55)     #Pontuaçao Full House = 50
                                #Se nao for, nao pontua