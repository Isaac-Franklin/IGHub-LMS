let fellowname = document.querySelectorAll('.name')
let assignment = document.querySelector('.assignment')
let grade = document.querySelector('.grade')
let groupdata = document.querySelectorAll('.groupdata')


console.log('test working')
console.log('====================================');
console.log(fellowname);
console.log('====================================');

console.log('====================================');
console.log(groupdata);
console.log('====================================');

fellowname.forEach(element => {
    let newFellows = element.innerHTML
    console.log(newFellows)
    return newFellows
});







// let allFellows = []

// const addAllFellows = () => {
//     let newAllFellows = allFellows.push(fellowname)
//     console.log('====================================');
//     console.log(newAllFellows);
//     console.log('====================================');
// }

// addAllFellows();