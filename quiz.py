
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

prompts = [
    "Which color is banana? (a)Red, (b)Yellow, (c) Green: ",
    "Which color are roses? (a)Green, (b)Blue, (c)Red:  "
]
questions = [
    Question(prompts[0], "b"),
    Question(prompts[1], "c")
]

def start_test(questions):
    for question in questions:
        a = ""
        guess_count = 0
        while a != question.answer and guess_count < 3:
            if guess_count > 0:
                print("Try one more time")
            a = input(question.prompt)
            guess_count += 1 

        if  guess_count >= 3:
            print("You lost")
        else:
            print("Correct!")

start_test(questions)
