def namegender(name,gender):
    if gender == 'm':
        print("Mr.", name)
    elif gender == 'f':
        print("Ms.", name)

name1 = input("Enter name: ")
gender1 = input("Enter gender: ")
namegender(name1,gender1)