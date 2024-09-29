//ფუნქციას გადაეცემა String და მან უნდა დააბრუნოს ეს სთრინგი შებრუნებულად. f("abcd") = "dcba", ახსნა: სიტყვა შებრუნდა

function reverseString(string){
    let reversed = "";
    for(let i = string.length - 1; i >= 0; i--){
        reversed += string[i];
    }
    return reversed;
}

console.log(reverseString("abcd") )
