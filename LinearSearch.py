# Program to show the use of linear search in a list
def linearSearch(n,list1):
    for i in range(0,len(list1)):
        if n == list1[i]:
            return i
    return None

myList = []
n = int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    num = int(input())
    myList.append(num)

numberToBeSearched = int(input("Enter the number to be searched: "))
result = linearSearch(numberToBeSearched,myList)

if result is not None:
    print("Element found at index:", result)
else:
    print("Element not found in the list")