import math
import random
import time
import matplotlib.pyplot as plt


def sumThemUp(arg1, arg2):
    result = x + y
    arg1 = 15000
    arg2 = 40000
    return result

def reportGroup(personList):
    print()
    print("Printing Group")
    for i in range (0, len(personList)):
        p = personList[i]
        print(p.name + " " + str(p.weight) + " " + str(p.height))

# everything starts here
# code is either executable or declares things...

print(2)
print("Hello World")

myGreeting = 6
print (myGreeting)
myGreeting = "Hello MSc students"
print (myGreeting)


a = 8
b = 2
c = a + 5
c = b
a = a + 1
b = c + a

e = abs(-7)

# std library
p = math.pi

# imported  modules
a = math.cos(0)
a = math.sin(p/6)
a = round(a,2)


myA36276 = 21.4599943
BUYGF8474743 = 3.58487376

result = myA36276 - myA36276

print(type(a))
print(type (result))
print(id(a))


for i in range(0,10):
    print (i)
    print(type(i))
    #i = i + 1
    print(myGreeting + " " + str(i))

for i in range(0, 10, 2):
    print(myGreeting + " " + str(i))

i = 0
while i < 10:
    print(i)
    i = i + 2
    #what would happen to for with i = i + 2

#userNumber = input("Input times to greet")
userNumber = 12
userNumber = int (userNumber)

if userNumber > 100:
    print("These are too many times")
else:
    for iiii in range(0, userNumber):
        print(myGreeting + " " + str(iiii))

condition1 = True
condition2 = False


if condition1 == True:
    print("YES")
else:
    print("NO")

if condition1 == True and condition2 == True:
    print("YES")
else:
    print("NO")

if condition1 == True or condition2 == True:
    print("YES")
else:
    print("NO")

if condition1 == True ^ condition2 == True:
    print("YES")
else:
    print("NO")

if condition1 == True ^ 5 == 5:
    print("YES")
else:
    print("NO")

cond = 3 == 7
if cond:
    print("Test 1")

if not cond:
    print("Test 2")


b = False
for i in range(10):
    b = not b
    print (b)

def my_isfloat(val):
    try:
        float(val)
        return True
    except:
        return False

# a = input("Enter an Integer Value...")
# b = input("Enter an Integer Value...")
# if a.isnumeric() and b.isnumeric():
#     c = float(a) + float(b)
#     print(c)
# print (a + b)
#
#
# a = input("Enter a numeric Value...")
# b = input("Enter a numeric Value...")
# if my_isfloat(a) and my_isfloat(b):
#     c = float(a) + float(b)
#     print(c)
# print (a + b)
#


iterator = 0
terminationCondition = False
myString = "exampleString"

while (terminationCondition == False):
    print(str(iterator) + " " + myString)
    iterator += 1
    if (iterator == 50):
        terminationCondition = True

i = 0
while i < 10:
    print(myGreeting + " " + str(i))
    i = i + 1


#Functions
x = 12
y = 14
sum = x + y
print(sum)

sum2 = sumThemUp(x, y)
print(sum2)
print(x)
print(y)


def sumOrSubtract(x, y, param):
    if param:
        return x + y
    else:
        return x - y

def sum_or_subtract_optional(x, y = 2, param=True):
    if param:
        return x + y
    else:
        return x - y

otherResult = sumOrSubtract(x, y, True)
anotherResult = sumOrSubtract(x, y, False)
another_one = sumOrSubtract(param=True, y=10, x=x)

third_one = sum_or_subtract_optional(x, y)
fourth_one = sum_or_subtract_optional(x, y, False)


class Person():
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.name = ""
        self.myFriends = []

    def dietInObject(self, param):
        self.weight = self.weight - 2


p1 = Person()
p2 = Person()

p1.weight = 60
p1.height = 165
p1.name = "Mary"

name = "Alex"
p2.name = name
p2.weight = 73
p2.height = 175

p3 = Person()
p3.name = "George"
p3.weight = 80.0
p3.height = 180.0


