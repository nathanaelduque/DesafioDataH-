# Uma classe pai, chamada de score eh criada para se obedecer o Open-Closed
# principle
class score ():
#Soh vai atualizar os pontos de cada Jogador 
#  O parametro kind points,ja eh util para o Liskov Substitution Principle
    def update(self,kind_points):
        self.points+=kind_points