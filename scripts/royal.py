from .count_score import score

#Classe encarregada de pontuar um flush 
class flush(score):
    
    def check_flush(self):
        i=0
        self.is_flush=True
        while(i<4 and self.is_flush ==True):  # Vai fazer 4 comparaçoes entre as cartas
                                              #Porem, se encontrar uma que ja nao seja,
                                              # ja retorna que nao eh e sai do laço 
            if self.sep_characters[i][1] != self.sep_characters[i+1][1]:
                self.is_flush=False
                
            i+=1
        if self.is_flush == True:
            self.update(40)     # Pontuação Flush = 40
                                # Nao vai pontuar se nao for
          


                                 

# Classe encarregada de pontuar um straight
class straight(score):

     def check_straight(self):
         
        self.is_straight=False
        if(max(self.first_characters)-min(self.first_characters)==4):
            self.is_straight= True
            self.update(30)  # Pontuaçao Straight = 40
                             # Nao vai pontuar se nao for




#Classe encarregada de checar se eh um straight flush
#tem mixin aqui tbm, creio
class straight_flush(straight,flush,score):
    
    def check_straight_flush(self):
        
        self.is_straight_flush = False
        self.check_straight() # Vai checar se eh um straight e pontuar se for 
        self.check_flush()    # Vai checar se eh um flush e pontuar se for
        
        # Se for straight e Flush --> Straight Flush
        if(self.is_straight==True and self.is_flush==True):
            self.is_straight_flush=True 
            self.update(10) #Vai adicionar mais 10 pontos se for um straight flush 
    
    
            

# Classe encarregada de pontuar um royal straight flush
class royal(straight_flush,score):

#Se for um straight flush e a maior carta for  um A -- > royal straight flush    
     def check_royal(self):
 
         self.check_straight_flush()
         if (self.is_straight_flush == True and max(self.first_characters)==14):
             self.update(20) # Alem dos pontos de flush e de straight, e do 
                             # Straight flush, ganha mais 20 pontos
                             # ganha + 10 pontos
 
   
# Classe utilizada para pontuar caso seja uma mao do tipo high card
class high_card(score):  
    
# Se nao existir cartas iguais, nao for flush e nem straight, sera high card
     def check_high_card(self):         
        if(len(self.equals)==5 and self.is_flush == False and self.is_straight == False):
            self.update(max(self.first_characters))  # Pontuaçao High Card =
                                                     # numero da maior carta