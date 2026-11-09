#Program to show the reverse of the string
def reverse_string(st):
    rev_st = ""
    for ch in range(-1, -len(st)-1, -1):
        rev_st += st[ch]
    return rev_st

st = input("Enter a string: ")
new_str = reverse_string(st)
print("Reversed string:", new_str)


    