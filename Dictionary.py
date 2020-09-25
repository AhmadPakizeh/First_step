#a = dict()

#F2T = dict()
#F2T['hi'] = 'salam'
# print(F2T)

#Ghad= {'ahmad': 182, 'parvin': 160}
# print(Ghad)
# print(Ghad['ahmad'])

# print(Ghad.keys())
# print(list(Ghad.keys()))
# print(Ghad.values())
#print(183 in Ghad)

string = 'Ahmad is here and testing py'

counter = dict()

# for letter in string:
#  if letter in counter:
#   counter[letter] += 1
# else:
#   counter[letter] = 1

for letter in string:
    counter[letter] = counter.get(letter, 0) + 1

for this_one in list(counter.keys()):
    print('%s appeared %s times' % (this_one, counter[this_one]))
