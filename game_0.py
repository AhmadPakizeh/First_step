import random

answer = random.randint(1, 100)
name = input("What is your name? ")

print("-----------------------------------")
x = int(input('Hi %s how many time you want to play? ' % name))

print("-----------------------------------")
count = 0


def game():
    guess = int(input("what is your guess? "))

    print("-----------------------------------")

    while guess != answer:
        print("Guess is:", type(guess), " Answer is: ", answer)

        print("-----------------------------------")

        if guess > answer:
            print("mine is smaller!")

            print("-----------------------------------")
        else:
            print("mine is bigger!")

            print("-----------------------------------")

        guess = int(input("what is your guess? "))

        print("-----------------------------------")

    return 'well done!!! %s you did it' % name


for count in range(x):
    print("Lets play for %s times" % x)

    print("-----------------------------------")

    answer = random.randint(1, 100)
    print(game(), 'TNX')

    print("-----------------------------------")

    count = count + 1
print("End")
