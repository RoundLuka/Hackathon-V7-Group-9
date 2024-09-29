//ფუნქციას გადაეცემა მარტიცა. დააბრუნეთ ამ მარტიცის ყველაზე დიდი ჯამის მქონე სტრიქონის ინდექსი. f([[1,4,2],[5,3,9],[4,9,2],[6,7,8]]) = 3. ახსნა: პირველი სტრიქონის ჯამია 1+4+2=7, მეორესი

function maxSumMatrix(matrix) {
    let sum = 0;
    let index = 0;
    for(let i = 0; i < matrix.length; i++){
        const currentArr = matrix[i];
        let currentSum = 0;
        for(let j = 0; j < currentArr.length; j++){
            currentSum += currentArr[j];
        }
        if(currentSum > sum) {
            sum = currentSum;
            index = i;
        }
    }
    return index;
}

console.log(maxSumMatrix([[1,4,2],[5,3,9],[4,9,2],[6,7,8]]))