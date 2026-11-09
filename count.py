#program to save the positive values in one array and negative values in another array
arr = [10,-20,30,40,-50,60,-70,80,-90]
brr = []
crr= []

def count(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            brr.append(arr[i])
        elif arr[i] < 0:
            crr.append(arr[i])

count(arr)
print("Positive numbers in the array:", brr)
print("Negative numbers in the array:", crr)

