#Program to show the occurance of values in array
arr = [10, 20, 10, 30, 20, 10]
def count_occurrence(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

target = 10
occurrence_count = count_occurrence(arr, target)
print(f"The number {target} occurs {occurrence_count} times in the array.")
