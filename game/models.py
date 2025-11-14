from .settings import *
from .exceptions import *
import random

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    def select_attack(self) -> str:
        print(f"\n<<Choose your attack>>\n\n1 - {PAPER}\n2 - {STONE}\n3 - {SCISSORS}\n")
        playerChoice = ""
        while playerChoice not in ALLOWED_ATTACKS:
            playerChoice = input("--> ")
        attack = ALLOWED_ATTACKS[playerChoice]
        print(f"\n(LOG) Your choice - {attack}")
        return attack

    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver()
        
    def add_score(self, other) -> None:
        self.score += other
        print(f"(LOG) +{other} points")

class Enemy:
    def __init__(self, difficulty, level) -> None:
        self.level = level
        self.lives = ENEMY_LIVES + level
        self.difficulty = difficulty
        self.lives *= self.difficulty
        self.lives -= 1 

    def select_attack(self) -> str:
        enemyChoice = str(random.randrange(1, 4))
        attack = ALLOWED_ATTACKS[enemyChoice]
        print(f"(LOG) Enemy choice - {attack}")
        return attack
    
    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown()