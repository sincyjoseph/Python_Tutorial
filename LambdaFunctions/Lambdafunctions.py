###########################################################
def addTwo(n):
    return n + 2
print(addTwo(2))

###########################################################
# variable = lambda arguments : return statement
x = lambda n : n+2
print(x(5))

###########################################################
addTwoNum = lambda x, y : x + y
print(addTwoNum(10,20))

###########################################################
#filter
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(filter(lambda n : n%2 == 1,list1))
list3 = list(filter(lambda n : n%2 == 0,list1))
print("List1: " + str(list1))
print("List2: " + str(list2))
print("List3: " + str(list3))

###########################################################
#map
list4 = [n*2 for n in list1]
print("List4: " + str(list4))
list5 = map(lambda n : n*3,list1)
print("List5: " + str(list5))

###########################################################
