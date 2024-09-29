'''ფუნქციას გადაეცემა სია. დააბრუნეთ True, თუ ამ სიაში მეორდება ელემენტი ორჯერ. 
სხვა შემთხვევაში დააბრუნეთ False. f([4,6,3,7,4,9,8]) = True. ახსნა: 4 მეორდება 2-ჯერ.'''

def fun(num_list):
    for i in num_list:
        if num_list.count(i)==2:
            return True
    
    return False

print(fun([4,6,3,7,4,9,7]))