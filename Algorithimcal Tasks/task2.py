"""2. მოცემულია n+2 რიცხვისგან შექმნილი მასივი, რომელთა მნიშ-
ვნელობები არის დიაპაზონში 1-დან n-მდე. ყველა რიცხვი გან-
სხვავებულია გარდა ორი რიცხვისა, რომლებიც მეორდებიან.

იპოვეთ ეს რიცხვები"""

def findDuplicates(arr):
    first = arr[0]
    sum = 0
    count = 0
    for num in arr:
        sum += num
        count += 1
    for i in range(first, count):
        sum -= i
    return sum

print(findDuplicates([1,35,2,352,5,2]))