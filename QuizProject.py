class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
    
    def display_question(self):
        question = self.questions[self.current_question_index]
        answer = input(question.prompt)
        self.check_answer(answer)
        self.current_question_index += 1 
    
    def check_answer(self, answer):
        question = self.questions[self.current_question_index]
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("Correct")
        else:
            print("Incorrect!")

    def has_more_questions(self):
        return self.current_question_index < len(self.questions)

    def display_score(self):
        print(f"Your score is {self.score} / {len(self.questions)} ")


question_dict = {
    "What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n(d) Rome\n": "c",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n": "b",
    "Who wrote 'To Kill a Mockingbird'?\n(a) Harper Lee\n(b) J.K. Rowling\n(c) Ernest Hemingway\n(d) F. Scott Fitzgerald\n": "a",
    "What is the smallest prime number?\n(a) 0\n(b) 1\n(c) 2\n(d) 3\n": "c",
    "Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Saturn\n": "b",
    "What is the chemical symbol for water?\n(a) O\n(b) H2\n(c) H2O\n(d) HO2\n": "c",
    "Who painted the Mona Lisa?\n(a) Vincent van Gogh\n(b) Pablo Picasso\n(c) Leonardo da Vinci\n(d) Claude Monet\n": "c",
    "Which language is primarily spoken in Brazil?\n(a) Spanish\n(b) English\n(c) Portuguese\n(d) French\n": "c",
    "What is the largest ocean on Earth?\n(a) Atlantic Ocean\n(b) Indian Ocean\n(c) Arctic Ocean\n(d) Pacific Ocean\n": "d",
    "Who developed the theory of relativity?\n(a) Isaac Newton\n(b) Albert Einstein\n(c) Nikola Tesla\n(d) Galileo Galilei\n": "b",
    "What is the hardest natural substance on Earth?\n(a) Gold\n(b) Iron\n(c) Diamond\n(d) Silver\n": "c",
    "Which planet is closest to the sun?\n(a) Venus\n(b) Earth\n(c) Mars\n(d) Mercury\n": "d",
    "Who is known as the Father of Computers?\n(a) Charles Babbage\n(b) Alan Turing\n(c) Bill Gates\n(d) Steve Jobs\n": "a",
    "What is the tallest mountain in the world?\n(a) K2\n(b) Kangchenjunga\n(c) Lhotse\n(d) Mount Everest\n": "d",
    "Which element has the atomic number 1?\n(a) Helium\n(b) Hydrogen\n(c) Oxygen\n(d) Carbon\n": "b"
}

#using loop to create list of questions
questions = [Question(prompt,answer) for prompt,answer in question_dict.items()]

def run_quiz():
    quiz = Quiz(questions)
    while quiz.has_more_questions():
        quiz.display_question()
    quiz.display_score()


run_quiz()



    






