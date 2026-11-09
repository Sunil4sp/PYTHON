#Program to show the string after removing the vowels
def string2(st):
    newstr = ''
    for char in st:
        if char in 'aeiouAEIOU':
            newstr += '*'
        else:
            newstr += char
    return newstr

st = input("Enter a string: ")
result = string2(st)
print("Original string:", st)
print("String after removing vowels:", result)