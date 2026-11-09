#Program to show the menu and select the various list
myList = [22, 11, 34, 45, 67, 89, 90]
choice = 0
while True:
    print("The list 'myList' has the following elements", myList)
    print("\nL I S T O P E R A T I O N S")
    print(" 1. Append an element")
    print(" 2. Insert an element at the desired position")
    print(" 3. Append a list to the given list")
    print(" 4. Modify an existing element")
    print(" 5. Delete an existing element by its position")
    print(" 6. Delete an existing element by its value")
    print(" 7. Sort the list in ascending order")
    print(" 8. Sort the list in descending order")
    print(" 9. Display the list")
    print(" 10. Exit")
    choice = int(input("Enter your choice (1-10):"))
    if choice == 1:
        element = int(input("Enter the element to append: "))
        myList.append(element)
        print("Element appended.")
    elif choice == 2:
        element = int(input("Enter the element to insert: "))
        pos = int(input("Enter the position: "))
        myList.insert(pos, element)
        print("Element inserted.")
    elif choice == 3:
        newList = input("Enter the elements of the new list: ")
        myList.extend(newList)
        print("List appended.")
    elif choice == 4:
        i = int(input("Enter the position of the element to be modified: "))
        if i < len(myList):
            newElement = int(input("Enter the new element: "))
            oldElement = myList[i]
            myList[i] = newElement
            print("The element",oldElement,"has been modified\n")
        else:
            print("Position of the element is more than the length of list")
    #delete an existing element by position
    elif choice == 5:
        i = int(input("Enter the position of the element to be deleted: "))
        if i < len(myList):
            element = myList.pop(i)
            print("The element",element,"has been deleted\n")
        else:
            print("\nPosition of the element is more than the length of list")
    #delete an existing element by value
    elif choice == 6:
        element = int(input("\nEnter the element to be deleted: "))
        if element in myList:
            myList.remove(element)
            print("\nThe element",element,"has been deleted\n")
        else:
            print("\nElement",element,"is not present in the list")
    #list in sorted order
    elif choice == 7:
        myList.sort()
        print("\nThe list has been sorted")
    #list in reverse sorted order
    elif choice == 8:
        myList.sort(reverse = True)
        print("\nThe list has been sorted in reverse order")
    #display the list
    elif choice == 9:
        print("\nThe list is:", myList)
    #exit from the menu
    elif choice == 10:
        break
    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()
