"""1. მოცემულია რიცხვითი მასივი და მოცემულია ცალკე კიდევ ერ-
თი რიცხვი. იპოვეთ არის თუ არა მასივში ორი რიცხვი, რომელ-
თა ჯამი ეს ცალკე მოცემული მნიშვნელობაა."""

def containChecker(arr, num):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i] + arr[j] == num):
                return True
    return False 
            

print(containChecker([1,12,341,12,62,62,642,2], 3))