def diet(anthrwpos: Person, param):
    anthrwpos.weight = anthrwpos.weight - param


diet(p1, 2)
p1.dietInObject(2)


def changePerson(per):
    per.weight = 1000
    pp = Person()
    pp.name = "Manos"
    pp.weight = -100
    pp.height = -100
    per = pp



changePerson(p3)
print(p3.weight)
print(p3.height)
print(p3.name)

#lists
group1 = []
group2 = []

group1.append(p1)
group1.append(p3)
group1.append(p2)
group1.append(p3)
group1.append(p1)
reportGroup(group1)

diet(p3, 5)
reportGroup(group1)

#removes the first occurence of p1
group1.remove(p1)

reportGroup(group1)

#remove at specific index, you may store the return value
removed = group1.pop(1)
reportGroup(group1)


removed = group1.pop(1)
reportGroup(group1)

group2 = group1
group1.insert(0, p1)
reportGroup(group2)

group1.insert(0, p2)
reportGroup(group2)

mylst = [5, 7, 9, 10, 1]
mylst.sort()
print(mylst)

mylst = [5, 7, 9, 10, 1]
mylst.sort(reverse=True)
print(mylst)

mylst = [5, 7, 9, 10, 1]
my_sorted_lst = sorted(mylst)
print(mylst)
print(my_sorted_lst)


def naiveSortOnWeight(listPersons):
    for i in range (0, len(listPersons)):
        for j in range (0, len(listPersons) - 1):
            if listPersons[j].weight > listPersons[j + 1].weight:
                temp = listPersons[j]
                listPersons[j] = listPersons[j + 1]
                listPersons[j + 1] = temp


naiveSortOnWeight(group1)

group1 = []
group1.append(p1)
group1.append(p3)
group1.append(p2)
group1.append(p3)
group1.append(p1)
group1.append(p1)
group1.append(p3)
group1.append(p2)
group1.append(p3)
group1.append(p1)


def WeightGetter(x):
    return x.weight

# lambda arguments: return
doubleTheNumber = lambda x: x*2
res = doubleTheNumber(3)
print (res)

doubleFirstNumberAndAddSecond = lambda x, y: x*2 + y
res = doubleFirstNumberAndAddSecond(3, 10)
print (res)


reportGroup(group1)
group1.sort(key = WeightGetter)
group1.sort(key = lambda p: p.weight)
reportGroup(group1)
reportGroup(group2)
#As I iterate through the list one element at a time , I'm going to pass the current element to the function provided in the key argument
#The sorting will be made according to the value returned by this function


#Two Dimensional lists
one_row = []
listOfLists = []

for i in range(0,10):
    one_row.append(0.0)
for i in range(0,10):
    listOfLists.append(one_row)


one_row2 = [0.0 for i in range(0,10)]
listOfLists2 = [one_row2 for i in range (0,10)]

listOfLists3 = [[0.0 for i in range(0, 10)] for j in range(0, 10)]

listOfLists[2][3] = 45
listOfLists3[2][3] = 45

print(listOfLists)
#what went wrong???

print(listOfLists3)


print("***************")
random.seed(1)
for i in range(0, 10):
    a = random.randint(0, 5)
    print (a)
print("***************")
random.seed(2)
for i in range(0, 10):
    a = random.randint(0, 5)
    print(a)

#The functions supplied by random are actually methods of a hidden instance of the random.Random class. You can instantiate your own instances of Random to get generators that don’t share state.
print("***************")
randomGenerator1 = random.Random(1)
randomGenerator2 = random.Random(2)

for i in range(0, 10):
    a = randomGenerator1.randint(0, 5)
    b = randomGenerator2.randint(0, 5)
    print (str(a) + " " + str(b))

print("Thats all!!!")


#sets
myset = set()
myset.add(5)
myset.add(7)
i=8
if i in myset:
    print("Its there " + str(i))
else:
    print("Its NOT there " + str(i))

myset.update([12,12,5,7,8,8,90])
print(myset)

myset.remove(12)
#myset.remove(70)
myset.discard(70)
myset.discard(90)
print(myset)

