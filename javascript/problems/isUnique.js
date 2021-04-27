/**
 * @param {string} str
 * @returns {boolean}
 */

const isUnique = function(str) {
    const chars = {};
    for (let i = 0; i < str.length; i++) {
        if (typeof chars[str[i]] !== 'undefined') {
            return false;
        }
        chars[str[i]] = true;
    }
    return true;
}

// Using Set
function isUnique2(str) {
    return new Set(str).size === str.length;
}

console.log(isUnique('abcdef')); // -> true
console.log(isUnique('89%df#$^a&x')); // -> true
console.log(isUnique('abcAdef')); // -> true
console.log(isUnique('abcaef')); // -> false

