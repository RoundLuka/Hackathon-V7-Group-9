#ფუნქციას გადაეცემა სია. დააბრუნეთ სია, სადაც არის ამ სიის მხოლოდ ლუწი რიცხვები. f([5,4,56,7,8,3,563]) = [4,56,8]. ახსნა: ამ სიის ლუწი ელემენტები.

def filter_evens(list):
    evens_list = []
    for i in list:
        if i % 2 == 0:
             evens_list.append(i)

    return evens_list

print(filter_evens([12,4,5,23,17,24]))