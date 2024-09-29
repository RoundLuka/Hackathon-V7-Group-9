'''ფუნქციას გადაეცემა ორი არგუმენტი: სიტყვა და შესაცვლელი სიმბოლო. დააბრუნეთ სიტყვა, 
საიდანაც ამოშლილი იქნება ყველა შესაცვლელი სიმბოლო. f("hello", "l') = "heo" ახსნა: სიტყვაში შეგვხვდა "l", ამიტომ ის ამოიშალა'''

def fun(word, l):
    new_word=""
    for i in word:
        if i!=l:
            new_word=new_word+i

    return new_word

print(fun("saba", "a"))
print(fun("hello", "l"))