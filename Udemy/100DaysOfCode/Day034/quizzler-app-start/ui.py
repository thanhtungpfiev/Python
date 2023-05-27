from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text='Score: 0', fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=200, text='Hello', font=('Arial', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.false_photo = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_photo, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=0)

        self.true_photo = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_photo, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=1)

        self.quiz = quiz_brain

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz")
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
