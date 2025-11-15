from game.models import Player
from game.settings import USER_CHOICE_OPTIONS,MODES,SCORE_FILE
from game.game import Game
from game.score import ScoreHandler

def main():
    print("\n <<Game: Stone-Scissors-Paper>>\n\n# 1 - Start game\n# 2 - Show scores\n# 3 - Exit")
    choice = input("--> ")

    while choice not in USER_CHOICE_OPTIONS:
        print("Incorrect choice")
        choice = input("--> ")

    match USER_CHOICE_OPTIONS[choice]:
        case "Start game":
            start_game()
        case "Show scores":
            show_scores()
        case "Exit":
            return
        
def start_game():
    player_info = create_player()
    game = Game(player_info["Player"], player_info["Mode"])
    play_game(game)

def play_game(game: Game):
    game.play()

def create_player() -> dict:
    NICKNAME = input("\n# Write your nickaname: ")
    CHOOSED_DIFFICULTY = input("\n# Choose difficulty:\n1 - Normal\n2 - Hard\n--> ")

    while CHOOSED_DIFFICULTY not in MODES:
        print("\n# Incorrect choice")
        CHOOSED_DIFFICULTY = input("\n# Choose difficulty:\n1 - Normal\n2 - Hard\n--> ")

    player = Player(NICKNAME)
    return {"Player": player, "Mode": int(CHOOSED_DIFFICULTY)}


def show_scores():
    handler = ScoreHandler(SCORE_FILE)
    handler.prepare_records()

    print("\n===== SCORES TABLET =====")
    if not handler.game_record.records:
        print("# TABLET EMPTY!")
        print("=========================\n")
        return main()
    for i, r in enumerate(handler.game_record.records, 1):
        print(f"{i}. {r}")

    print("=========================\n")
    return main()

main()
