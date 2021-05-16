// O(n)
function crossAdd(input) {
    let answer = [];
    for (let i = 0; i < input.length; i++) {
        let goingUp = input[i];
        let goingDown = input[input.length - 1 - i];
        answer.push(goingUp + goingDown);
    }
    return answer;
}
console.log(crossAdd([1, 3, 5, 7]));

// O(n)
function find(needle, haystack) {
    for (let i = 0; i < haystack.length; i++) {
        if (haystack[i] === needle) return true;
    }
}
let haystack = ['hay', 'rabbit', 'needle', 'hat'];
console.log(find('needle', haystack));
console.log(find('bank', haystack));

// O(n2)
function makeTuples(input) {
    let answer = [];
    for (let i = 0; i < input.length; i++) {
        for (let j = 0; j < input.length; j++) {
            answer.push([input[i], input[j]]);
        }
    }
    return answer;
}
console.log(makeTuples([2, 4, 6]));
