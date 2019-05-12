Week 1 Wed. Excercise 1 Step 1


secretDigit = "5"
guess = ""
guess = input("Guess a number between 1 and 20. Whats the number? ")
if guess == secretDigit:
    print("Yes! You win!")

while guess != secretDigit:
    print("Nope, try again.")
    answer = input("Whats the number? ")
    if answer == secretDigit:
        print("Yes! You win!")
        break

Step 2

secretDigit = "5"
guess = ""
guess = input("Guess a number between 1 and 20. Whats the number? ")
if guess == secretDigit:
    print("Yes! You win!")

while guess < secretDigit:
    print("Guess is too low.")
    answer = input("Whats the number? ")
    if answer > secretDigit:
        print("Guess is too high.")
    elif answer == secretDigit:
        print("Yes! You win!")
        break

Step 3

import random

number = random.randint(1, 10)
print("Guess a number between 1 and 10.")

def main():
    question = int(input("Whats the number? "))

    if question == number:
        print("Yes! You win!")
    else:
        print("Nope, try again.")
        main()
main()

Step 4

import random

number = random.randint(1, 10)
guessMade = 5
print("Im thinking of a number between 1 and 10.")

while guessMade < 6:
    print("Whats the number? ")
    guess = input()
    guess = int(guess)
    guessMade = guessMade -1

    if guess < number:
        print("Your guess is too low. You have ", guessMade, "left." )
    if guess > number:
        print("Your guess is too high. You have ", guessMade, "left.")
    if guessMade == 0:
        print("You ran out of guesses.")
        break
    else:
        if guess == number:
            print("Yes! You win!")
            break



Exercise 2 
1.)

x = "digit crafts rocks"
print(x.upper())

2.)

y = "coding is cool"
print(y.capitalize())

3.)

z = "test staement"
print(z[::-1])

4.)

replacements = (("D","|)"), ("I","1"), ("G","9"), ("T","+"), ("A","4"), ("L","|"), ("C","("), ("R","^"), ("F","7"), ("S","5"))
statement = "Digital Crafts"
for a, b in replacements:
    statement = statement.replace(a, b)
print(statement)

5.)

replacements = (("mood", "moooood"), ("good", "goooood"), ("cheese", "cheeeeese"))
sentence = "Im in the mood for good cheese!"
for a, b in replacements:
    sentence = sentence.replace(a, b)
print(sentence)




