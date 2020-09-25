import random


print("-----------------------------------")
name_of_player = input("Enter your name : ")
print("-----------------------------------")
times_to_play = int(
    input("Hello %s, how many times you want to play? " % name_of_player))
print("-----------------------------------")
print("Well %s you want play %s times, good luck!" %
      (name_of_player, times_to_play))
print("-----------------------------------")
print('Peak up a number between 1, 99')


count = 0  # To count numbers of play times!
mylist_0 = []
mylist_1 = []

############################################################################


def game():
    x = 1
    y = 99
    guess = random.randint(x, y)
    print("-----------------------------------")
    print("My guess is %s, it's right or wrong? " % guess)
    print("-----------------------------------")
    print("my answer is right or wrong? if it is right print right else enter one of this options:  If my guess is bigger thanthe answer enter B else print S")
    answer = input("Tell me: ")
    while answer != 'right':
        if answer == 'b':
            mylist_0.append(guess)
            for i in mylist_0:
                x = i
                print("-----------------------------------")
                print("Karan paien", mylist_0)
                print("Karan bala", mylist_1)
            print("-----------------------------------")
            print("Wll your answer is bigger!")
            #guess > i
            guess = random.randint(x, y)
            print("-----------------------------------")
            print("My guess is %s, it's right or wrong? " % guess)

############################################################################

        elif answer == 's':

            mylist_1.append(guess)
            for j in mylist_1:
                y = j
                print("-----------------------------------")
                print("Karan paien", mylist_0)
                print("Karan bala", mylist_1)
            print("-----------------------------------")
            print("Well your answer is smaller!")
            #guess < j
            guess = random.randint(x, y)
            print("-----------------------------------")
            print("My guess is %s, it's right or wrong? " % guess)

############################################################################

        else:
            print("-----------------------------------")
            print('Enter "b" or "s" ')

        print("-----------------------------------")
        answer = input("Tell me again: ")
    print("-----------------------------------")
    return 'Cool I did it %s. ' % name_of_player

############################################################################


for n in range(times_to_play):

    print(game())
