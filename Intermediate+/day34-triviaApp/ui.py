from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0,command=self.false_pressed)
        self.false_btn.grid(row=2, column=0)
        
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0,command=self.true_pressed)
        self.true_btn.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            qtext=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qtext)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self,correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.set_score()
        self.window.after(500,self.get_next_question)

    def set_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")