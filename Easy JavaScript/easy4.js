// ფუნქციას გადაეცემა რიცხვების მასივი და მან უნდა დააბრუნოს მასივის ყველაზე მაქსიმალური რიცხვი. f([1, 2, 10, 3, 4, 5]) = 10, ახსნა: 10 არის ყველაზე დიდი რიცხვი ამ მასივში

function maxNumber(arr){
    let maxNum = arr[0];
    for(let i = 0; i < arr.length; i++){
        if(maxNum < arr[i]){
            maxNum = arr[i];
        }
    }
    return maxNum;
}

console.log(maxNumber([1, 2, 10, 3, 4, 5]))