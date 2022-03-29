"""
This program allows a user three tries to guess the correct answer to the question
question = "That is the capital of California?". The answer is "Sacramento"

We first set max_tires = 3. Then we create a loop to iterate three times. For each interationt,
we ask the user for the answer (use input). Then based on the answer the user gives, we check
to see if the user input matches the answer. If so, print "Correct!", then terminate the loop with a
break statment.

if the user could not guess the correct answer within the max_tries, then print
"You have used your allotment of guesses.", then print "The correct answer is 'Sacromento'"
"""

"""

main
    question = "What is the capital of California?"
    answer = "Sacramento"
    ask(question, answer)


ask
    tries = 0
    loop three times
        increment tires by 1
        ask user input()
        check to see if user input is = to answer   
            if so, print"Correct" then exit loop.
if not correct
    print to the user "You have used your allotment of guesses."
    print the correct answer "The correct answer is 'Sacramento'"

main
"""


def main():
    question = "What is the capital of California?"
    answer = "Sacramento"
    ask(question, answer)


def ask(question, answer, max_tires=3):
    tries = 0
    ans = ""
    while tries < max_tires:
        tries = tries + 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your allotment of guesses.")
