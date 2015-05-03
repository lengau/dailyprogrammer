#!/usr/bin/env python3
# Daily Programmer #212, intermediate edition: Animals
# http://redd.it/34asls

import pickle
import random

YES_ANSWERS = ['yes', 'yep', 'yeah', 'ja', 'da', 'y']
NO_ANSWERS = ['no', 'nope', 'nein', 'nyet', 'nee', 'n']
QUESTIONS_FILENAME = 'questions.dat'
GLOATS = [
    'HAHA! You lost to a computer!',
    'You lost to a computer. You idiot!',
    "You shouldn't feel too bad for losing to me. I am a computer, after all."
    ]
VOWELS = 'aeiou'

class Question(object):
    """A question to be asked in the game."""
    def __init__(self, text, yes, no):
        self.text = text
        self.answers = {True: yes, False: no}

    def ask(self):
        """Ask a question and handles the user's response.

        If the response leads to an answer, check with the user if the answer
        is correct.
        """
        answer = ask_question(self.text)
        if isinstance(self.answers[answer], Question):
            return self.answers[answer]
        elif isinstance(self.answers[answer], str):
            an = 'n' if self.answers[answer][0].lower() in VOWELS else ''
            answer_string = 'a%s %s' % (an, self.answers[answer])
            if ask_question('I think your animal is %s. Am I correct?' %
                            answer_string):
                won_game()
                return True
            else:
                child_question = self.create(no=self.answers[answer])
                self.answers[answer] = child_question
                return False
        else:
            print("I don't know what type of animal it is.")
            animal = input('What is the name of your animal? -> ')
            self.answers[answer] = animal

    @classmethod
    def create(cls, no=None):
        animal = input('What is the name of your animal? ->')
        question_string = input('What is a unique question that answers yes '
                                'for %s? ->' % animal)
        return Question(question_string, animal, no)


def ask_question(question):
    while True:
        answer = input('%s --> ' % question)
        answer = answer.lower()
        if answer in YES_ANSWERS:
            return True
        if answer in NO_ANSWERS:
            return False
        print("I don't understand your answer.")


def load_questions(filename=QUESTIONS_FILENAME):
    """Load the question/answer pairs from a file."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("No animals in database. Creating initial question.")
        return Question.create()


def save_questions(base_question):
    with open(QUESTIONS_FILENAME, 'wb+') as file:
        return pickle.dump(base_question, file)

def won_game():
    print(random.choice(GLOATS))


def main():
    base_question = load_questions()
    question = base_question
    while True:
        question = question.ask()
        if isinstance(question, bool) or question is None:
            break
    save_questions(base_question)


if __name__ == '__main__':
    main()
