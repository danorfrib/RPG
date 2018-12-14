from random import randint

class Actor:
    def __init__ (self, name, health, stamina, mana):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.mana = mana
    
    def recover (self):
        rsp = randint (0, 5)
        print (self.name, " recovers ", rsp, " stamina points!")

    def __str__ (self):
        return "[{}]\nHP: {}\nSP: {}\nMP: {}".format(
    self.name, self.health, self.stamina, self.mana)

    def heavy_attack (self, other):
        d20 = randint (1, 20)

    def light_attack (self, other):
        d20 = randint (1, 20)

        if d20 == 1:
            self. stamina -= 15
            print("[{}]: Critical failure on light attack! -15 stamina.".format(self.name))
            return
        
        self.stamina -= 5

        DAMAGES = [
          0, # 1
          5, 5, 5, # 2, 3, 4 
          6, 6, # 5, 6
          7, 7, 7, 7, # 7, 8, 9, 10
          10, 10, 10, 10, 10, # 11, 12, 13, 14, 15
          15, 15, 15, 15, # 16, 17, 18, 19
          19  # 20
        ]
        
        dmg = DAMAGES[d20 - 1]

        if d20 == 20:
            dmg += randint (1, 20)
        
        other.health -= dmg
        print ("[{}]: {} DMG to {}!".format(self.name, dmg, other.name))


    def attack(self, other):
        self.light_attack (other)

        '''
        dmg = min (randint (0, 35), self.stamina * 2)
        self.stamina -= dmg // 2
        other.health -= dmg

        print (self.name, "deals", dmg, "damage points to", other.name)
        '''

    def is_alive (self):
        return self.health > 0
    
    def is_dead (self):
        return not self.health > 0