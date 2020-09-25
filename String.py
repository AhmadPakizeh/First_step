# x = 'salam'
#length = len(x)

# for i in range(0, length):
#  print(i, x[i])

#y = 'salam khoobi? '

# for i in range(0, len(y)):
# print(y[i])

# for letter in 'my string':
# print(letter)

#count = 0

# for letter in y:
# if letter == 'a':
# count = count + 1
# print(letter)
#print( "The numberog a in this str is : ", count)


#z = 'man daram miram'
#print('M' + z[1:])
#print('a' in z)

#e = 'ahmad'
# print(e.upper())
# print(dir('ahmad'))

name = input('Enter your name: ')

print('hello %s whats up? do you know how old are you? ' % name.upper())
age = int(input('Enter your age: '))
print('hello %s whats up? you are %s years old ' % (name, age))
if 30 > age > 20:
    print("%s yeasr old, cool!!! you are in the bset years ofyour life but chilhood was sweeter!" % age)
elif 40 > age > 30:
    print("%s yeasr old, wow!!! you are in a wonderful year!" % age)
elif 50 > age > 40:
    print("%s years old, nice! the years of super mony :) " % age)
elif age > 50:
    print("%s years old, wow this is the net begining" % age)
else:
    print("%s years old, just unique childhood is the best of the best" % age)
