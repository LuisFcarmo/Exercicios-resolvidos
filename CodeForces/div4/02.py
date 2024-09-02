qtd = int(input())

class Pessoa:
    def __init__(self, cards, wins):
        self.cards = cards  # Usando self para referenciar os atributos da instância
        self.wins = wins
    
    def win(self):
        self.wins += 1
    
    def rest(self):
        self.wins = 0
        self.cards = []

    def push_card(self, card):
        self.cards.append(card)
        
sunnet = Pessoa([],0)
slavic = Pessoa([],0)

while qtd != 0:
    entrada = input() 
    a1, a2, b1, b2 = map(int, entrada.split())    
    sunnet.push_card(a1)
    sunnet.push_card(a2)
    slavic.push_card(b1)
    slavic.push_card(b2)
    

    if(sunnet.cards[0] > slavic.cards[0] and sunnet.cards[1] > slavic.cards[1]):
        sunnet.win()
    if(sunnet.cards[0] > slavic.cards[1] and sunnet.cards[1] > slavic.cards[0]):
        sunnet.win()
    if(sunnet.cards[1] > slavic.cards[0] and sunnet.cards[0] > slavic.cards[1]):
        sunnet.win()
    if(sunnet.cards[1] > slavic.cards[1] and sunnet.cards[0] > slavic.cards[0]):
        sunnet.win()
   
    print(sunnet.wins)

    sunnet.rest()
    slavic.rest()
    
    qtd-=1
