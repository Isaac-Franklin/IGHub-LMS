let grade = document.querySelectorAll('.grade')


console.log('test working')
console.log('====================================');
console.log(grade);
console.log('====================================');


let gradeArr = []
let newFellows;
let value = 0;
grade.forEach(element => {
    newFellows = element.innerHTML
    gradeArr.push(newFellows)
    return gradeArr
});

console.log(gradeArr)
const newgradeArr = []
const addAll = () => {
    gradeArr.map((cur) => {
        let numberScore = parseInt(cur);
        newgradeArr.push(numberScore)
        // value = numberScore + 0
        console.log(newgradeArr)
    })
    return newgradeArr

}

addAll()
console.log(newgradeArr)
let sumAllUp;
const sunScore = async () => {
    sumAllUp = await newgradeArr.reduce((acc, cur) => {
        acc + cur, value
        console.log(sumAllUp)
    })
}
sunScore()
// console.log(sunScore)