function shortestDistance(wordsDict, word1, word2) {
    let index1 = -1;
    let index2 = -1;
    let minDist = Infinity;

    for (let i = 0; i < wordsDict.length; i++) {
        const word = wordsDict[i];

        if (word === word1) {
            index1 = i;
        } else if (word === word2) {
            index2 = i;
        }

        if (index1 !== -1 && index2 !== -1) {
            minDist = Math.min(minDist, Math.abs(index1 - index2));
        }
    }

    return minDist;
}

// Test examples
console.log(shortestDistance(
    ["practice", "makes", "perfect", "coding", "makes"],
    "coding",
    "practice"
)); // 3

console.log(shortestDistance(
    ["practice", "makes", "perfect", "coding", "makes"],
    "makes",
    "coding"
)); // 1
