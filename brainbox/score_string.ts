export function scoreOfString(s: string): number {
    let total = 0;
    for (let i = 0; i < s.length - 1; i++) {
        total += Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));
    }
    return total;
}


import { scoreOfString } from "./score_string";

function testScoreOfString() {
    console.assert(scoreOfString("hello") === 13, "Test 1 failed");
    console.assert(scoreOfString("abc") === 2, "Test 2 failed");
    console.assert(scoreOfString("aaa") === 0, "Test 3 failed");
    console.assert(scoreOfString("zaz") === 50, "Test 4 failed");
    console.assert(scoreOfString("") === 0, "Test 5 failed");
    console.assert(scoreOfString("a") === 0, "Test 6 failed");

    console.log("All tests passed!");
}

testScoreOfString();
