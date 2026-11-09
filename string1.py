def string1(ch, str1):
    count = 0
    for char in str1:
        if char == ch:
            count += 1
    return count

str1 = input("Enter a string: ")
ch = input("Enter a character: ")
count = string1(ch, str1)
print(f"The character '{ch}' appears {count} times in the string.")
