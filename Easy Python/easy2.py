'''ფუნქციას გადაეცემა ლუწი ზომის სია. გაუცვალეთ ადგილები კენტ ინდექსებს ლუწ ინდექსებთან
(0<-->1, 2<-->3,...). f([4,6,3,8,7,4,6,9]) = [6,4,8,3,4,7,9,6]. ახსნა: პირველი ელემნტი(4) გაიცვალა მეორე 
ელემენტთან(6), მესამე(3) მეოთხესთან(8), მეხუთე(7) მეექვსესთან(4), მეშვიდე(6) მერვესთან(9).'''

def swap(num_list):
    i=0
    while(i<len(num_list)):
        x=num_list[i]
        num_list[i]=num_list[i+1]
        num_list[i+1]=x
        i=i+2
    return num_list

print(swap([4,6,3,8,7,4,6,9]))