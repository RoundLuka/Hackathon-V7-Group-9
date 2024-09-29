"""ფუნქციას გადაეცემა სია და რიცხვი x, დააბრუნეთ ამ სიის მე-x ე უდიდესი ელემენტი. f([3,5,8,7,2], 4) = 3. ახსნა: სიაში [3,5,8,7,2] უდიდესი ელემენტია 8, მეორე უდიდესი 7,...,მეოთხე - 3"""

def specificBiggest(arr,x):
    sorted_arr = sorted(arr)
    reversed = sorted_arr[::-1]
    return reversed[x - 1]

print(specificBiggest([3,5,8,7,2], 4))