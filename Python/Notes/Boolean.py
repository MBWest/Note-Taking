#BOOLEAN EXPRESSIONS (TRUE OR FALSE)------------------------------------------------------------

bool1 = True #Boolean expression = True
bool2 = 3*3 == 9 #Boolean expression = True
bool3 = False #Boolean expression = False
bool4 = 3*3 != 9 #Boolean expression = False

print(bool1,bool2,bool3,bool4) #Print the bool1-4 variables
print(type(bool1)) #Print the type of item that bool1 is

bool5 = "True" #Quotes make this a string and not a boolean
print(type(bool5)) #Print the type of item that bool5 is

#RELATIONAL AND BOOLEAN OPERATORS------------------------------------------------------------

greater_than = 7 > 5 #True
less_than = 5 < 7 #True
greater_than_equal_to = 7 >= 7 #True
less_than_equal_to = 7 <= 7 #True

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True
test_not = (7 > 5 ) or ( 5 > 7) # False
print(test_and, test_and2, test_or, test_or2, test_not)