myStringSet = set("Manos Zachariadis")
myStringSet.discard('M')
newSet = myStringSet.difference(set('Zach'))
print(newSet)
print(myStringSet)
myStringSet.difference_update(set('Zach'))
print(myStringSet)
print(myStringSet)

print(1)

manos1 = Person()
manos2 = Person()
manos3 = Person()
manos4 = Person()
manos5 = manos4
personSet = set([manos1, manos2, manos3, manos4, manos5])
print(personSet)

#
# abyss_lst = []
# abyss_set = set()
# for i in range(0, 10000000):
#     abyss_lst.append(i)
#     abyss_set.add(i)
#
# t0 = time.time()
# a = 9900000 in abyss_lst
# t1 = time.time()
# tot_time = t1-t0
# print('in list ' + str(tot_time))
#
#
# t0 = time.time()
# a = 9900000 in abyss_set
# t1 = time.time()
# tot_time = t1-t0
# print('in set ' + str(tot_time))
#
# t0 = time.time()
# time.sleep(1)
# t1 = time.time()
# tot_time = t1-t0
# print('sleep ' + str(tot_time))

print(1)







#Dictionaries
simpleAnimalInfoDictionary = {
    "Name": "lion",
    "Weight": 680,
    "LifeExpectancy": 40
}
print(simpleAnimalInfoDictionary)

simpleAnimalInfoDictionary['is_mammal'] = False
print(simpleAnimalInfoDictionary)

simpleAnimalInfoDictionary.update({'is_mammal':True, 'is_mammal_2':True})
print(simpleAnimalInfoDictionary)

del simpleAnimalInfoDictionary['is_mammal']
print(simpleAnimalInfoDictionary)


test1 = simpleAnimalInfoDictionary["Name"]
test2 = simpleAnimalInfoDictionary.get("Name")
print(test1)
print(test2)

simpleAnimalInfoDictionary["Name"] = "Liontari"
test1 = simpleAnimalInfoDictionary["Name"]
print(test1)

for i in simpleAnimalInfoDictionary:
    print (i)

for i in simpleAnimalInfoDictionary:
    print (simpleAnimalInfoDictionary[i])

for i in simpleAnimalInfoDictionary.values():
    print (i)


st = "Extinct"
if (st in simpleAnimalInfoDictionary):
    print("Already there")
else:
    simpleAnimalInfoDictionary[st] = False

print (simpleAnimalInfoDictionary)

keys = list(simpleAnimalInfoDictionary.keys())

#just for demonstration purposes
simpleAnimalInfoDictionary = {
    "Name": "lion",
    "Weight": 680,
    "LifeExpectancy": 40,
    "Extinct": False
}
print(simpleAnimalInfoDictionary)
keys = list(simpleAnimalInfoDictionary.keys())


Zoo = {}
Zoo[simpleAnimalInfoDictionary["Name"]] = simpleAnimalInfoDictionary

print(Zoo)


def generate_a_single_animal_dictionary(keys, param):
    d = dict()
    for i in range(len(keys)):
        d[keys[i]] = param[i]
    return d


d = generate_a_single_animal_dictionary(keys, ["Hippo", 1200, 30, False])
Zoo[d["Name"]] = d
d = generate_a_single_animal_dictionary(keys, ["Dino", 15000, 70, True])
Zoo[d["Name"]] = d

print(Zoo)

tst_name = "Dino"
if tst_name in Zoo:
    print(Zoo[tst_name])

print(5)


list_x_values = []
list_y_values = []
for i in range(0,100):
    x = i
    y = 3 * i + random.normalvariate(0, 3)

    list_x_values.append(x)
    list_y_values.append(y)
#
# plt.scatter(list_x_values, list_y_values)
# plt.show()
# plt.scatter(list_x_values, list_y_values, marker='x')
# plt.xlabel('x-values')
# plt.ylabel('ys')
# plt.show()
# plt.hist(list_y_values)
# plt.show()
# plt.hist(list_y_values)
# plt.show()