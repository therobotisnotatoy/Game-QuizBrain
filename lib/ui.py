from tkinter import messagebox, Label, Button, Tk, PhotoImage, Canvas
from lib.quiz_brain import QuizBrain


THEME_COLOR = "#375362"
WHITE_COLOR = "#FFFFFF"

SCORE_FONT = ("Arial", 10, "italic")
QUESTION_FONT = ("Arial", 20, "normal")


# application window
class QuizInterface:

    def __init__(self, new_quiz: QuizBrain):
        # Vars
        self.next_game = True
        self.current_quiz = new_quiz

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.attributes("-topmost", True)

        self.score_label = Label(text=f"Score: {self.current_quiz.question_number}",
                                 bg=THEME_COLOR,
                                 fg=WHITE_COLOR,
                                 font=SCORE_FONT
                                 )

        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        start_qustion = self.current_quiz.question_list[0]
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=start_qustion,
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # interaction response
        def answer_check(answer: str):
            if self.current_quiz.goes_on:
                type_of_response, text_of_response = self.current_quiz.next_question(answer)

                if type_of_response > 2:
                    self.canvas.config(bg="red")
                else:
                    self.canvas.config(bg="green")

                self.window.update()
                self.window.after(400)
                self.canvas.config(bg="white")
                self.window.update()
                self.score_label.config(text=f"Score: {self.current_quiz.question_number}")
                self.canvas.itemconfig(self.question_text, text=text_of_response)

                if type_of_response > 1:
                    is_ok = messagebox.askokcancel(title="Game Over", message="New Game?")
                    self.window.destroy()
                    self.next_game = is_ok

        def true_button_click():
            answer_check("True")

        def false_button_click():
            answer_check("False")

        true_icon = PhotoImage(file="./img/Accept-icon.png")
        false_icon = PhotoImage(file="./img/Cancel-icon.png")

        self.true_button = Button(image=true_icon,
                                  highlightthickness=0,
                                  bg=THEME_COLOR,
                                  command=true_button_click
                                  )

        self.false_button = Button(image=false_icon,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   command=false_button_click
                                   )

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
