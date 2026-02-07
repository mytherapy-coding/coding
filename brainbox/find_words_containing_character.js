// -------------------------
// Solution
// -------------------------
function findWordsContaining(words, x) {
  const result = [];
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes(x)) {
      result.push(i);
    }
  }
  return result;
}

// -------------------------
// Tests
// -------------------------
const tests = [
  { words: ["leet", "code"], x: "e", expected: [0, 1] },
  { words: ["abc", "bcd", "aaaa", "cbc"], x: "a", expected: [0, 2] },
  { words: ["hello", "world"], x: "z", expected: [] },
  { words: ["x", "xx", "abc"], x: "x", expected: [0, 1] },
  { words: ["apple", "banana", "kiwi"], x: "i", expected: [2] },
];

tests.forEach(({ words, x, expected }) => {
  const result = findWordsContaining(words, x);
  console.log(
    `words=${JSON.stringify(words)}, x="${x}" → ${JSON.stringify(result)} (expected ${JSON.stringify(expected)})`
  );
});
