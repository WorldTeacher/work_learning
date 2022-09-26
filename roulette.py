import random
import player as p
from termcolor import colored
class Roulette:
    def __init__(self) -> None:
        self._number = random.randint(0, 36)
        self.color=self.get_color()

    def get_color(self)->str:
        if self._number == 0:
            return "green"
        elif self._number % 2 == 0:
            return "black"
        else:
            return "red"
    def play_game(self,games):
        player1=p.Player()
        player2=p.Player()
        player3=p.Player()
        for i in range(games):
            roulete=Roulette()
            player1.play(roulete.color,"martingale")
            player2.play(roulete.color,"random_color")
            player3.play(roulete.color,"switch_color")
        
        return player1,player2,player3
    
    def max_profit(self,runs:int):
        players=self.play_game(runs)
        max_profit=0
        for player in players:
            if player.win>max_profit:
                max_profit=player.win
                max_player=player.style
        max_profit_msg=colored(max_profit,'blue',attrs=['bold'])
        max_player_msg=colored(max_player,"green",attrs=['bold'])
        print(f'Player with {max_player_msg} method made the most profit: {max_profit_msg}')
        print(f'meaning he won {round(max_profit/runs,2)} per game')
        

if __name__ == "__main__":
    for i in range(100):
        Roulette().max_profit(1000)
    # game=Roulette()
    # game.max_profit(1000)
        

   
