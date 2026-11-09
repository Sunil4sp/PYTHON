fp = open("data2.txt", "w+")
while True:
    data = input("Enter data to be saved in the file: ")
    fp.write(data)
    ans = input("Do you want to continue? (y/n): ")
    if ans == 'n':
        break
fp.close()
fp = open("data2.txt", "r")
for line in fp:
    print(line)
fp.close()