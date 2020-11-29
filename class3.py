import random
#slaid 53

# list = []
# for f in range(100):
#     list.append(random.randint(-100, 100))
#     list.sort()
# print(list)

#64
# programmers = ['ivanov','petrov','sidorov']
# managers = ['ivanov','moxov','goroxov']
# set_progr=set(programmers)
# set_managers=set(managers)
# a = set.intersection(set_progr, set_managers)   #only prog+manag
# b = set.union(set_managers, set_progr)           #all progr,manag
# c = set.difference(set_progr, set_managers)
# print( a, b, c)

#79
list_a = set("There were scenes of jubilation in the Spanish parliament but Spain's political future looks uncertain? The Socialist Party only holds 84 seats in the Congress of Deputies so Sanchez will have to rely on securing the support of allies such as left-wing Podemos in order to enact legislation. The King has been informed of the appointment of the new prime minister and Sanchez is expected to name a cabinet early next week! Then it could be a question of just how long the government can last in a divided parliament.")
a = len(list_a)
for l in list_a:
    wordlist = l.split()
    text_len = len(wordlist)
print(wordlist)
print(text_len)
print(a)