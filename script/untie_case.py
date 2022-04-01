# Classe  usada para dar pontos nas casas dos decimais para as maos
# somente eh utilizada caso dois jogadores segurem o mesmo tipo de mao
# fiz uma funçao generica para funcionar em todos os casos de empate
class decimals():
    def define_decimals(self): 
        
        # A maximum sera  utilizada no criterio de desempate, ira retornar 
        #a maior carta das mais contadas.Por exemplo:
            
        #  Mao 1 :  7S 7D 6C 6H 9C     --> self.maximum=7 
        #  Mao 2:   7S 7D 5C 5H 9C     --> self.maximum=7
        
        # o 7 eh entao removido do dicionário counts_dict, para dessa forma 
        # o codigo escolher o segundo maior mais contado. No exemplo acima:
            
        #  Mao 1 :  7S 7D 6C 6H 9C     --> 7 saiu de counts_dict -->self.maximum=6 
        #  Mao 2:   7S 7D 5C 5H 9C     --> 7 saiu de counts_dict -->self.maximum=5
        
        # Mao 1 vence
        
        max_key=max(self.counts_dict.keys())
        if self.counts_dict[max_key] != list():
            maximum_value=max(self.counts_dict[max_key])
            self.maximum=maximum_value
            self.counts_dict[max_key].remove(maximum_value)
        else:
            self.counts_dict.pop(max_key)
            
        #caso de duas maos inteiramente iguais:
        if self.counts_dict == dict():
            raise Exception("It's a Tie")

                

class untie(decimals):
    
    def define_untie(self,player_2):

        while (self.points == player_2.points):
            self.define_decimals()
            self.update((self.maximum/100))
            self.maximum=0
        
            
            
            #o setar o maximum em 0 eh essencial, pois,caso continue um empate, 
            #ele passa para a segunda mais contada da mao e, com isso deve apagar 
            # o valor ja salvo em self.maximum

            player_2.define_decimals()
            player_2.update((player_2.maximum/100))
            player_2.maximum=0

