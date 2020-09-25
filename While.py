your_num = int(input("Enter a random number: "))  # get number
while your_num >= 0:
    print(your_num)
    your_num = your_num + 1  # if we have + without break we go in a infinity loop
    if your_num == 100:
        print("You reachthe 100")
        break
print("Out of loop")



name = input("What is yor name ? ")  # get name
while name != 'end':
    print('salam', name)
    name = input("What is yor name ? ")  # without this we go in infinity loop
