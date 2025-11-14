from game.models import Player
from game.settings import *
from game.game import Game
from game.score import ScoreHandler


def main():

    print("\n <<Game: Stone-Scissors-Paper>>\n\n# 1 - Start game\n# 2 - Show scores\n# 3 - Exit")

    OPTIONS = {
        "1":"Start game",
        "2":"Show scores",
        "3":"Exit"
    }

    choice = input("--> ")

    while choice not in OPTIONS:
        print("Неправильный выбор")
        choice = input("--> ")

    match OPTIONS[choice]:
        case "Start game":
            play_game()
        case "Show scores":
            show_scores()
        case "Exit":
            return
        

def play_game() -> None:
    player_info = create_player()
    game = Game(player_info["Player"], player_info["Mode"])
    game.play()
    return

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
    handler.game_record.prepare_records()

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
