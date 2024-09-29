// ფუნქციას გადაეცემა პატარა ინგლისური ასოებიანი სტრიქონი(არ შეიცავს გამოტოვებებს). დააბრუნეთ მაქსიმალური დისტანცია(ინდექსების სხვაობა) ორ ერთნაირ ასოს შორის. f("goaisthebest") = 6. ახსნა: სტრიქონის ასო ინდექსით 4(s) უდრის ასოს ინდექსით 10(s). მათ შორის დისტანციაა 10-4=6. უფრო დიდი დისტანციის მქონე ორი ერთნაირი ასო არ არსებობს.

function maxPosDifference(string) {
    let max = 0;
    for(let i = 0; i < string.length; i++) {
        let current = string.lastIndexOf(string[i]) - string.indexOf(string[i]);
        if(max < current) {
            max = current;
        }
    } 
    return max;
}

console.log(maxPosDifference(("goaisthebest")));