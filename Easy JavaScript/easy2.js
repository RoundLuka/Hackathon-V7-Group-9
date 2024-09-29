//ფუნქციას გადაეცემა მასივი (მასივში მოცემული იქნება რიცხვები ან ტექსტური ინფორმაცია) და მან უნდა დააბრუნოს ერთი String, სადაც იქნება მასივის ყველა ელემენტი. f(["aa", 10, "abc", 20]) = "aa10abc20", ახსნა: ყველა მასივის ელემენტი მოვათავსეთ ამ სთრინგში

function joinArr(arr){
    let joinedArr = "";
    for(let i = 0; i < arr.length; i++){
        joinedArr += arr[i];
    }
    return joinedArr;
}

console.log(joinArr(["aa", 10, "abc", 20]));