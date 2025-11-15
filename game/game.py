from .models import Enemy
from .settings import POINTS_FOR_KILLING_NORMAL, POINTS_FOR_KILLING_HARD, ATTACK_PAIRS_OUTCOME, POINTS_FOR_FIGHT, SCORE_FILE
from .exceptions import GameOver, EnemyDown
from .score import ScoreHandler, PlayerRecord
# from main import create_player

class Game():
    def __init__(self, player, difficulty):
        self.player = player
        self.difficulty = difficulty
        self.level = 0
        self.create_new_enemy()

    def create_new_enemy(self) -> None:
        self.level += 1
        self.enemy = Enemy(self.difficulty, self.level)
                
    def play(self) -> None:
        print("-" * 50)
        print("\n=== GAME STARTED ===\n")
        while True:
            try:
                outcome = self.fight()
                self.handle_fight_result(outcome)
            
            except EnemyDown:
                print(f"\n=== Enemy Defeated! ===\n" f"New enemy created — (level {self.level})")
                print("-" * 50)
                if self.difficulty == 2:
                        self.player.add_score(POINTS_FOR_KILLING_HARD)
                        print(f"(LOG) +{POINTS_FOR_KILLING_HARD} points")
                else:
                    self.player.add_score(POINTS_FOR_KILLING_NORMAL)
                    print(f"(LOG) +{POINTS_FOR_KILLING_NORMAL} points")
                self.create_new_enemy()
            
            except GameOver:
                print(f"\n=== GAME OVER! ===")
                print(f"Current level - {self.level}")
                self.save_score()
                break

    def fight(self) -> int:
            player_attack = self.player.select_attack()
            enemy_attack = self.enemy.select_attack()
            outcome = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
            self.player.add_score(POINTS_FOR_FIGHT)
            return outcome
    
    def handle_fight_result(self, outcome) -> None:
        match outcome:
            case "Draw":
                print("\n# Draw!")
            case "Win":
                print("\n# Win!")
                self.enemy.decrease_lives()
            case "Lose":
                print("\n# Lose!")
                self.player.decrease_lives()
    
    def save_score(self):
            record = PlayerRecord(self.player.name, str(self.difficulty), self.player.score)
            handler = ScoreHandler(SCORE_FILE)
            handler.game_record.add_record(record)
            handler.save()



    