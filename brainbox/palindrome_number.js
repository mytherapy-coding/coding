function isPalindrome(x) {
    if (x < 0) return false;
    return String(x) === String(x).split("").reverse().join("");
}


function testIsPalindrome() {
    console.assert(isPalindrome(121) === true, "121 should be true");
    console.assert(isPalindrome(0) === true, "0 should be true");
    console.assert(isPalindrome(1221) === true, "1221 should be true");

    console.assert(isPalindrome(123) === false, "123 should be false");
    console.assert(isPalindrome(10) === false, "10 should be false");
    console.assert(isPalindrome(-1) === false, "-1 should be false");

    console.log("All tests passed!");
}

testIsPalindrome();
