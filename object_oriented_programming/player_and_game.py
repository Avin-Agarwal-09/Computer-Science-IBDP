class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
    
    def add_points(self,points):
        self.score += points
    
class Game:
    def __init__(self):
        self.players = []

    def add_player(self,player):
        self.players.append(player)
    
    def leader(self):
        top_player = self.players[0]
        for player in self.players:
            if player.score > top_player.score:
                top_player = player
        
        return top_player
    
    def total_points(self):
        total = 0
        for player in self.players:
            total += player.score
        return total

p1 = Player("Alice")
p2 = Player("Bob")

p1.add_points(10)
p1.add_points(5)

p2.add_points(12)
print(p1.score)
print(p2.score)

g = Game()

g.add_player(p1)
g.add_player(p2)

print(g.total_points())   # 27

print(g.leader().name)    # Alice

p2.add_points(10)

print(g.leader().name)    # Bob
print(g.total_points())   # 37