fp = open('data1.txt', 'w')
#with open('data.txt', 'r+') as fp:
sentence = input("Enter a sentence: ")
fp.write(sentence)
#print(fp.readlines())
fp.close()

print("Now reading the contents of the file.")
fp = open('data1.txt', 'r')
for str in fp:
    print(str)
fp.close()