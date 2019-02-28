import random
print('Hello, what is your name?')
name = input()
print('Hello ' + name + ' welcome to the guess the number game')
print('I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTake in range (1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Goog Job ' + name + ' You guessed my number in ' + str(guessesTake) + ' guesses')
else:
    print('nope, the number I was thinking of was ' + str(secretNumber))
 
