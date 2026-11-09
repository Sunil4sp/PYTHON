#Program to concatenate, repetation, membership, slicing, use of functions of the tuple
tup = (10, 12, 13, 14, 15, 16)
tup = tup + (17, 18,)       #concatenate of the tuple using '+' operator
tup1 = ("Hello", "!","Welcome") 
print(tup1 * 3)     #repetation of the tuple
print(tup)          #printing the tuple
print('!' in tup1) #membership operator using 'in'
print(tup[1:])      #slicing of the tuple
print(tup[:8])      #slicing of the tuple
tup2 = tuple('aeiou')   #use of tuple method
tup3 = tuple([1,2,7,4,5,6,7,8])     #use of tuple method
print(tup2,tup3,tup3.count(7), sorted(tup3))