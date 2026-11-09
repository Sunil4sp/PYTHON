#Program to check the string is palindrome or not
def palindrome(st):
    i=0
    j=len(st)-1
    while i<j:
        if st[i]!=st[j]:
            return False
        i+=1
        j-=1
    return True

st = input("Enter a string: ")
if palindrome(st):
    print(f'"{st}" is a palindrome.')
else:
    print(f'"{st}" is not a palindrome.')