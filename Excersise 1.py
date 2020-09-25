print("If you enter -1 the program will be stop")
my_list = []
x = (int(input("Enter your numbers: ")))
my_list.append(x)

count = 0
sum = 0

while x != -1:
    x = (int(input("Enter your numbers: ")))
    my_list.append(x)
    count = count + 1

for i in my_list:
    sum += i

print("-----------------------------------")
print("Lit of your number that you enter: ", my_list)
print("-----------------------------------")
print("Number of your inputs: ", count, " Sigma of your numbers: ", sum)
print("-----------------------------------")
print("The avrage of your inputs: ", sum/count)
