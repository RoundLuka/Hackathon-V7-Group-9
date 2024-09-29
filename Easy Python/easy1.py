"""ფუნქციას გადაეცემა 3 რიცხვი. დააბრუნეთ უდიდესი. f(4,6,3) = 6"""

def manualMax(arr):
    max = arr[0]
    for i in range(arr):
        if arr[i] > max:
            max = arr[i]
    return max

print(manualMax(4,6,3))