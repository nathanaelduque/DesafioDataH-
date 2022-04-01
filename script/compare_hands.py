from .checkpairs import one_pair,two_pair,three_kind,full_house,four_kind
from .royal import royal,high_card
from .untie_case import untie
from .DefResult import Result



# Vai herdar todas as funçoes check, e checar cada uma delas 
class punctuation(royal,high_card,one_pair,two_pair,three_kind,
                 full_house,four_kind):

       def get_points(self):

           self.check_royal()
           self.check_high_card()
           self.check_one_pair()
           self.check_two_pair()
           self.check_three_kind()
           self.check_full_house()
           self.check_four_kind()
           
           
# Compare sera a mixin 
# Vai fazer a comparaçao dos pontos, se o primeiro for maior, temos um 
# campeao, caso contrario, temos perca
# tbm tem o caso de empate, quando os dois possuem a mesma mao. Ex: dois two pair
class compare(untie):
    
    def compare_with(self, player_2):
        self.get_points()
        player_2.get_points()
        if self.points > player_2.points:
            return  Result.WIN
        elif player_2.points > self.points:
            return Result.LOSS
        # em caso de de dois jogadores terem os mesmo tipo de mao
        #, o codigo entra nesse else
        else:
            self.define_untie(player_2)
            if(self.points>player_2.points):

                return Result.WIN
            else:
                return Result.LOSS
