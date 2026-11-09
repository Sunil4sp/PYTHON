#Program to take input of the dictionary
num = int(input("Enter a number of employees whose data to be stored: "))
count = 1
employee = dict()
while count <= num:
    name = input("Enter the name of the Employee: ")
    salary = int(input("Enter salary of the Employee: "))
    employee[name] = salary
    count += 1

print("\n\nEmployee Name :\t Salary")
for key in employee:
    print(key," : \t", employee[key])
#print(employee)