//ფუნქციას გადაეცემა რიცხვების მასივი. ფუნქციამ უნდა დააბრუნოს მასივის მაქსიმალურ რიცხვს გამოკლებული მასივის მინიმალური რიცხვი. f([1, 2, 3, 4, 5]) = 4,  ახსნა: 5 - 1 = 4

function maxDifference(arr){
    let smallest = arr[0];
    let largest = arr[0];
    for(let i = 0; i < arr.length;i++){
        if(arr[i] > largest){
            largest = arr[i];
        }
        if(arr[i] < smallest){
            smallest = arr[i];
        }
    }
    return largest - smallest;
}

console.log(maxDifference([1, 2, 3, 4, 5]))