import random

class Player:
    def __init__(self) -> None:
        self.budget = 1000
        self.win=0
        self.style=""
    #function for betting 5,10,20,40,80,160,320,640,1280,2560
    def martingale(self,roulete_color):
        bet=5
        bet_color="red"
        self.style="martingale"
        if bet_color==roulete_color:
            self.budget+=bet
            bet=5
            self.win+=bet
        else:
            self.budget-=bet
            bet=bet*2
    def random_color(self,roulete_color):
        bet=5
        bet_color=random.choice(["red","black"])
        self.style="random_color"
        if bet_color==roulete_color:
            self.budget+=bet
            self.win+=bet
        else:
            self.budget-=bet
    def switch_color(self,roulete_color):
        bet=5
        bet_color="red"
        self.style="switch_color"
        if bet_color==roulete_color:
            self.budget+=bet
            self.win+=bet
            bet_color="black"
        else:
            self.budget-=bet
            bet_color="red"
    def play(self,roulete_color,player):
        if player=="martingale":
            self.martingale(roulete_color)
        elif player=="random_color":
            self.random_color(roulete_color)
        elif player=="switch_color":
            self.switch_color(roulete_color)
