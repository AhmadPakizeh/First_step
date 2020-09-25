#l = [1, 10, 'ahmad']
##l[0] = 9
# for i in range(0, len(l)):
#print(i, l[i])
# print('------------------------')
# for item in l:
# print(item)


#l1 = [1, 2]
#l2 = ['ahmad', 'armin', 'ehsan']

#print(l1 + l2)

# print(type(l1))
# print(dir(l1))

l3 = [1, 2]
l3.append('ahmad')
print(l3)

l3.extend([1, 6, 9, 4.5])

print(l3)

del l3[2]

print(l3)
l3.sort()  # just for int
print(l3)

x = l3.pop()
print(l3)

print(x)

l3.remove(6)

print(l3)

print(len(l3), '& ', sum(l3), ' & ', max(l3), ' & ', min(l3))


s = 'ahmad reza pakizeh'

#list_of_words = print(s.split())
#print('t'.join(list_of_words))

#print(s.split('a'))

