function countConsistentStrings(allowed, words) {
  const allowedSet = new Set(allowed);
  let count = 0;

  for (const w of words) {
    let ok = true;
    for (const ch of w) {
      if (!allowedSet.has(ch)) {
        ok = false;
        break;
      }
    }
    if (ok) count++;
  }

  return count;
}


const countConsistentStrings = require('./countConsistentStrings'); 
// or comment out the line above if running inline


test("example case", () => {
  expect(
    countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
  ).toBe(2);
});

test("all consistent", () => {
  expect(
    countConsistentStrings("abc", ["a", "bb", "ccc", "abc"])
  ).toBe(4);
});

test("none consistent", () => {
  expect(
    countConsistentStrings("a", ["b", "c", "d"])
  ).toBe(0);
});

test("empty allowed", () => {
  expect(
    countConsistentStrings("", ["a", "b", ""])
  ).toBe(1); // only "" is consistent
});

test("empty words", () => {
  expect(
    countConsistentStrings("abc", [])
  ).toBe(0);
});

test("mixed characters", () => {
  expect(
    countConsistentStrings("xyz", ["x", "xy", "yxz", "abc", "zzz"])
  ).toBe(4);
});

test("repeated characters", () => {
  expect(
    countConsistentStrings("ab", ["aaaa", "bbbb", "abab", "baba", "ccc"])
  ).toBe(4);
});
