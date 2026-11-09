#Program to show the use of list1 into list2 
def list2(list3):
    for i in range(0, len(list3)):
        list3[i] += 5
    print(list3)

list1 = [10,11,12,13,14,15,16,17,18,19]
list2(list1)
print(list1)