import random 
import json
import pathlib

#how to load a json file?
with open("Hackathon_questions.json", 'r') as file:
    questions = json.load(file)

def random_q (questions):
    #q = questions.random() How to return random value in a dictionary?
    q = random.choice(all_questions)
    return q
def get_answer (q, questions):
    a = questions["q"]

def remove(questions, q):
    a = questions.pop(q)
    return a 


if __name__ == "__main__":
    print("Welcom")
    print(input("Where are you heading to?"))
    all_questions = list(questions.values())
    
    print(q)
