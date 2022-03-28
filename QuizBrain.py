from lib.quiz_brain import build_new_game
from lib import ui


# Game body
def main():

    im_going_in = True

    while im_going_in:
        # preparing new data
        game = build_new_game()

        # running game with new data
        quiz_ui = ui.QuizInterface(game)

        # next game check
        im_going_in = quiz_ui.next_game


if __name__ == "__main__":
    main()
